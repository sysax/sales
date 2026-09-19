"""
POS §6 — Flujo completo caja con pagos mixtos, promociones, ticket, cajón y corte
Cliente selector, descuentos, impuestos, pagos Efectivo/Tarjeta/Transferencia/Credito separados + cambio,
Impresión ticket, apertura/cierre caja, modo offline simulado
KivyMD 2.0.1
"""
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField, MDTextFieldLeadingIcon, MDTextFieldHintText, MDTextFieldHelperText
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp

from components.topbar import create_topbar
from components.theme import action_bar, flex_columns
from data.repository import repo
from data import offline as offline_mod
from components.printer import print_ticket, open_drawer


class POSScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "pos"
        self.cart = []
        self.confirm_dialog = None
        self.ticket_dialog = None
        self.promo_discount = 0.0
        self.promo_code = None
        self.promo_obj = None

        # ── Campos ──
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar SKU/nombre/categoria/barcode..."),
            mode="outlined", size_hint_x=1,
        )
        self.search_field.bind(text=self.on_search)

        self.client_field = MDTextField(
            MDTextFieldLeadingIcon(icon="account"),
            MDTextFieldHintText(text="Cliente (ej Juan Perez)"),
            MDTextFieldHelperText(text="Vendedor: ver clientes · deja vacío = Público general", mode="persistent"),
            mode="outlined", size_hint_x=1,
        )
        self.promo_field = MDTextField(
            MDTextFieldLeadingIcon(icon="tag"),
            MDTextFieldHintText(text="Código promo (ej ELEC10)"),
            MDTextFieldHelperText(text="2X1AUD, ELEC10, 50KOFF, VOL5, ABAR10", mode="persistent"),
            mode="outlined", size_hint_x=1,
        )
        # Pagos mixtos
        self.pay_efectivo = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Efectivo"), mode="outlined", text="0")
        self.pay_tarjeta = MDTextField(MDTextFieldLeadingIcon(icon="credit-card"), MDTextFieldHintText(text="Tarjeta"), mode="outlined", text="0")
        self.pay_transfer = MDTextField(MDTextFieldLeadingIcon(icon="bank-transfer"), MDTextFieldHintText(text="Transferencia"), mode="outlined", text="0")
        self.pay_credito = MDTextField(MDTextFieldLeadingIcon(icon="hand-coin"), MDTextFieldHintText(text="Crédito"), mode="outlined", text="0")

        self.products_grid = MDGridLayout(cols=3, spacing="12dp", padding="12dp", adaptive_height=True, size_hint_x=1)
        self.cart_table = MDDataTable(
            size_hint=(1, None), height="200dp", use_pagination=False,
            column_data=flex_columns(760,
                ("Producto", 2.8),
                ("Precio", 1.4),
                ("Cant", 1),
                ("Subtotal", 1.6),
            ),
            row_data=[],
        )
        # Labels COP
        self.lbl_items = MDLabel(text="Items: 0", font_style="Title", role="small", adaptive_height=True)
        self.lbl_subtotal = MDLabel(text="Subtotal: $0 COP", font_style="Body", role="small", adaptive_height=True)
        self.lbl_discount = MDLabel(text="Descuento: $0 COP", font_style="Body", role="small", theme_text_color="Custom", text_color="#4CAF50", adaptive_height=True)
        self.lbl_tax = MDLabel(text="IVA 19% DIAN: $0 COP", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True)
        self.lbl_total = MDLabel(text="$0 COP", font_style="Headline", role="large", halign="center", theme_text_color="Custom", text_color="#4CAF50", adaptive_height=True)
        self.lbl_cambio = MDLabel(text="Cambio: $0 COP", font_style="Title", role="small", halign="center", theme_text_color="Custom", text_color="#FF9800", adaptive_height=True)
        self.lbl_caja = MDLabel(text="Caja: Cerrada", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True)
        self.lbl_offline = MDLabel(text="Online", font_style="Body", role="small", halign="center", theme_text_color="Custom", text_color="#4CAF50", adaptive_height=True)

        self._build_products_grid()
        self._build_ui()
        self._refresh_caja_status()
        self._refresh_offline_status()
        # Monitor background: auto-badge + auto-sync al reconectar (offline real)
        try:
            offline_mod.start_monitor(on_change=self._on_connectivity_change, interval=10)
        except Exception:
            pass

    def _on_connectivity_change(self, online: bool):
        try:
            self._refresh_offline_status()
        except Exception:
            pass
        if online:
            try:
                synced, pending = offline_mod.sync_queue(repo)
                self._refresh_offline_status()
                if synced:
                    from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
                    MDSnackbar(MDSnackbarText(text=f"Reconectado — sincronizados {synced}, pendientes {pending}"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
            except Exception:
                pass

    def on_enter(self, *a):
        # re-consultar DB local (offline-first) + estado cola al entrar
        try:
            self._build_products_grid()
        except Exception:
            pass
        self._refresh_offline_status()
        self._refresh_caja_status()

    def _build_products_grid(self):
        self.products_grid.clear_widgets()
        try:
            products = repo.list_products()
        except Exception:
            products = []
        for p in products:
            if (p.get("stock", 0) or 0) > 0:
                self.products_grid.add_widget(self._make_product_card(p))

    def _make_product_card(self, product):
        return MDCard(
            MDLabel(text=product["name"], font_style="Title", role="small", adaptive_height=True),
            MDLabel(text=f"${product['price']:,.2f}", font_style="Headline", role="medium", halign="center", theme_text_color="Custom", text_color="#2196F3", adaptive_height=True),
            MDLabel(text=f"Stock:{product['stock']} Promo:{'Sí' if product['sku']=='P005' else '-'}", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            orientation="vertical", padding="12dp", size_hint_y=None, height="120dp",
            on_release=lambda x, p=product: self.add_to_cart(p["id"]),
        )

    def _build_ui(self):
        # Panel derecho con scroll
        right = MDBoxLayout(
            MDLabel(text="Carrito de Compra", font_style="Title", role="large", halign="center", adaptive_height=True, padding=(0,"8dp",0,"8dp")),
            self.client_field,
            self.promo_field,
            action_bar(
                MDButton(MDButtonText(text="Aplicar Promo"), style="outlined", on_release=lambda x: self._apply_promo()),
                MDButton(MDButtonText(text="Quitar Promo"), style="text", on_release=lambda x: self._clear_promo()),
                MDButton(MDButtonText(text="Limpiar Carrito"), style="text", on_release=lambda x: self.clear_cart()),
            ),
            self.cart_table,
            self.lbl_items,
            self.lbl_subtotal,
            self.lbl_discount,
            self.lbl_tax,
            MDBoxLayout(MDLabel(text="TOTAL:", font_style="Title", role="medium", adaptive_height=True), self.lbl_total, orientation="horizontal", adaptive_height=True, padding=("16dp","4dp","16dp","4dp")),
            MDLabel(text="Pagos mixtos (suma debe = TOTAL) — Efectivo calcula cambio", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
            MDGridLayout(MDBoxLayout(self.pay_efectivo), MDBoxLayout(self.pay_tarjeta), MDBoxLayout(self.pay_transfer), MDBoxLayout(self.pay_credito), cols=2, spacing="8dp", adaptive_height=True),
            self.lbl_cambio,
            action_bar(
                MDButton(MDButtonText(text="Apertura Caja"), style="outlined", on_release=lambda x: self._open_caja_dialog()),
                MDButton(MDButtonText(text="Cierre Caja"), style="outlined", on_release=lambda x: self._close_caja_dialog()),
            ),
            self.lbl_caja,
            self.lbl_offline,
            action_bar(
                MDButton(MDButtonText(text="Toggle Offline"), style="text", on_release=lambda x: self._toggle_offline()),
                MDButton(MDButtonText(text="Sincronizar"), style="text", on_release=lambda x: self._sync_offline()),
            ),
            MDButton(MDButtonText(text="Procesar Venta + Ticket + Cajón"), style="filled", size_hint_x=1, on_release=lambda x: self.process_sale()),
            orientation="vertical", adaptive_height=True, spacing="6dp", padding="8dp", size_hint_x=1,
        )
        scroll_right = MDScrollView(right, do_scroll_x=False, size_hint_x=0.45)

        left = MDBoxLayout(self.search_field, MDScrollView(self.products_grid, do_scroll_x=False), orientation="vertical", size_hint_x=0.55, padding="8dp")

        self.add_widget(MDBoxLayout(create_topbar("Punto de Venta"), MDBoxLayout(left, scroll_right, orientation="horizontal"), orientation="vertical"))

    def _refresh_caja_status(self):
        s = repo.get_caja_status()
        if s["open"]:
            self.lbl_caja.text = f"Caja ABIERTA por {s['opening_user']} ${s['opening_amount']:.0f} COP — ventas {len(s['sales_today'])} tot ${s['total_sales']:.0f} COP esperado ${s['expected']:.0f} COP"
            self.lbl_caja.text_color = "#4CAF50"
        else:
            self.lbl_caja.text = "Caja CERRADA — abra caja para vender (Apertura)"
            self.lbl_caja.text_color = "#F44336"

    def _refresh_offline_status(self):
        online = offline_mod.is_online()
        queued = len(offline_mod.get_queue())
        try:
            from data import dian as dian_mod
            dian_on = dian_mod.is_enabled()
        except Exception:
            dian_on = False
        if online:
            self.lbl_offline.text = f"● Online — cola {queued}" + (" — DIAN sincrónico" if dian_on else "")
            self.lbl_offline.text_color = "#4CAF50"
        else:
            self.lbl_offline.text = f"● OFFLINE — cola {queued} — guardado local, sync pendiente"
            self.lbl_offline.text_color = "#F44336"

    def _toggle_offline(self):
        # switch manual: flag persistente en offline_mod (+ mock para compat)
        offline_mod.set_offline_forced(not offline_mod.is_offline_forced())
        try:
            from data import mock_data as db_mock
            db_mock.IS_OFFLINE = offline_mod.is_offline_forced()
        except Exception:
            pass
        self._refresh_offline_status()
        MDSnackbar(MDSnackbarText(text=f"Modo {'OFFLINE' if offline_mod.is_offline_forced() else 'Online'}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()

    def _sync_offline(self):
        synced, pending = offline_mod.sync_queue(repo)
        self._refresh_offline_status()
        MDSnackbar(MDSnackbarText(text=f"Sincronizados {synced}, pendientes {pending}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Búsqueda / carrito ──
    def on_search(self, instance, value):
        try:
            filtered = repo.search_products(value)
        except Exception:
            filtered = []
        self.products_grid.clear_widgets()
        for p in filtered:
            if (p.get("stock", 0) or 0) > 0:
                self.products_grid.add_widget(self._make_product_card(p))

    def add_to_cart(self, product_id):
        prod = repo.find_product(product_id)
        if not prod: return
        in_cart = next((i for i in self.cart if i["id"]==product_id), None)
        cur = in_cart["qty"] if in_cart else 0
        if cur >= prod["stock"]:
            MDSnackbar(MDSnackbarText(text=f"Stock insuficiente {prod['name']}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        if in_cart:
            in_cart["qty"]+=1; in_cart["subtotal"]=in_cart["qty"]*prod["price"]
        else:
            self.cart.append({"id": prod["id"], "name": prod["name"], "price": prod["price"], "qty":1, "subtotal": prod["price"]})
        self._refresh_cart()

    def _refresh_cart(self):
        self.cart_table.row_data = [(i["name"][:14], f"${i['price']:,.0f}", str(i["qty"]), f"${i['subtotal']:,.0f}") for i in self.cart]
        subtotal = sum(i["subtotal"] for i in self.cart)
        # promo descuento ya calculado, si cart cambió recalcular si había promo
        if self.promo_code and self.promo_obj:
            try:
                disc, _ = repo.apply_promo(self.cart, self.promo_code)
                self.promo_discount = disc
            except Exception:
                disc = self.promo_discount
        else:
            disc = self.promo_discount
        # cliente descuento (si cliente tiene discount) — DB local, funciona offline
        client_name = (self.client_field.text or "").strip()
        try:
            cli = repo.find_client(client_name) if client_name else None
        except Exception:
            cli = None
        cli_disc = 0
        if cli and cli.get("discount",0):
            cli_disc = subtotal * cli["discount"]/100
        total_discount = disc + cli_disc
        taxable = max(0, subtotal - total_discount)
        tax = taxable * 0.19  # IVA Colombia 19% DIAN
        total = taxable + tax
        self.lbl_items.text = f"Items: {sum(i['qty'] for i in self.cart)}"
        self.lbl_subtotal.text = f"Subtotal: ${subtotal:,.0f} COP" + (f" (-{cli_disc:.0f} cliente {cli['discount']}%)" if cli_disc else "")
        self.lbl_discount.text = f"Descuento: -${total_discount:,.0f} COP" + (f" promo {self.promo_code}" if self.promo_code else "")
        self.lbl_tax.text = f"IVA 19% DIAN: ${tax:,.0f} COP"
        self.lbl_total.text = f"${total:,.0f} COP"
        # cambio preview
        try:
            ef = float(self.pay_efectivo.text or 0)
            # si solo efectivo supera total, cambio = ef - (total - otros pagos)
            otros = float(self.pay_tarjeta.text or 0) + float(self.pay_transfer.text or 0) + float(self.pay_credito.text or 0)
            if ef + otros >= total and ef>0:
                self.lbl_cambio.text = f"Cambio: ${max(0, ef+otros - total):,.0f} COP"
            else:
                falta = total - (ef+otros)
                self.lbl_cambio.text = f"Falta por pagar: ${max(0,falta):,.0f} COP"
        except Exception:
            self.lbl_cambio.text = "Cambio: $0 COP"
        return subtotal, total_discount, tax, total

    def clear_cart(self):
        self.cart=[]; self.promo_discount=0; self.promo_code=None; self.promo_obj=None
        # no limpiamos cliente ni pagos para agilizar siguiente venta, pero reseteamos pagos a 0
        self.pay_efectivo.text="0"; self.pay_tarjeta.text="0"; self.pay_transfer.text="0"; self.pay_credito.text="0"
        self.promo_field.text=""
        self._refresh_cart()

    def _apply_promo(self):
        code = (self.promo_field.text or "").strip().upper()
        if not code:
            MDSnackbar(MDSnackbarText(text="Ingrese código promo"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()
            return
        if not self.cart:
            MDSnackbar(MDSnackbarText(text="Carrito vacío"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()
            return
        try:
            disc, promo = repo.apply_promo(self.cart, code)
            self.promo_discount = disc
            self.promo_code = code
            self.promo_obj = promo
            self._refresh_cart()
            MDSnackbar(MDSnackbarText(text=f"Promo {code} aplicada -${disc:,.2f} ({promo['name']})"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _clear_promo(self):
        self.promo_discount=0; self.promo_code=None; self.promo_obj=None
        self.promo_field.text=""
        self._refresh_cart()
        MDSnackbar(MDSnackbarText(text="Promo quitada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()

    # ── Caja ──
    def _open_caja_dialog(self):
        f = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Monto apertura *"), MDTextFieldHelperText(text="Ej 2000", mode="persistent"), mode="outlined", text="2000")
        self._fields = {"open": f}
        self.confirm_dialog = MDDialog(
            MDDialogHeadlineText(text="Apertura de caja"),
            MDDialogSupportingText(text="Registra fondo inicial — todas las ventas se suman al esperado"),
            f,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.confirm_dialog.dismiss()), MDButton(MDButtonText(text="Abrir"), style="filled", on_release=lambda x: self._do_open_caja()), spacing="8dp"),
        )
        self.confirm_dialog.open()
    def _do_open_caja(self):
        try:
            amt = self._fields["open"].text.strip()
            app = MDApp.get_running_app()
            repo.open_caja(amt, user=app.current_user.get("username","sistema") if app.current_user else "sistema")
            self.confirm_dialog.dismiss()
            self._refresh_caja_status()
            MDSnackbar(MDSnackbarText(text=f"Caja abierta ${float(amt):,.0f}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _close_caja_dialog(self):
        f = MDTextField(MDTextFieldLeadingIcon(icon="cash-check"), MDTextFieldHintText(text="Monto contado en cajón *"), mode="outlined")
        self._fields = {"close": f}
        s = repo.get_caja_status()
        info = f"Esperado ${s['expected']:.0f} (apertura ${s['opening_amount']:.0f} + ventas ${s['total_sales']:.0f})" if s["open"] else "Caja cerrada"
        self.confirm_dialog = MDDialog(
            MDDialogHeadlineText(text="Cierre de caja"),
            MDDialogSupportingText(text=info),
            f,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.confirm_dialog.dismiss()), MDButton(MDButtonText(text="Cerrar y cuadrar"), style="filled", on_release=lambda x: self._do_close_caja()), spacing="8dp"),
        )
        self.confirm_dialog.open()
    def _do_close_caja(self):
        try:
            amt = self._fields["close"].text.strip()
            app = MDApp.get_running_app()
            res = repo.close_caja(amt, user=app.current_user.get("username","sistema") if app.current_user else "sistema")
            self.confirm_dialog.dismiss()
            self._refresh_caja_status()
            # ticket de cierre COP
            self.ticket_dialog = MDDialog(
                MDDialogHeadlineText(text="Corte de caja"),
                MDDialogSupportingText(text=f"Esperado ${res['expected']:,.0f} COP\nContado ${res['counted']:,.0f} COP\nDiferencia {res['diff']:+.0f} COP\nVentas {res['sales_count']} tot ${res['total_sales']:,.0f} COP"),
                MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.ticket_dialog.dismiss()), spacing="8dp"),
            )
            self.ticket_dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Procesar venta ──
    def process_sale(self):
        if not self.cart:
            MDSnackbar(MDSnackbarText(text="Carrito vacío"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()
            return
        if not repo.get_caja_status()["open"]:
            MDSnackbar(MDSnackbarText(text="Abra caja primero (Apertura)"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        subtotal, discount, tax, total = self._refresh_cart()
        # validar cliente — DB local (offline-first)
        client_name = (self.client_field.text or "").strip() or "Público general"
        try:
            cli = repo.find_client(client_name) if client_name != "Público general" else None
        except Exception:
            cli = None
        if client_name!="Público general" and not cli:
            MDSnackbar(MDSnackbarText(text=f"Cliente {client_name} no existe — use nombre exacto o vacío"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        # validar pagos mixtos
        try:
            ef = float(self.pay_efectivo.text or 0)
            tar = float(self.pay_tarjeta.text or 0)
            tr = float(self.pay_transfer.text or 0)
            cre = float(self.pay_credito.text or 0)
        except Exception:
            MDSnackbar(MDSnackbarText(text="Pagos deben ser numéricos"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        suma = ef+tar+tr+cre
        # si solo un método y es 0, auto-asignar total a efectivo
        if suma==0:
            ef = total
            self.pay_efectivo.text = f"{total:.0f}"
            suma = total
        if abs(suma - total) > 0.01 and not (ef+tar+tr+cre >= total and cre==0):  # permite sobrepago solo efectivo (cambio)
            MDSnackbar(MDSnackbarText(text=f"Pagos ${suma:,.2f} no cuadran con total ${total:,.2f}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        # crédito validación límite
        if cre>0 and cli:
            if cli.get("status")=="bloqueado":
                MDSnackbar(MDSnackbarText(text="Cliente bloqueado (moroso)"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
                return
            if cre + cli.get("balance",0) > cli.get("credit_limit",0):
                MDSnackbar(MDSnackbarText(text=f"Límite crédito excedido: {cli.get('balance',0)}+{cre}>{cli.get('credit_limit',0)}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
                return
        cambio = max(0, suma - total)
        # dialogo resumen COP 19% DIAN
        items_txt = "\n".join([f"{it['name'][:14]} x{it['qty']} = ${it['subtotal']:,.0f} COP" for it in self.cart])
        self.confirm_dialog = MDDialog(
            MDDialogHeadlineText(text="Confirmar venta — Colombia COP"),
            MDDialogSupportingText(text=f"Cliente: {client_name} (NIT)\n{items_txt}\n\nSubtotal ${subtotal:,.0f} COP Desc -${discount:,.0f} IVA 19% DIAN ${tax:,.0f} COP\nTOTAL ${total:,.0f} COP\nPagos: Ef ${ef:.0f} Tarj ${tar:.0f} Trans ${tr:.0f} Cred ${cre:.0f} Cambio ${cambio:.0f} COP\nPromo: {self.promo_code or '-'}"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.confirm_dialog.dismiss()), MDButton(MDButtonText(text=f"Pagar ${total:,.0f}"), style="filled", on_release=lambda x: self._confirm_sale(client_name, {"efectivo":ef,"tarjeta":tar,"transferencia":tr,"credito":cre}, cambio, discount, tax)), spacing="8dp"),
        )
        self.confirm_dialog.open()

    def _confirm_sale(self, client_name, payments, cambio, discount, tax):
        total = sum(i["subtotal"] for i in self.cart) - discount + tax
        # repo.create_sale maneja pagos dict y promo — siempre local (offline-first)
        # doc_type lo define data/dian.py (Ticket interno si DIAN OFF)
        sale = repo.create_sale(client_name=client_name, total=total, payment=payments, cart_items=list(self.cart), promo_code=self.promo_code, discount=discount, tax=tax, payments=payments)
        folio = sale["id"]
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        repo.log(user, "venta_pos", f"{folio} {client_name} ${total:.0f} COP pago {payments}")
        if self.confirm_dialog:
            self.confirm_dialog.dismiss()
        # Offline REAL: venta ya guardada local (offline-first). Solo se encola
        # el trabajo remoto pendiente (DIAN) con idempotencia por folio.
        online = offline_mod.is_online()
        if not online:
            offline_mod.queue_operation("sale", {"folio": folio, "client": client_name, "total": total, "payments": payments, "cart": list(self.cart), "user": user, "cufe": sale.get("dian_cufe", f"CUFE-{folio}-DIAN"), "ts": sale.get("date")}, idempotency_key=f"sale-{folio}")
            offline_mod.queue_operation("dian", {"folio": folio, "cufe": sale.get("dian_cufe", f"CUFE-{folio}-DIAN"), "user": user}, idempotency_key=f"dian-{folio}")
            sale["dian_status"] = "PENDIENTE_OFFLINE"
        else:
            sale["dian_status"] = "SINCRONIZADO"
        # Ticket + cajón — siempre guarda archivo, intenta ESC/POS y lp
        # DIAN solo se muestra si está activado (data/dian.py); si no, ticket interno.
        printed = print_ticket(sale, list(self.cart), client_name, payments, cambio, discount, tax, promo_code=self.promo_code)
        drawer_ok, drawer_dev = open_drawer()
        self._refresh_offline_status()
        self._refresh_caja_status()
        # Ticket — muestra ruta y offline
        items_ticket = "\n".join([f"{it['name'][:16]:16} {it['qty']:2} x ${it['price']:,.0f} COP = ${it['subtotal']:,.0f} COP" for it in self.cart])
        try:
            from data import dian as dian_mod
            dian_on = dian_mod.is_enabled()
        except Exception:
            dian_on = False
        if not online:
            offline_note = "OFFLINE — guardado local" + (", se sincroniza DIAN al reconectar" if dian_on else ", se sincroniza al reconectar")
        else:
            offline_note = "Online" + (" — DIAN sincrónico" if dian_on else "")
        dian_line = f"\nCUFE DIAN: {sale.get('dian_cufe', 'CUFE-'+folio+'-DIAN')} [{sale.get('dian_status')}]" if dian_on else ""
        ticket_title = f"Ticket DIAN {folio} — Cajón — COP" if dian_on else f"Ticket {folio} — Cajón — COP"
        print_note = f"Ticket guardado: {printed['path']}" if printed["path"] else "Ticket no guardado"
        drawer_note = f"Cajón: {'abierto '+drawer_dev if drawer_ok else 'sin hardware ('+str(drawer_dev)+')'}"
        self.ticket_dialog = MDDialog(
            MDDialogHeadlineText(text=ticket_title),
            MDDialogSupportingText(text=f"Cliente: {client_name} NIT\n{items_ticket}\n\nDesc -${discount:,.0f} COP IVA 19% ${tax:,.0f} COP\nTOTAL ${total:,.0f} COP\nPagado: Ef ${payments['efectivo']:.0f} Tarj ${payments['tarjeta']:.0f} Trans ${payments['transferencia']:.0f} Cred ${payments['credito']:.0f}\nCambio ${cambio:.0f} COP{dian_line}\n{offline_note}\n{print_note}\n{drawer_note}\nGracias por su compra! — abarrotes/electrónica — Colombia — documento interno sin validez fiscal DIAN" if not dian_on else f"Cliente: {client_name} NIT\n{items_ticket}\n\nDesc -${discount:,.0f} COP IVA 19% DIAN ${tax:,.0f} COP\nTOTAL ${total:,.0f} COP\nPagado: Ef ${payments['efectivo']:.0f} Tarj ${payments['tarjeta']:.0f} Trans ${payments['transferencia']:.0f} Cred ${payments['credito']:.0f}\nCambio ${cambio:.0f} COP{dian_line}\n{offline_note}\n{print_note}\n{drawer_note}\nGracias por su compra! — abarrotes/electrónica — Colombia"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cerrar"), style="filled", on_release=lambda x: (self.ticket_dialog.dismiss(), self.clear_cart(), self._build_products_grid(), self._refresh_caja_status(), self._refresh_offline_status())), spacing="8dp"),
        )
        self.ticket_dialog.open()
        MDSnackbar(MDSnackbarText(text=f"Venta {folio} ${total:,.0f} COP — {offline_note} — {drawer_note}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.9).open()

