###### **KivyMD** **_Release 2.0.1.dev0_** 

**Aug 20, 2026** 

###### **CONTENTS** 

|**1**<br>**Kiv**|**yMD**|**1**|
|---|---|---|
|**2**<br>**Con**|**tents**|**3**|
|2.1|Getting Started . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . .<br>3|
|2.2|Themes . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . .<br>7|
|2.3|Components<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . .<br>37|
|2.4|Controllers . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 615|
|2.5|Behaviors . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 616|
|2.6|Efects<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 674|
|2.7|Changelog<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 675|
|2.8|About . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 693|
|2.9|KivyMD . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . 693|
|**3**<br>**Indi**|**ces and tables**|**729**|
|**Python**|**Module Index**|**731**|
|**Index**||**733**|



**i** 

**ii** 



<!-- Start of picture text -->
} — SN = . Men, .<br>rm ae x rw)<br>eS (isa<br>{|¥ 4 LoungeisaDN; a. a|| ¢, a » ’<br>.|<br>,B<br>u ss<br>peBlue Bottle Coffee © .<br>46 ok ok ot 359 reviews »$ Chronomart $380<br>Coffee Shop<br>= FEYERT Logo Office Lady Fashion<br>& * ® ‘SmallStrap WristDial Stainless Watch  Steel Leather<br>Trendy cafe chain offering upscale coffee drink & . 7) More information v<br>pastries, plus beans & brewing equipment<br>- Beautiful 3D Design Dial, with '7 marking<br>Q 315 Linden st, san Francisco, CA 94102 -“Durable Comfortablestainless Soft Leathersteel buckle Watch Band<br>Open today: 7:00 AM-. 6:00 PM ; -- Precise Comfortable Quartz for movementEveryday Wear for accurate ti<br>lySH TworlneSecondary temtext withhereavatar WARRANTY- For defective INFORMATION:products, buyers may return<br>. the Zalora PH return period (within 30 days<br>"]] THIS WARRANTY DOES NOT COVER:<br>- Damage resulting from impact, accidents, Menu:<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

**Chapter 1. KivyMD** 

**2** 

**CHAPTER TWO** 

###### **CONTENTS** 

###### **2.1 Getting Started** 

In order to start using _KivyMD_ , you must first install the Kivy framework on your computer. Once you have installed _Kivy_ , you can install _KivyMD_ . 

**Warning:** _KivyMD_ depends on _Kivy_ ! Therefore, before using _KivyMD_ , first learn how to work with _Kivy_ . 

###### **2.1.1 Installation** 

pip install kivymd 

Command above will install latest release version of KivyMD from PyPI. If you want to install development version from master branch, you should specify link to zip archive: 

pip install https://github.com/kivymd/KivyMD/archive/master.zip 

**Note:** Replace _master.zip_ with _<commit hash>.zip_ (eg _51b8ef0.zip_ ) to download KivyMD from specific commit. 

Also you can install manually from sources. Just clone the project and run pip: 

```
gitclonehttps://github.com/kivymd/KivyMD.git--depth1
cdKivyMD
pipinstall.
```

**Note:** If you don’t need full commit history (about 320 MiB), you can use a shallow clone ( _git clone https://github.com/kivymd/KivyMD.git –depth 1_ ) to save time. If you need full commit history, then remove _–depth 1_ . 

**3** 









**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV="""
#:importget_color_from_hexkivy.utils.get_color_from_hex
<RectangleFlatButton>:
ripple_color:0,0,0,.2
background_color:0,0,0,0
color:root.primary_color
canvas.before:
Color:
rgba:root.primary_color
Line:
width:1
rectangle:(self.x,self.y,self.width,self.height)
Screen:
canvas:
Color:
rgba:get_color_from_hex("#0F0F0F")
Rectangle:
pos:self.pos
size:self.size
"""
classRectangleFlatButton(TouchRippleBehavior,Button):
primary_color=get_color_from_hex("#EB8933")
defon_touch_down(self,touch):
collide_point=self.collide_point(touch.x,touch.y)
ifcollide_point:
touch.grab(self)
self.ripple_show(touch)
returnTrue
returnFalse
defon_touch_up(self,touch):
iftouch.grab_currentisself:
touch.ungrab(self)
self.ripple_fade()
returnTrue
returnFalse
classMainApp(App):
defbuild(self):
screen=Builder.load_string(KV)
screen.add_widget(
RectangleFlatButton(
text="Hello,World",
```

(continues on next page) 

**2.1. Getting Started** 

**5** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=(None, None), size=(dp(110), dp(35)), ripple_color=(0.8, 0.8, 0.8, 0.5), ) ) return screen MainApp().run()` **2.1.5 And the equivalent with** **_KivyMD_** `from kivymd.app import MDApp from kivymd.uix.screen import MDScreen from kivymd.uix.button import MDButton, MDButtonText class MainApp(MDApp): def build(self): self.theme_cls.theme_style = "Dark" self.theme_cls.primary_palette = "Orange" return ( MDScreen( MDButton( MDButtonText( text="Hello, World", ), pos_hint={"center_x": 0.5, "center_y": 0.5}, ) ) ) MainApp().run()` 

**Chapter 2. Contents** 

**6** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.1.6** **_KivyMD_** 

###### **2.1.7** **_Kivy_** 

###### **2.2 Themes** 

###### **2.2.1 Theming** 

###### **See also:** 

Material Design spec, Dynamic color 

###### **Material App** 

The main class of your application, which in _Kivy_ inherits from the `App` class, in _KivyMD_ must inherit from the _`MDApp`_ class. The _`MDApp`_ class has properties that allow you to control application properties such as `color/style/font` of interface elements and much more. 

###### **Control material properties** 

The main application class inherited from the _`MDApp`_ class has the _`theme_cls`_ attribute, with which you control the material properties of your application. 

###### **API -** `kivymd.theming` 

###### `kivymd.theming.set_dark_mode_listener` 

###### `class kivymd.theming.ThemeManager(` _**kwargs_ `)` 

Dynamic color class. 

Added in version 2.0.0. 

###### `primary_palette` 

The name of the color scheme that the application will use. All major _material_ components will have the color of the specified color theme. 

Works like a `ColorProperty` , but also accepts color names from `kivy.utils.hex_colormap` , including keys with capital letters. 

To change the color scheme of an application: 

Imperative python style with KV 

**2.2. Themes** 

**7** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
style:"elevated"
pos_hint:{"center_x":.5,"center_y":.5}
MDButtonIcon:
icon:"plus"
MDButtonText:
text:"Button"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"#"Purple","Red"
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonIcon,MDButtonText
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"#"Purple","Red"
return(
MDScreen(
MDButton(
MDButtonIcon(
icon="plus",
),
MDButtonText(
text="Button",
),
style="elevated",
pos_hint={"center_x":0.5,"center_y":0.5},
),
```

(continues on next page) 

**Chapter 2. Contents** 

**8** 





<!-- Start of picture text -->
+ Button + Button + Button<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color:app.theme_cls.surfaceColor
MDButton:
style:"elevated"
pos_hint:{"center_x":.5,"center_y":.5}
MDButtonIcon:
icon:"plus"
MDButtonText:
text:"Elevated"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_resume(self,*args):
'''Updatingthecolorschemewhentheapplicationresumes.'''
self.theme_cls.set_colors()
defset_dynamic_color(self,*args)->None:
'''
Whensetsthe�dynamic_color�value,theselfmethodwillbe
�called.theme_cls.set_colors()�whichwillgenerateacolor
schemefromacustomwallpaperif�dynamic_color�is�True�.
'''
self.theme_cls.dynamic_color=True
defon_start(self)->None:
'''
Itisfiredatthestartoftheapplicationandrequeststhe
necessarypermissions.
'''
defcallback(permission,results):
ifall([resforresinresults]):
Clock.schedule_once(self.set_dynamic_color)
ifplatform=="android":
fromandroid.permissionsimportPermission,request_permissions
permissions=[Permission.READ_EXTERNAL_STORAGE]
request_permissions(permissions,callback)
Example().run()
```

Declarative python style 

**Chapter 2. Contents** 

**10** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivyimportplatform
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonIcon,MDButtonText
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
return(
MDScreen(
MDButton(
MDButtonIcon(
icon="plus",
),
MDButtonText(
text="Elevated",
),
style="elevated",
pos_hint={"center_x":.5,"center_y":.5},
),
md_bg_color=self.theme_cls.surfaceColor,
)
)
defon_resume(self,*args):
'''Updatingthecolorschemewhentheapplicationresumes.'''
self.theme_cls.set_colors()
defset_dynamic_color(self,*args)->None:
'''
Whensetsthe�dynamic_color�value,theselfmethodwillbe
�called.theme_cls.set_colors()�whichwillgenerateacolor
schemefromacustomwallpaperif�dynamic_color�is�True�.
'''
self.theme_cls.dynamic_color=True
defon_start(self)->None:
'''
Itisfiredatthestartoftheapplicationandrequeststhe
necessarypermissions.
'''
defcallback(permission,results):
ifall([resforresinresults]):
Clock.schedule_once(self.set_dynamic_color)
ifplatform=="android":
fromandroid.permissionsimportPermission,request_permissions
```

(continues on next page) 

**2.2. Themes** 

**11** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
permissions=[Permission.READ_EXTERNAL_STORAGE]
request_permissions(permissions,callback)
```

```
Example().run()
```

_`dynamic_color`_ is an `BooleanProperty` and defaults to _False_ . 

###### `dynamic_scheme_name` 

Name of the dynamic scheme. Availabe schemes _TONAL_SPOT_ , _SPRITZ VIBRANT_ , _EXPRESSIVE_ , _FRUIT_SALAD_ , _RAINBOW_ , _MONOCHROME_ , _FIDELITY_ and _CONTENT_ . 

_`dynamic_scheme_name`_ is an `OptionProperty` and defaults to _‘TONAL_SPOT’_ . 

###### `dynamic_scheme_contrast` 

The contrast of the generated color scheme. 

_`dynamic_scheme_contrast`_ is an `NumericProperty` and defaults to _0.0_ . 

###### `path_to_wallpaper` 

The path to the image to set the color scheme. You can use this option if you want to use dynamic color on platforms other than the Android platform. 

Added in version 2.0.0. 

_`path_to_wallpaper`_ is an `StringProperty` and defaults to _‘’_ . 

###### `theme_style_switch_animation` 

Animate app colors when switching app color scheme (‘Dark/light’). 

Added in version 1.1.0. 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDCard:
orientation:"vertical"
padding:0,0,0,"36dp"
size_hint:.5,.5
style:"elevated"
pos_hint:{"center_x":.5,"center_y":.5}
MDLabel:
text:"Themestyle-{}".format(app.theme_cls.theme_style)
halign:"center"
valign:"center"
bold:True
font_style:"Display"
```

(continues on next page) 

**Chapter 2. Contents** 

**12** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
role:"small"
MDButton:
on_release:app.switch_theme_style()
pos_hint:{"center_x":.5}
MDButtonText:
text:"Settheme"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style_switch_animation=True
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
returnBuilder.load_string(KV)
defswitch_theme_style(self):
self.theme_cls.primary_palette=(
"Orange"ifself.theme_cls.primary_palette=="Red"else"Red"
)
self.theme_cls.theme_style=(
"Dark"ifself.theme_cls.theme_style=="Light"else"Light"
)
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.cardimportMDCard
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style_switch_animation=True
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
return(
MDScreen(
MDCard(
MDLabel(
id="label",
text="Themestyle-{}".format(
self.theme_cls.theme_style),
```

(continues on next page) 

**2.2. Themes** 

**13** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `halign="center", valign="center", bold=True, font_style="Display", role="small", ), MDButton( MDButtonText( text="Set theme", ), on_release=self.switch_theme_style, pos_hint={"center_x": 0.5}, ), id="card", orientation="vertical", padding=(0, 0, 0, "36dp"), size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}, style="elevated", ) ) ) def on_start(self): def on_start(*args): self.root.md_bg_color = self.theme_cls.backgroundColor Clock.schedule_once(on_start) def switch_theme_style(self, *args): self.theme_cls.primary_palette = ( "Orange" if self.theme_cls.primary_palette == "Red" else "Red" ) self.theme_cls.theme_style = ( "Dark" if self.theme_cls.theme_style == "Light" else "Light" ) self.root.get_ids().label.text = ( "Theme style - {}".format(self.theme_cls.theme_style) ) Example().run()` 

_`theme_style_switch_animation`_ is an `BooleanProperty` and defaults to _True_ . 

###### `theme_style_switch_animation_duration` 

Duration of the animation of switching the color scheme of the application (“Dark/light”). 

Added in version 1.1.0. 

```
classExample(MDApp):
```

(continues on next page) 

**Chapter 2. Contents** 

**14** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `def build(self): self.theme_cls.theme_style_switch_animation = True self.theme_cls.theme_style_switch_animation_duration = 0.8` 

_`theme_style_switch_animation_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `follow_system_theme` 

Automatically follows the Android system theme. 

When set to `True` , the application automatically switches between `"Light"` and `"Dark"` theme styles when the Android system appearance changes. On other platforms, this property has no effect. 

Added in version 2.0.0. 

Declarative style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLabel:
text:"Changethesystemthemeonyourdevice."
pos_hint:{"center_x":.5,"center_y":.5}
adaptive_size:True
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.follow_system_theme=True
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
```

`class Example(MDApp): def build(self): self.theme_cls.follow_system_theme = True return ( MDScreen( MDLabel( text="Change the system theme on your device.",` (continues on next page) 

**2.2. Themes** 

**15** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `pos_hint={"center_x": .5, "center_y": .5}, adaptive_size=True, ), md_bg_color=self.theme_cls.backgroundColor ) ) Example().run()` 

_`follow_system_theme`_ is a `BooleanProperty` and defaults to _False_ . 

###### `theme_style` 

App theme style. 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.buttonimportMDButton,MDButtonText
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Light"#"Dark"
returnMDScreen(
MDButton(
MDButtonText(
text="Hello,World",
),
style="outlined",
pos_hint={"center_x":0.5,"center_y":0.5},
)
)
defon_start(self):
defon_start(*args):
self.root.md_bg_color=self.theme_cls.backgroundColor
Clock.schedule_once(on_start)
Example().run()
```



_`theme_style`_ is an `OptionProperty` and defaults to _‘Light’_ . 

**Chapter 2. Contents** 

**16** 

**KivyMD, Release 2.0.1.dev0** 

###### `disabled_hint_text_color` 

Color of the disabled text used in the `MDTextField` . 

_`disabled_hint_text_color`_ is an `AliasProperty` that returns the value in `rgba` format for _`disabled_hint_text_color`_ , property is readonly. 

###### `device_orientation` 

Device orientation. 

_`device_orientation`_ is an `StringProperty` and defaults to _‘’_ . 

###### `font_styles` 

Data of default font styles. 

###### **Add custom font** 

Declarative style with KV 

```
fromkivy.core.textimportLabelBase
fromkivy.langimportBuilder
fromkivy.metricsimportsp
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLabel:
text:"MDLabel"
halign:"center"
font_style:"nasalization"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
LabelBase.register(
name="nasalization",
fn_regular="nasalization.ttf",
)
self.theme_cls.font_styles["nasalization"]={
"large":{
"line-height":1.64,
"font-name":"nasalization",
"font-size":sp(57),
},
"medium":{
"line-height":1.52,
"font-name":"nasalization",
"font-size":sp(45),
```

(continues on next page) 

**2.2. Themes** 

**17** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
},
"small":{
"line-height":1.44,
"font-name":"nasalization",
"font-size":sp(36),
},
}
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

`from kivy.core.text import LabelBase from kivy.metrics import sp from kivymd.uix.label import MDLabel from kivymd.uix.screen import MDScreen from kivymd.app import MDApp class Example(MDApp): def build(self): self.theme_cls.theme_style = "Dark" LabelBase.register( name="nasalization", fn_regular="/Users/urijivanov/Projects/Dev/MyGithub/Articles/` _˓→_ `StarTest/data/font/nasalization-rg.ttf", ) self.theme_cls.font_styles["nasalization"] = { "large": { "line-height": 1.64, "font-name": "nasalization", "font-size": sp(57), }, "medium": { "line-height": 1.52, "font-name": "nasalization", "font-size": sp(45), }, "small": { "line-height": 1.44, "font-name": "nasalization", "font-size": sp(36), }, } return (` 

(continues on next page) 

**Chapter 2. Contents** 

**18** 





**KivyMD, Release 2.0.1.dev0** 

- onPrimaryColor 

- onPrimaryContainerColor 

- onPrimaryFixedColor 

- onPrimaryFixedVariantColor 

- onSecondaryColor 

- onSecondaryContainerColor 

- onSecondaryFixedColor 

- onSecondaryFixedVariantColor 

- onSurfaceColor 

- onSurfaceLightColor 

- onSurfaceVariantColor 

- onTertiaryColor 

- onTertiaryContainerColor 

- onTertiaryFixedColor 

- onTertiaryFixedVariantColor 

- outlineColor 

- outlineVariantColor 

- primaryColor 

- primaryContainerColor 

- primaryDimColor 

- primaryFixedColor 

- primaryFixedDimColor 

- primaryPaletteKeyColorColor 

- rippleColor 

- scrimColor 

- secondaryColor 

- secondaryContainerColor 

- secondaryDimColor 

- secondaryFixedColor 

- secondaryFixedDimColor 

- secondaryPaletteKeyColorColor 

- shadowColor 

- surfaceBrightColor 

- surfaceColor 

- surfaceContainerColor 

- surfaceContainerHighColor 

**Chapter 2. Contents** 

**20** 

**KivyMD, Release 2.0.1.dev0** 

- surfaceContainerHighestColor 

- surfaceContainerLowColor 

- surfaceContainerLowestColor 

- surfaceDimColor 

- surfaceTintColor 

- surfaceVariantColor 

- tertiaryColor 

- tertiaryContainerColor 

- tertiaryDimColor 

- tertiaryFixedColor 

- tertiaryFixedDimColor 

- tertiaryPaletteKeyColorColor 

- transparentColor 

_`dynamic_color_names`_ is an `AliasProperty` and for internal usage only. 

- `set_colors(` _*args_ `)` _→_ None 

Fired methods for setting a new color scheme. 

###### `update_theme_colors(` _*args_ `)` _→_ None 

Fired when the _`theme_style`_ value changes. 

- `on_follow_system_theme(` _instance_ , _value_ `)` _→_ None 

Fired when the _`follow_system_theme`_ value changes. 

- `on_dynamic_scheme_name(` _*args_ `)` _→_ None 

Fired when the _`dynamic_scheme_name`_ value changes. 

`on_dynamic_scheme_contrast(` _*args_ `)` _→_ None 

Fired when the _`dynamic_scheme_contrast`_ value changes. 

`on_path_to_wallpaper(` _*args_ `)` _→_ None 

Fired when the _`path_to_wallpaper`_ value changes. 

`switch_theme()` _→_ None 

Switches the theme from light to dark. 

`switch_theme_system(` _is_dark_mode: bool_ `)` _→_ None 

Updates the application theme style according to the system theme. 

###### **Parameters** 

`is_dark_mode` – `True` if the system is using dark mode, otherwise `False` for light mode. 

`sync_theme_styles(` _*args_ `)` _→_ None 

`color_to_rgba(` _color_ `)` 

`class kivymd.theming.ThemableBehavior(` _**kwargs_ `)` 

**2.2. Themes** 

**21** 

**KivyMD, Release 2.0.1.dev0** 

###### `theme_cls` 

Instance of _`ThemeManager`_ class. 

_`theme_cls`_ is an `ObjectProperty` . 

###### `device_ios` 

`True` if device is `iOS` . 

_`device_ios`_ is an `BooleanProperty` . 

###### `theme_line_color` 

Line color scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_line_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_bg_color` 

Background color scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_bg_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_shadow_color` 

Elevation color scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_shadow_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_shadow_offset` 

Elevation offset scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_shadow_offset`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_elevation_level` 

Elevation level scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_elevation_level`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_font_size` 

Font size scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_font_size`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

**Chapter 2. Contents** 

**22** 

**KivyMD, Release 2.0.1.dev0** 

###### `theme_width` 

Widget width scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_width`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_height` 

Widget width scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_height`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_line_height` 

Line height scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_line_height`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_font_name` 

Font name scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_font_name`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_shadow_softness` 

Elevation softness scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_shadow_softness`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_focus_color` 

Focus color scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_focus_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

###### `theme_divider_color` 

Divider color scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_divider_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

**2.2. Themes** 

**23** 

**KivyMD, Release 2.0.1.dev0** 

```
theme_text_color
```

Label color scheme name. 

Available options are: _‘Primary’_ , _‘Secondary’_ , _‘Hint’_ , _‘Error’_ , _‘Custom’_ . 

_`theme_text_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

```
theme_icon_color
```

Label color scheme name. 

Available options are: _‘Primary’_ , _‘Secondary’_ , _‘Hint’_ , _‘Error’_ , _‘Custom’_ . 

_`theme_icon_color`_ is an `OptionProperty` and defaults to _‘Primary’_ . 

`remove_widget(` _widget_ `)` _→_ None 

###### **2.2.2 Material App** 

This module contains _`MDApp`_ class that is inherited from `App` . _`MDApp`_ has some properties needed for _KivyMD_ library (like _`theme_cls`_ ). You can turn on the monitor displaying the current _FP_ value in your application: 

Imperative python style with KV 

```
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLabel:
text:"Hello,World!"
halign:"center"
'''
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
classMainApp(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
self.fps_monitor_start()
MainApp().run()
```

Declarative python style 

```
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
```

(continues on next page) 

**Chapter 2. Contents** 

**24** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `class MainApp(MDApp): def build(self): return ( MDScreen( MDLabel( text="Hello, World!", halign="center", ), md_bg_color=self.theme_cls.backgroundColor, ) ) def on_start(self): self.fps_monitor_start() MainApp().run()` 

**2.2. Themes** 

**25** 



<!-- Start of picture text -->
FPS: 76.115339<br>Hello, World!<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

**Warning:** The _`theme_cls`_ attribute is already available in a class that is inherited from the _`MDApp`_ class. The following code will result in an error! 

```
classMainApp(MDApp):
theme_cls=ThemeManager()
theme_cls.primary_palette="Teal"
```

**Note:** Correctly do as shown below! 

```
classMainApp(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Teal"
```

_`theme_cls`_ is an `ObjectProperty` . 

###### `load_all_kv_files(` _path_to_directory: str_ `)` _→_ None 

Recursively loads KV files from the selected directory. 

Added in version 1.0.0. 

###### **2.2.3 Icon Definitions** 



List of icons from materialdesignicons.com. These expanded material design icons are maintained by Austin Andrews (Templarian on Github). 

Version 7.4.47 

**2.2. Themes** 

**27** 

**KivyMD, Release 2.0.1.dev0** 

###### **To preview the icons and their names, you can use the following application:** 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
fromkivymd.uix.listimportMDListItem
Builder.load_string(
'''
#:importimages_pathkivymd.images_path
<IconItem>
MDListItemLeadingIcon:
icon:root.icon
MDListItemSupportingText:
text:root.text
<PreviousMDIcons>
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
orientation:'vertical'
spacing:dp(10)
padding:dp(20)
MDBoxLayout:
adaptive_height:True
MDIconButton:
icon:'magnify'
pos_hint:{'center_y':.5}
MDTextField:
id:search_field
hint_text:'Searchicon'
on_text:root.set_list_md_icons(self.text,True)
RecycleView:
id:rv
key_viewclass:'viewclass'
key_size:'height'
RecycleBoxLayout:
padding:dp(10),dp(10),0,dp(10)
```

(continues on next page) 

**Chapter 2. Contents** 

**28** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
default_size:None,dp(48)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
orientation:'vertical'
'''
)
classIconItem(MDListItem):
icon=StringProperty()
text=StringProperty()
classPreviousMDIcons(MDScreen):
defset_list_md_icons(self,text="",search=False):
'''BuildsalistoficonsforthescreenMDIcons.'''
defadd_icon_item(name_icon):
self.ids.rv.data.append(
{
"viewclass":"IconItem",
"icon":name_icon,
"text":name_icon,
"callback":lambdax:x,
}
)
self.ids.rv.data=[]
forname_iconinmd_icons.keys():
ifsearch:
iftextinname_icon:
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
classMainApp(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=PreviousMDIcons()
defbuild(self):
returnself.screen
defon_start(self):
self.screen.set_list_md_icons()
MainApp().run()
```

Declarative python style 

**2.2. Themes** 

**29** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.propertiesimportStringProperty
fromkivy.langimportBuilder
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.material_resourcesimportdp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
fromkivymd.uix.listimportMDListItem
fromkivymd.uix.textfieldimportMDTextField,MDTextFieldHintText
Builder.load_string('''
<IconItem>
MDListItemLeadingIcon:
icon:root.icon
MDListItemSupportingText:
text:root.text
''')
classIconItem(MDListItem):
icon=StringProperty()
text=StringProperty()
classPreviousMDIcons(MDScreen):
defset_list_md_icons(self,text="",search=False):
'''BuildsalistoficonsforthescreenMDIcons.'''
defadd_icon_item(name_icon):
self.get_ids().rv.data.append(
{
"viewclass":"IconItem",
"icon":name_icon,
"text":name_icon,
"callback":lambdax:x,
}
)
self.get_ids().rv.data=[]
forname_iconinmd_icons.keys():
ifsearch:
iftextinname_icon:
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
```

(continues on next page) 

**Chapter 2. Contents** 

**30** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classMainApp(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=PreviousMDIcons(
MDBoxLayout(
MDBoxLayout(
MDIconButton(
icon='magnify',
pos_hint={'center_y':0.5},
),
MDTextField(
MDTextFieldHintText(
text='Searchicon',
),
id="search_field",
),
adaptive_height=True,
),
MDRecycleView(
MDRecycleBoxLayout(
padding=(dp(10),dp(10),0,dp(10)),
default_size=(None,dp(48)),
default_size_hint=(1,None),
size_hint_y=None,
adaptive_height=True,
orientation='vertical',
),
id="rv",
),
orientation='vertical',
spacing=dp(10),
padding=dp(20),
),
md_bg_color=self.theme_cls.backgroundColor,
)
defbuild(self):
rv=self.screen.get_ids().rv
rv.key_viewclass='viewclass'
rv.key_size='height'
search_field=self.screen.get_ids().search_field
search_field.bind(
text=lambdainstance,value:self.screen.set_list_md_icons(
value,True
)
)
returnself.screen
defon_start(self):
self.screen.set_list_md_icons()
```

(continues on next page) 

**2.2. Themes** 

**31** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MainApp().run()
```

###### **API -** `kivymd.icon_definitions` 

```
kivymd.icon_definitions.md_icons
```

`class kivymd.icon_definitions.IconItem(` _*args_ , _**kwargs_ `)` 

Implements a list item. 

For more information, see in the `BaseListItem` and `BoxLayout` classes documentation. `icon text` 

###### **2.2.4 Font definitions** 

###### **See also:** 

Material Design spec, The type system 

###### **Example** 

###### Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.font_definitionsimporttheme_font_styles
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDRecycleView:
id:rv
key_viewclass:'viewclass'
key_size:'height'
RecycleBoxLayout:
padding:dp(10)
spacing:dp(10)
default_size:None,dp(48)
default_size_hint:1,None
size_hint_y:None
```

(continues on next page) 

**Chapter 2. Contents** 

**32** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
height:self.minimum_height
orientation:"vertical"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_start(self):
forstyleintheme_font_styles:
ifstyle!="Icon":
forroleintheme_font_styles[style]:
font_size=int(theme_font_styles[style][role]["font-size"])
self.root.ids.rv.data.append(
{
"viewclass":"MDLabel",
"text":f"{style}{role}{font_size}sp",
"adaptive_height":"True",
"font_style":style,
"role":role,
}
)
Example().run()
```

Declarative python style 

```
fromkivymd.material_resourcesimportdp
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
fromkivymd.font_definitionsimporttheme_font_styles
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.screen=(
MDScreen(
MDRecycleView(
MDRecycleBoxLayout(
padding=(dp(10),dp(10),0,dp(10)),
default_size=(None,dp(48)),
default_size_hint=(1,None),
size_hint_y=None,
adaptive_height=True,
orientation='vertical',
),
```

(continues on next page) 

**2.2. Themes** 

**33** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
id="rv",
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
rv=self.screen.get_ids().rv
rv.key_viewclass='viewclass'
rv.key_size='height'
returnself.screen
defon_start(self):
forstyleintheme_font_styles:
ifstyle!="Icon":
forroleintheme_font_styles[style]:
font_size=int(theme_font_styles[style][role]["font-size"])
self.screen.get_ids().rv.data.append(
{
"viewclass":"MDLabel",
"text":f"{style}{role}{font_size}sp",
"adaptive_height":"True",
"font_style":style,
"role":role,
}
)
Example().run()
```

**Chapter 2. Contents** 

**34** 

Display large 57 sp Display medium 45 sp Display small 36 sp Headline large 32 sp 

Headline medium 28 sp Headline small 24 sp 

Title large 22 sp Title medium 16 sp Title small 14 sp Body large 16 sp Body medium 14 sp 

Display large 57 sp Display medium 45 sp Display small 36 sp Headline large 32 sp Headline medium 28 sp Headline small 24 sp Title large 22 sp Title medium 16 sp Title small 14 sp Body large 16 sp Body medium 14 sp 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3 Components** 

###### **2.3.1 Animation** 

Added in version 2.0.0. 

Adds new transitions to the `AnimationTransition` class: 

- “easing_standard” 

- “easing_decelerated” 

- “easing_accelerated” 

- “easing_linear” 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivy.animationimportAnimation
fromkivy.uix.boxlayoutimportBoxLayout
fromkivy.clockimportClock
fromkivy.metricsimportdp
fromkivy.propertiesimportListProperty
fromkivymd.appimportMDApp
classAnimBox(BoxLayout):
obj_pos=ListProperty([0,0])
UI='''
<AnimBox>:
transition:"in_out_bounce"
size_hint_y:None
height:dp(100)
obj_pos:[dp(40),self.pos[-1]+dp(40)]
canvas:
Color:
rgba:app.theme_cls.primaryContainerColor
Rectangle:
size:[self.size[0],dp(5)]
pos:self.pos[0],self.pos[-1]+dp(50)
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
size:[dp(30)]*2
pos:root.obj_pos
MDLabel:
adaptive_height:True
```

(continues on next page) 

**2.3. Components** 

**37** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text:root.transition
padding:[dp(10),0]
halign:"center"
MDGridLayout:
orientation:"lr-tb"
cols:1
md_bg_color:app.theme_cls.backgroundColor
spacing:dp(10)
'''
classMotionApp(MDApp):
defbuild(self):
returnBuilder.load_string(UI)
defon_start(self):
fortransitionin[
"easing_linear",
"easing_accelerated",
"easing_decelerated",
"easing_standard",
"in_out_cubic"
]:#addmorehereforcomparison
print(transition)
widget=AnimBox()
widget.transition=transition
self.root.add_widget(widget)
Clock.schedule_once(self.run_animation,1)
_inverse=True
defrun_animation(self,dt):
x=(self.root.children[0].width-dp(30))ifself._inverseelse0
forwidgetinself.root.children:
Animation(
obj_pos=[x,widget.obj_pos[-1]],t=widget.transition,d=3
).start(widget)
self._inverse=notself._inverse
Clock.schedule_once(self.run_animation,3.1)
MotionApp().run()
```

###### Declarative python style 

```
fromkivy.core.windowimportWindow
fromkivy.graphicsimportColor,Rectangle
fromkivy.animationimportAnimation
fromkivy.clockimportClock
```

(continues on next page) 

**Chapter 2. Contents** 

**38** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivy.metricsimportdp
fromkivy.propertiesimportListProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.gridlayoutimportMDGridLayout
fromkivymd.uix.labelimportMDLabel
```

```
classAnimBox(MDBoxLayout):
obj_pos=ListProperty([0,0])
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.transition="in_out_bounce"
self.size_hint_y=None
self.height=dp(100)
self.label=MDLabel(
adaptive_height=True,
text=self.transition,
padding=[dp(10),0],
halign="center",
)
self.add_widget(self.label)
withself.canvas:
Color(rgba=self.theme_cls.primaryContainerColor)
self.background_rect=Rectangle(
size=(self.width,dp(5)),
pos=(self.x,self.y+dp(50)),
)
Color(rgba=self.theme_cls.primaryColor)
self.obj_rect=Rectangle(
size=(dp(30),dp(30)),
pos=(dp(40),self.y+dp(40)),
)
self.bind(
pos=self.update_position,
size=self.update_canvas,
y=self.update_canvas,
obj_pos=self.update_obj_rect,
)
Clock.schedule_once(self.set_initial_pos)
defset_initial_pos(self,dt):
self.obj_pos=[
dp(40),
```

(continues on next page) 

**2.3. Components** 

**39** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.y+dp(40),
]
defupdate_position(self,*args):
self.obj_pos=[
self.obj_pos[0],
self.y+dp(40),
]
defupdate_canvas(self,*args):
self.background_rect.size=(
self.width,
dp(5),
)
self.background_rect.pos=(
self.x,
self.center_y,
)
defupdate_obj_rect(self,*args):
self.obj_rect.pos=self.obj_pos
classMotionApp(MDApp):
defbuild(self):
layout=MDGridLayout(
orientation="lr-tb",
cols=1,
md_bg_color=self.theme_cls.backgroundColor,
spacing=dp(10),
)
Window.bind(size=layout.do_layout)
returnlayout
defon_start(self):
fortransitionin[
"easing_linear",
"easing_accelerated",
"easing_decelerated",
"easing_standard",
"in_out_cubic",
]:
widget=AnimBox()
widget.transition=transition
widget.label.text=transition
self.root.add_widget(widget)
Clock.schedule_once(self.run_animation,1)
_inverse=True
```

(continues on next page) 

**Chapter 2. Contents** 

**40** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defrun_animation(self,dt):
forwidgetinself.root.children:
x=widget.width-dp(30)ifself._inverseelse0
Animation(
obj_pos=[
x,
widget.y+dp(40),
],
t=widget.transition,
d=3,
).start(widget)
self._inverse=notself._inverse
Clock.schedule_once(self.run_animation,3.1)
MotionApp().run()
```

**API -** `kivymd.animation` 

```
classkivymd.animation.MDAnimationTransition
```

KivyMD’s equivalent of kivy’s _AnimationTransition_ . 

```
easing_standard
```

Material Design standard easing transition. 

_`easing_standard`_ is a `Callable` and defaults to `CubicBezier(0.4, 0.0, 0.2, 1.0).t` . `easing_decelerated` 

Material Design standard easing transition. 

_`easing_decelerated`_ is a `Callable` and defaults to `CubicBezier(0.0, 0.0, 0.2, 1.0).t` . 

###### `easing_accelerated` 

Material Design standard easing transition. 

_`easing_accelerated`_ is a `Callable` and defaults to `CubicBezier(0.4, 0.0, 1.0, 1.0).t` . 

###### `easing_linear` 

Material Design standard easing transition. 

_`easing_linear`_ is a `Callable` and defaults to `CubicBezier(0.0, 0.0, 1.0, 1.0).t` . 

###### `easing_emphasized()` 

Material Design emphasized easing transition. 

###### **Parameters** 

`t` – Animation progress in the range `0` to `1` . 

###### **Returns** 

Interpolated animation progress. 

**2.3. Components** 

**41** 



<!-- Start of picture text -->
Yellow custom input Yellow On Yellow Yellow Container On Yellow Container<br>5<br>Yellow40 Yellow100 Yellow90 Yellow10<br>Orange custom input Orange On Orange Orange Container On Orange Container<br>eo<br>Orange40 Orange100 Orange90 Orange10<br>Green custom input Green On Green Green Container On Green Container<br>eo<br>Green40 Green100 Green90 Green10<br><!-- End of picture text -->



<!-- Start of picture text -->
| ,. e880Ge t J<br>"hay rN<br>tr<br>SONG HISTORIES PODCAST<br>1 rue<br>tae e8 cg<br>mY<br>| ; 1fetuswr | 5 a8an<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

3. Colors extracted from content 

###### **Example of dynamic color from the list of standard color schemes** 

```
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty,ColorProperty
fromkivy.uix.boxlayoutimportBoxLayout
fromkivy.utilsimporthex_colormap
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.appimportMDApp
KV='''
<ColorCard>
orientation:"vertical"
MDLabel:
text:root.text
color:"grey"
adaptive_height:True
MDCard:
theme_bg_color:"Custom"
md_bg_color:root.bg_color
MDScreen:
md_bg_color:app.theme_cls.backgroundColor
MDIconButton:
on_release:app.open_menu(self)
pos_hint:{"top":.98}
x:"12dp"
icon:"menu"
MDRecycleView:
id:card_list
viewclass:"ColorCard"
bar_width:0
size_hint_y:None
-
height:root.heightdp(68)
RecycleGridLayout:
cols:3
spacing:"16dp"
padding:"16dp"
default_size:None,dp(56)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
```

(continues on next page) 

**2.3. Components** 

**43** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
'''
```

```
classColorCard(BoxLayout):
text=StringProperty()
bg_color=ColorProperty()
```

```
classExample(MDApp):
menu:MDDropdownMenu=None
defbuild(self):
self.theme_cls.dynamic_color=True
returnBuilder.load_string(KV)
defget_instance_from_menu(self,name_item):
index=0
rv=self.menu.ids.md_menu
opts=rv.layout_manager.view_opts
datas=rv.data[0]
fordatainrv.data:
ifdata["text"]==name_item:
index=rv.data.index(data)
break
instance=rv.view_adapter.get_view(
index,datas,opts[index]["viewclass"]
)
returninstance
defopen_menu(self,menu_button):
menu_items=[]
foritem,methodin{
"Setpalette":lambda:self.set_palette(),
"Switchthemestyle":lambda:self.theme_switch(),
}.items():
menu_items.append({"text":item,"on_release":method})
self.menu=MDDropdownMenu(
caller=menu_button,
items=menu_items,
)
self.menu.open()
defset_palette(self):
instance_from_menu=self.get_instance_from_menu("Setpalette")
available_palettes=[
name_color.capitalize()forname_colorinhex_colormap.keys()
]
menu_items=[]
```

(continues on next page) 

**Chapter 2. Contents** 

**44** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
forname_paletteinavailable_palettes:
menu_items.append(
{
"text":name_palette,
"on_release":lambdax=name_palette:self.switch_palette(x),
}
)
MDDropdownMenu(
caller=instance_from_menu,
items=menu_items,
).open()
defswitch_palette(self,selected_palette):
self.theme_cls.primary_palette=selected_palette
Clock.schedule_once(self.generate_cards,0.5)
deftheme_switch(self)->None:
self.theme_cls.switch_theme()
Clock.schedule_once(self.generate_cards,0.5)
defgenerate_cards(self,*args):
self.root.ids.card_list.data=[]
forcolorinself.theme_cls.dynamic_color_names:
self.root.ids.card_list.data.append(
{
"bg_color":getattr(self.theme_cls,color),
"text":color,
}
)
defon_start(self):
Clock.schedule_once(self.generate_cards)
Example().run()
```

###### **Example of a dynamic color from an image** 

###### **See also:** 

```
kivymd.theming.ThemeManager.path_to_wallpaper
```

```
importos
fromkivy.clockimportClock
fromkivy.core.windowimportWindow
fromkivy.core.window.window_sdl2importWindowSDL
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty,ColorProperty
```

(continues on next page) 

**2.3. Components** 

**45** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.appimportMDApp
KV='''
<ColorCard>
orientation:"vertical"
MDLabel:
text:root.text
color:"grey"
adaptive_height:True
MDCard:
theme_bg_color:"Custom"
md_bg_color:root.bg_color
MDScreen:
md_bg_color:app.theme_cls.backgroundColor
MDRecycleView:
id:card_list
viewclass:"ColorCard"
bar_width:0
RecycleGridLayout:
cols:3
spacing:"16dp"
padding:"16dp"
default_size:None,dp(56)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
'''
classColorCard(MDBoxLayout):
text=StringProperty()
bg_color=ColorProperty()
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
Window.bind(on_dropfile=self.on_drop_file)
defon_drop_file(self,sdl:WindowSDL,path_to_file:str)->None:
ext=os.path.splitext(path_to_file)[1]
ifisinstance(path_to_file,bytes):
path_to_file=path_to_file.decode()
ifisinstance(ext,bytes):
```

(continues on next page) 

**Chapter 2. Contents** 

**46** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
ext=ext.decode()
ifextin[".png",".jpg"]:
self.theme_cls.path_to_wallpaper=path_to_file
Clock.schedule_once(self.generate_cards,0.5)
defbuild(self):
self.theme_cls.dynamic_color=True
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
deftheme_switch(self)->None:
self.theme_cls.switch_theme()
Clock.schedule_once(self.generate_cards,0.5)
defgenerate_cards(self,*args):
self.root.ids.card_list.data=[]
forcolorinself.theme_cls.dynamic_color_names:
self.root.ids.card_list.data.append(
{
"bg_color":getattr(self.theme_cls,color),
"text":color,
}
)
defon_start(self):
Clock.schedule_once(self.generate_cards)
Example().run()
```

**API -** `kivymd.dynamic_color` 

```
classkivymd.dynamic_color.DynamicColor
```

Dynamic color class. Added in version 2.0.0. 

```
current_schemes_color_data
```

```
primaryColor
```

Primary color. 

_`primaryColor`_ is an `ColorProperty` and defaults to _None_ . 

```
primaryDimColor
```

Primary dim color. 

_`primaryDimColor`_ is an `ColorProperty` and defaults to _None_ . 

```
primaryContainerColor
```

Primary container color. 

_`primaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

**2.3. Components** 

**47** 

**KivyMD, Release 2.0.1.dev0** 

###### `onPrimaryColor` 

On primary color. 

_`onPrimaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onPrimaryContainerColor` 

On primary container color. 

_`onPrimaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `primaryFixedColor` 

Primary fixed color. 

_`primaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `primaryFixedDimColor` 

Primary fixed dim color. 

_`primaryFixedDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onPrimaryFixedColor` 

On primary fixed color. 

_`onPrimaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onPrimaryFixedVariantColor` 

On primary fixed variant color. 

_`onPrimaryFixedVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `secondaryColor` 

Secondary color. 

_`secondaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `secondaryDimColor` 

Secondary dim color. 

_`secondaryDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `secondaryContainerColor` 

Secondary container color. 

_`secondaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSecondaryColor` 

On secondary color. 

_`onSecondaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSecondaryContainerColor` 

On secondary container color. 

_`onSecondaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `secondaryFixedColor` 

Secondary fixed color. 

_`secondaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

**Chapter 2. Contents** 

**48** 

**KivyMD, Release 2.0.1.dev0** 

###### `secondaryFixedDimColor` 

Secondary fixed dim color. 

_`secondaryFixedDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSecondaryFixedColor` 

On secondary fixed color. 

_`onSecondaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSecondaryFixedVariantColor` 

On secondary fixed variant color. 

_`onSecondaryFixedVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryColor` 

Tertiary color. 

_`tertiaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryDimColor` 

Tertiary dim color. 

_`tertiaryDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryContainerColor` 

Tertiary container color. 

_`tertiaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onTertiaryColor` 

On tertiary color. 

_`onTertiaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onTertiaryContainerColor` 

On tertiary container color. 

_`onTertiaryContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryFixedColor` 

Tertiary fixed color. 

_`tertiaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryFixedDimColor` 

Tertiary fixed dim color. 

_`tertiaryFixedDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onTertiaryFixedColor` 

On tertiary fixed color. 

_`onTertiaryFixedColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onTertiaryFixedVariantColor` 

On tertiary fixed variant color. 

_`onTertiaryFixedVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

**2.3. Components** 

**49** 

**KivyMD, Release 2.0.1.dev0** 

###### `surfaceColor` 

Surface color. 

_`surfaceColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceDimColor` 

Surface dim color. 

_`surfaceDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceBrightColor` 

Surface bright color. 

_`surfaceBrightColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceContainerLowestColor` 

Surface container lowest color. 

_`surfaceContainerLowestColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceContainerLowColor` 

Surface container low color. 

_`surfaceContainerLowColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceContainerColor` 

Surface container color. 

_`surfaceContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceContainerHighColor` 

Surface container high color. 

_`surfaceContainerHighColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceContainerHighestColor` 

Surface container highest color. 

_`surfaceContainerHighestColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceVariantColor` 

Surface variant color. 

_`surfaceVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `surfaceTintColor` 

Surface tint color. 

_`surfaceTintColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSurfaceColor` 

On surface color. 

_`onSurfaceColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onSurfaceLightColor` 

On surface light color. 

_`onSurfaceLightColor`_ is an `ColorProperty` and defaults to _None_ . 

**Chapter 2. Contents** 

**50** 

**KivyMD, Release 2.0.1.dev0** 

###### `onSurfaceVariantColor` 

On surface variant color. 

_`onSurfaceVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `inverseSurfaceColor` 

Inverse surface color. 

_`inverseSurfaceColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `inverseOnSurfaceColor` 

Inverse on surface color. 

_`inverseOnSurfaceColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `inversePrimaryColor` 

Inverse primary color. 

_`inversePrimaryColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `backgroundColor` 

Background color. 

_`backgroundColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onBackgroundColor` 

On background color. 

_`onBackgroundColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `errorColor` 

Error color. 

_`errorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `errorDimColor` 

Error dim color. 

_`errorDimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `errorContainerColor` 

Error container color. 

_`errorContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onErrorColor` 

On error color. 

_`onErrorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `onErrorContainerColor` 

On error container color. 

_`onErrorContainerColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `outlineColor` 

Outline color. 

_`outlineColor`_ is an `ColorProperty` and defaults to _None_ . 

**2.3. Components** 

**51** 

**KivyMD, Release 2.0.1.dev0** 

###### `outlineVariantColor` 

Outline variant color. 

_`outlineVariantColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `shadowColor` 

Shadow color. 

_`shadowColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `scrimColor` 

Scrim color. 

_`scrimColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `primaryPaletteKeyColorColor` 

Primary palette key color. 

_`primaryPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `secondaryPaletteKeyColorColor` 

Secondary palette key color. 

_`secondaryPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `tertiaryPaletteKeyColorColor` 

Tertiary palette key color. 

_`tertiaryPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `neutralPaletteKeyColorColor` 

Neutral palette key color. 

_`neutralPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `neutralVariantPaletteKeyColorColor` 

Neutral variant palette key color. 

_`neutralVariantPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `errorPaletteKeyColorColor` 

Error palette key color. 

_`errorPaletteKeyColorColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `disabledTextColor` 

Disabled text color. 

_`disabledTextColor`_ is an `ColorProperty` and defaults to _None_ . 

###### `transparentColor` 

Transparent color. 

_`transparentColor`_ is an `ColorProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `rippleColor` 

Ripple color. 

_`rippleColor`_ is an `ColorProperty` and defaults to _‘#BDBDBD’_ . 

**Chapter 2. Contents** 

**52** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3.3 ScreenManager** 

Added in version 1.0.0. 

`ScreenManager` class equivalent. If you want to use Hero animations you need to use _`MDScreenManager`_ not `ScreenManager` class. 

###### **Transition** 

_`MDScreenManager`_ class supports the following transitions: 

- `MDFadeSlideTransition` 

- `MDSlideTransition` 

- `MDSwapTransition` 

You need to use the _`MDScreenManager`_ class when you want to use hero animations on your screens. If you don’t need hero animation use the `ScreenManager` class. 

`ScreenManager` class equivalent. Simplifies working with some widget properties. For example: 

###### **ScreenManager** 

KV 

```
ScreenManager:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.screenmanagerimportScreenManager
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=ScreenManager()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

**2.3. Components** 

**53** 

**KivyMD, Release 2.0.1.dev0** 

###### **MDScreenManager** 

Imperative python style with KV 

```
MDScreenManager:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.sreenmanagerimportMDScreenManager
fromkivymd.appimportMDApp
```

```
classMyApp(App):
defbuild(self):
returnMDScreenManager(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent `size_hint_x: None height: self.minimum_width` 

**Chapter 2. Contents** 

**54** 

**KivyMD, Release 2.0.1.dev0** 

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

###### **API -** `kivymd.uix.screenmanager` 

`class kivymd.uix.screenmanager.MDScreenManager(` _*args_ , _**kwargs_ `)` 

Screen manager. This is the main class that will control your _`MDScreen`_ stack and memory. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `ScreenManager` and _`MDAdaptiveWidget`_ classes documentation. 

###### `current_hero` 

The name of the current tag for the _`MDHeroFrom`_ and _`MDHeroTo`_ objects that will be animated when animating the transition between screens. 

Deprecated since version 1.1.0: Use _`current_heroes`_ attribute instead. 

See the Hero module documentation for more information about creating and using Hero animations. 

_`current_hero`_ is an `StringProperty` and defaults to _None_ . 

###### `current_heroes` 

A list of names (tags) of heroes that need to be animated when moving to the next screen. 

Added in version 1.1.0. 

_`current_heroes`_ is an `ListProperty` and defaults to _[]_ . 

- `check_transition(` _*args_ `)` _→_ None 

Sets the default type transition. 

- `get_hero_from_widget()` _→_ list 

Get a list of _`MDHeroFrom`_ objects according to the tag names specified in the _`current_heroes`_ list. 

- `on_current_hero(` _instance_ , _value: str_ `)` _→_ None 

Fired when the value of the _`current_hero`_ attribute changes. 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Changed in version 2.1.0: Renamed argument _screen_ to _widget_ . 

###### **2.3.4 StackLayout** 

`StackLayout` class equivalent. Simplifies working with some widget properties. For example: 

**2.3. Components** 

**55** 

**KivyMD, Release 2.0.1.dev0** 

###### **StackLayout** 

KV 

```
StackLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.stacklayoutimportStackLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=StackLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDStackLayout** 

Imperative python style with KV 

```
MDStackLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.stacklayoutimportMDStackLayout
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDStackLayout(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

**Chapter 2. Contents** 

**56** 

**KivyMD, Release 2.0.1.dev0** 

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

###### **API -** `kivymd.uix.stacklayout` 

`class kivymd.uix.stacklayout.MDStackLayout(` _*args_ , _**kwargs_ `)` 

Stack layout class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `StackLayout` and _`MDAdaptiveWidget`_ classes documentation. 

**2.3. Components** 

**57** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3.5 RelativeLayout** 

`RelativeLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **RelativeLayout** 

KV 

```
RelativeLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.relativelayoutimportRelativeLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=RelativeLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDRelativeLayout** 

Imperative python style with KV 

```
MDRelativeLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.relativelayoutimportMDRelativeLayout
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDRelativeLayout(
```

(continues on next page) 

**Chapter 2. Contents** 

**58** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
height:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**2.3. Components** 

**59** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.relativelayout` 

`class kivymd.uix.relativelayout.MDRelativeLayout(` _*args_ , _**kwargs_ `)` 

Relative layout class. 

For more information see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `RelativeLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.6 MDRecycleBoxLayout** 

`MDRecycleBoxLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **RecycleBoxLayout** 

KV 

```
RecycleBoxLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.recycleboxlayoutimportRecycleBoxLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=RecycleBoxLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

**Chapter 2. Contents** 

**60** 

**KivyMD, Release 2.0.1.dev0** 

###### **MDRecycleBoxLayout** 

Imperative python style with KV 

```
MDRecycleBoxLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.appimportMDApp
```

```
classMyApp(App):
defbuild(self):
returnMDRecycleBoxLayout(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

**2.3. Components** 

**61** 

**KivyMD, Release 2.0.1.dev0** 

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**API -** `kivymd.uix.recycleboxlayout` 

`class kivymd.uix.recycleboxlayout.MDRecycleBoxLayout(` _*args_ , _**kwargs_ `)` 

Recycle box layout class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `RecycleBoxLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.7 ScrollView** 

Added in version 1.0.0. 

`ScrollView` class equivalent. It implements Material Design’s overscorll effect and simplifies working with some widget properties. For example: 

###### **ScrollView** 

KV 

```
ScrollView:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.scrollviewimportScrollView
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
```

```
classMyApp(App):
defbuild(self):
layout=ScrollView()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
```

(continues on next page) 

**Chapter 2. Contents** 

**62** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
returnlayout
MyApp().run()
```

###### **MDScrollView** 

Imperative python style with KV 

```
MDScrollView:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.scrollviewimportMDScrollView
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDScrollView(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **The stretching effect** 

Declarative Python style with KV 

```
importos
importsys
fromkivy.core.windowimportWindow
fromkivyimport__version__askv__version__
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymdimport__version__
fromkivymd.uix.listimport(
MDListItem,
MDListItemHeadlineText,
MDListItemSupportingText,
MDListItemLeadingIcon,
)
frommaterialyoucolorimport__version__asmc__version__
```

```
MAIN_KV='''
```

(continues on next page) 

**2.3. Components** 

**63** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`MDScreen: md_bg_color: app.theme_cls.backgroundColor MDScrollView: do_scroll_x: False MDBoxLayout: id: main_scroll orientation: "vertical" adaptive_height: True MDBoxLayout: adaptive_height: True MDLabel: theme_font_size: "Custom" text: "OS Info" font_size: "55sp" adaptive_height: True padding: "10dp", "20dp", 0, 0 MDIconButton: icon: "menu" pos_hint: {"center_y": .5} ''' class Example(MDApp): def build(self): self.theme_cls.theme_style = "Dark" return Builder.load_string(MAIN_KV) def on_start(self): info = { "Name": [ os.name, ( "microsoft" if os.name == "nt" else ("linux" if os.uname()[0] != "Darwin" else "apple") ), ], "Architecture": [os.uname().machine, "memory"], "Hostname": [os.uname().nodename, "account"], "Python Version": ["v" + sys.version, "language-python"], "Kivy Version": ["v" + kv__version__, "alpha-k-circle-outline"], "KivyMD Version": ["v" + __version__, "material-design"], "MaterialYouColor Version": ["v" + mc__version__, "invert-colors"], "Pillow Version": ["Unknown", "image"], "Working Directory": [os.getcwd(), "folder"], "Home Directory": [os.path.expanduser("~"), "folder-account"], "Environment Variables": [os.environ, "code-json"],` (continues on next page) 

**Chapter 2. Contents** 

**64** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
}
try:
fromPILimport__version__aspil__version_
info["PillowVersion"]=["v"+pil__version_,"image"]
exceptException:
pass
forinfo_itemininfo:
self.root.ids.main_scroll.add_widget(
MDListItem(
MDListItemLeadingIcon(
icon=info[info_item][1],
),
MDListItemHeadlineText(
text=info_item,
),
MDListItemSupportingText(
text=str(info[info_item][0]),
),
pos_hint={"center_x":.5,"center_y":.5},
)
)
Window.size=[dp(350),dp(600)]
Example().run()
```

Declarative python style 

```
importos
importsys
fromkivy.core.windowimportWindow
fromkivyimport__version__askv__version__
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymdimport__version__
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.listimport(
MDListItem,
MDListItemHeadlineText,
MDListItemSupportingText,
MDListItemLeadingIcon,
)
frommaterialyoucolorimport__version__asmc__version__
```

(continues on next page) 

**2.3. Components** 

**65** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.scrollviewimportMDScrollView
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDScrollView(
MDBoxLayout(
MDBoxLayout(
MDLabel(
theme_font_size="Custom",
text="OSInfo",
font_size="55sp",
adaptive_height=True,
padding=("10dp","20dp",0,0),
),
MDIconButton(
icon="menu",
pos_hint={"center_y":.5},
),
adaptive_height=True
),
id="main_scroll",
orientation="vertical",
adaptive_height=True,
),
do_scroll_x=False
),
md_bg_color=self.theme_cls.backgroundColor
)
)
```

```
defon_start(self):
info={
"Name":[
os.name,
(
"microsoft"
ifos.name=="nt"
else("linux"ifos.uname()[0]!="Darwin"else"apple")
),
],
"Architecture":[os.uname().machine,"memory"],
"Hostname":[os.uname().nodename,"account"],
"PythonVersion":["v"+sys.version,"language-python"],
"KivyVersion":["v"+kv__version__,"alpha-k-circle-outline"],
"KivyMDVersion":["v"+__version__,"material-design"],
"MaterialYouColorVersion":["v"+mc__version__,"invert-colors"],
```

(continues on next page) 

**Chapter 2. Contents** 

**66** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
"PillowVersion":["Unknown","image"],
"WorkingDirectory":[os.getcwd(),"folder"],
"HomeDirectory":[os.path.expanduser("~"),"folder-account"],
"EnvironmentVariables":[os.environ,"code-json"],
}
try:
fromPILimport__version__aspil__version_
info["PillowVersion"]=["v"+pil__version_,"image"]
exceptException:
pass
forinfo_itemininfo:
self.root.get_ids().main_scroll.add_widget(
MDListItem(
MDListItemLeadingIcon(
icon=info[info_item][1],
),
MDListItemHeadlineText(
text=info_item,
),
MDListItemSupportingText(
text=str(info[info_item][0]),
),
pos_hint={"center_x":.5,"center_y":.5},
)
)
Window.size=[dp(350),dp(600)]
Example().run()
```

**API -** `kivymd.uix.scrollview` 

`class kivymd.uix.scrollview.StretchOverScrollStencil(` _*arg_ , _**kwargs_ `)` 

Stretches the view on overscroll and absorbs velocity at start and end to convert to stretch. 

Added in version 2.0.0. 

**Note:** This effect only works with _`kivymd.uix.scrollview.MDScrollView`_ . 

If you need any documentation please look at `dampedscrolleffect` . `minimum_absorbed_velocity = 0` 

```
maximum_velocity=10000
```

**2.3. Components** 

**67** 

**KivyMD, Release 2.0.1.dev0** 

```
stretch_intensity=0.016
exponential_scalar
scroll_friction=0.015
approx_normailzer=200000.0
duration_normailzer=10
scroll_view
scroll_scale
scale_axis='y'
last_touch_pos
```

`clamp(` _value_ , _min_val=0_ , _max_val=0_ `)` 

```
is_top_or_bottom()
```

`on_value(` _stencil_ , _scroll_distance_ `)` 

```
get_hw()
```

`set_scale_origin() absorb_impact() get_component(` _pos_ `)` 

`can_stretch_touch(` _touch_ `)` 

`convert_overscroll(` _touch_ `)` 

`reset_scale(` _*arg_ `)` 

- `class kivymd.uix.scrollview.StretchOverScrollBehavior(` _*args_ , _**kwargs_ `)` 

Shared overscroll-stretch setup for ScrollView-based widgets. 

`on_touch_down(` _touch_ `)` 

`on_touch_move(` _touch_ `)` 

`on_touch_up(` _touch_ `)` 

`class kivymd.uix.scrollview.MDScrollView(` _*args_ , _**kwargs_ `)` 

An approximate implementation to Material Design’s overscorll effect. 

For more information, see in the _`DeclarativeBehavior`_ and _`BackgroundColorBehavior`_ and `ScrollView` classes documentation. 

**Chapter 2. Contents** 

**68** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3.8 FloatLayout** 

`FloatLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **FloatLayout** 

KV 

```
FloatLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.floatlayoutimportFloatLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=FloatLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDFloatLayout** 

Imperative python style with KV 

```
MDFloatLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDFloatLayout(
```

(continues on next page) 

**2.3. Components** 

**69** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color=self.theme_cls.primaryColor
)
```

```
MyApp().run()
```

**Warning:** For a `FloatLayout` , the `minimum_size` attributes are always 0, so you cannot use `adaptive_size` and related options. 

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent `size_hint_x: None width: self.minimum_width` 

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**Chapter 2. Contents** 

**70** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.floatlayout` 

`class kivymd.uix.floatlayout.MDFloatLayout(` _*args_ , _**kwargs_ `)` 

Float layout class. 

For more information see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `FloatLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.9 CircularLayout** 

CircularLayout is a special layout that places widgets around a circle. 

###### **MDCircularLayout** 

###### **Usage** 

Imperative python style with KV 

```
fromkivy.lang.builderimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDCircularLayout:
id:container
pos_hint:{"center_x":.5,"center_y":.5}
row_spacing:min(self.size)*0.1
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_start(self):
forxinrange(1,49):
self.root.ids.container.add_widget(
MDLabel(text=f"{x}",adaptive_size=True)
)
Example().run()
```

Declarative python style 

**2.3. Components** 

**71** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.circularlayoutimportMDCircularLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.screen=MDScreen(
MDCircularLayout(
id="container",
pos_hint={"center_x":0.5,"center_y":0.5},
),
md_bg_color=self.theme_cls.backgroundColor
)
returnself.screen
defon_start(self):
defon_start(*args):
container.row_spacing=min(container.size)*0.1
container=self.screen.get_ids().container
forxinrange(1,49):
self.screen.get_ids().container.add_widget(
MDLabel(text=f"{x}",adaptive_size=True)
)
Clock.schedule_once(on_start)
Example().run()
```

**Chapter 2. Contents** 

**72** 



<!-- Start of picture text -->
11 |<br>34 4]_ As 3/__ 26<br>9 21 33 AS 39 7 15 3<br>44 40<br>20 16<br>30<br>6<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `circular_padding` 

Padding between outer widgets and the edge of the biggest circle. 

_`circular_padding`_ is an `NumericProperty` and defaults to _25dp_ . 

###### `row_spacing` 

Space between each row of widget. 

_`row_spacing`_ is an `NumericProperty` and defaults to _50dp_ . 

###### `clockwise` 

Direction of widgets in circular direction. 

_`clockwise`_ is an `BooleanProperty` and defaults to _True_ . 

- `get_angle(` _pos: tuple_ `)` _→_ float 

Returns the angle of given pos. 

###### `remove_widget(` _widget_ , _**kwargs_ `)` 

Remove a widget from the children of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to remove from our children list. 

```
>>>fromkivy.uix.buttonimportButton
>>>root=Widget()
>>>button=Button()
>>>root.add_widget(button)
>>>root.remove_widget(button)
```

###### `do_layout(` _*largs_ , _**kwargs_ `)` 

This function is called when a layout is called by a trigger. If you are writing a new Layout subclass, don’t call this function directly but use `_trigger_layout()` instead. 

The function is by default called _before_ the next frame, therefore the layout isn’t updated immediately. Anything depending on the positions of e.g. children should be scheduled for the next frame. 

Added in version 1.0.8. 

###### **2.3.10 RecycleView** 

Added in version 1.0.0. 

`RecycleView` class equivalent. Simplifies working with some widget properties. For example: 

**Chapter 2. Contents** 

**74** 

**KivyMD, Release 2.0.1.dev0** 

###### **RecycleView** 

KV 

```
RecycleView:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.recycleviewimportRecycleView
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=RecycleView()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDRecycleView** 

Imperative python style with KV 

```
MDRecycleView:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDRecycleView(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

**2.3. Components** 

**75** 

**KivyMD, Release 2.0.1.dev0** 

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
height:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

###### **API -** `kivymd.uix.recycleview` 

`class kivymd.uix.recycleview.MDRecycleView(` _*args_ , _**kwargs_ `)` 

Recycle view class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `RecycleView` and _`MDAdaptiveWidget`_ classes documentation. 

**Chapter 2. Contents** 

**76** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3.11 Screen** 

`Screen` class equivalent. Simplifies working with some widget properties. For example: 

###### **Screen** 

KV 

```
Screen:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.screenmanagerimportScreen
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=Screen()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDScreen** 

Imperative python style with KV 

```
MDScreen:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDScreen(
```

(continues on next page) 

**2.3. Components** 

**77** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
height:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**Chapter 2. Contents** 

**78** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.screen` 

`class kivymd.uix.screen.MDScreen(` _*args_ , _**kwargs_ `)` 

Screen is an element intended to be used with a _`MDScreenManager`_ . 

For more information see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `Screen` and _`MDAdaptiveWidget`_ classes documentation. 

###### `hero_to` 

Must be a _`MDHeroTo`_ class. 

See the documentation of the MDHeroTo widget for more detailed information. 

Deprecated since version 1.0.0: Use attr: _heroes_to_ attribute instead. 

_`hero_to`_ is an `ObjectProperty` and defaults to _None_ . 

###### `heroes_to` 

Must be a list of _`MDHeroTo`_ class. 

Added in version 1.0.0. 

_`heroes_to`_ is an `LiatProperty` and defaults to _[]_ . 

`on_hero_to(` _screen_ , _widget:_ kivymd.uix.hero.MDHeroTo `)` _→_ None 

Fired when the value of the _`hero_to`_ attribute changes. 

###### **2.3.12 ResponsiveLayout** 

Added in version 1.0.0. 

**Responsive design is a graphic user interface (GUI) design approach used to create content that adjusts smoothly to various screen sizes.** 

The _`MDResponsiveLayout`_ class does not reorganize your UI. Its task is to track the size of the application screen and, depending on this size, the _`MDResponsiveLayout`_ class selects which UI layout should be displayed at the moment: mobile, tablet or desktop. Therefore, if you want to have a responsive view some kind of layout in your application, you should have three KV files with UI markup for three platforms. 

You need to set three parameters for the _`MDResponsiveLayout`_ class _`mobile_view`_ , _`tablet_view`_ and _`desktop_view`_ . These should be Kivy or KivyMD widgets. 

###### **Usage responsive** 

```
fromkivy.langimportBuilder
```

```
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.responsivelayoutimportMDResponsiveLayout
fromkivymd.uix.screenimportMDScreen
KV='''
```

(continues on next page) 

**2.3. Components** 

**79** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
<CommonComponentLabel>
halign:"center"
<MobileView>
CommonComponentLabel:
text:"Mobile"
<TabletView>
CommonComponentLabel:
text:"Table"
<DesktopView>
CommonComponentLabel:
text:"Desktop"
ResponsiveView:
'''
classCommonComponentLabel(MDLabel):
pass
classMobileView(MDScreen):
pass
classTabletView(MDScreen):
pass
classDesktopView(MDScreen):
pass
classResponsiveView(MDResponsiveLayout,MDScreen):
def__init__(self,**kw):
super().__init__(**kw)
self.mobile_view=MobileView()
self.tablet_view=TabletView()
self.desktop_view=DesktopView()
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
```

(continues on next page) 

**Chapter 2. Contents** 

**80** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Test().run()
```

**Note:** Use common components for platform layouts (mobile, tablet, desktop views). As shown in the example above, such a common component is the _CommonComponentLabel_ widget. 

###### **Usage responsive with multiple screen** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.responsivelayoutimportMDResponsiveLayout
fromkivymd.uix.screenimportMDScreen
KV='''
<CommonComponentLabel>
halign:"center"
#--------------------------------LogIn---------------------------------
<LogInMobileView>
CommonComponentLabel:
text:"LogInMobile"
<LogInTabletView>
CommonComponentLabel:
text:"LogInTable"
<LogInDesktopView>
CommonComponentLabel:
text:"LogInDesktop"
#-------------------------------LogOut---------------------------------
<LogOutMobileView>
CommonComponentLabel:
text:"LogOutMobile"
<LogOutTabletView>
CommonComponentLabel:
text:"LogOutTable"
<LogOutDesktopView>
```

(continues on next page) 

**2.3. Components** 

**81** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`CommonComponentLabel: text: "Log Out Desktop" # ------------------------------------------------------------------------MDScreenManager: id: manager md_bg_color: self.theme_cls.backgroundColor LogInResponsiveView: name: "login" on_touch_down: if self.collide_point(args[0].x, args[0].y): manager.current␣` _˓→_ `= "logout" LogOutResponsiveView: name: "logout" on_touch_down: if self.collide_point(args[0].x, args[0].y): manager.current␣` _˓→_ `= "login" ''' class CommonComponentLabel(MDLabel): pass` _`# -------------------------------- Log In ---------------------------------`_ `class LogInMobileView(MDScreen): pass class LogInTabletView(MDScreen): pass class LogInDesktopView(MDScreen): pass class LogInResponsiveView(MDResponsiveLayout, MDScreen): def __init__(self, **kw): super().__init__(**kw) self.mobile_view = LogInMobileView() self.tablet_view = LogInTabletView() self.desktop_view = LogInDesktopView()` _`# ------------------------------- Log Out ---------------------------------`_ `class LogOutMobileView(MDScreen): pass` 

(continues on next page) 

**Chapter 2. Contents** 

**82** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classLogOutTabletView(MDScreen):
pass
classLogOutDesktopView(MDScreen):
pass
classLogOutResponsiveView(MDResponsiveLayout,MDScreen):
def__init__(self,**kw):
super().__init__(**kw)
self.mobile_view=LogOutMobileView()
self.tablet_view=LogOutTabletView()
self.desktop_view=LogOutDesktopView()
#-------------------------------------------------------------------------
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Test().run()
```

Perhaps you expected more from the _`MDResponsiveLayout`_ widget, but even _Flutter_ uses a similar approach to creating a responsive UI. 

You can also use the commands provided to you by the developer tools to create a project with an responsive design. 

###### **API -** `kivymd.uix.responsivelayout` 

`class kivymd.uix.responsivelayout.MDResponsiveLayout(` _*args_ , _**kwargs_ `)` 

###### **Events** 

_`on_change_screen_type`_ Called when the screen type changes. 

###### `mobile_view` 

Mobile view. Must be a Kivy or KivyMD widget. 

_`mobile_view`_ is an `ObjectProperty` and defaults to _None_ . 

###### `tablet_view` 

Tablet view. Must be a Kivy or KivyMD widget. 

_`tablet_view`_ is an `ObjectProperty` and defaults to _None_ . 

###### `desktop_view` 

Desktop view. Must be a Kivy or KivyMD widget. 

_`desktop_view`_ is an `ObjectProperty` and defaults to _None_ . 

**2.3. Components** 

**83** 



<!-- Start of picture text -->
ScreenA ScreenB<br>MDHeroTo<br>MDHeroFrom<br>FitImage Fitimage<br><!-- End of picture text -->

~~PT~~ 

**KivyMD, Release 2.0.1.dev0** 

###### **Base example** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreenManager:
MDScreen:
name:"screenA"
md_bg_color:"lightblue"
MDHeroFrom:
id:hero_from
tag:"hero"
size_hint:None,None
size:"120dp","120dp"
pos_hint:{"top":.98}
x:24
FitImage:
source:"kivymd/images/logo/kivymd-icon-512.png"
size_hint:None,None
size:hero_from.size
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["hero"]
root.current="screenB"
MDButtonText:
text:"MoveHeroToScreenB"
MDScreen:
name:"screenB"
hero_to:hero_to
md_bg_color:"cadetblue"
MDHeroTo:
id:hero_to
tag:"hero"
size_hint:None,None
size:"220dp","220dp"
pos_hint:{"center_x":.5,"center_y":.5}
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
```

(continues on next page) 

**2.3. Components** 

**85** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
on_release:
root.current_heroes=["hero"]
root.current="screenA"
MDButtonText:
text:"MoveHeroToScreenA"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.heroimportMDHeroFrom,MDHeroTo
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classExample(MDApp):
defgo_to_screen(self,*args):
self.root.current_heroes=["hero"]
ifself.root.current=="screenA":
self.root.current="screenB"
else:
self.root.current="screenA"
defon_start(self):
defon_start(*args):
self.root.get_ids().image.size=self.root.get_ids().hero_from.size
self.root.get_ids().screen_b.hero_to=self.root.get_ids().hero_to
self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
self.root.get_ids().button_a.bind(on_release=self.go_to_screen)
Clock.schedule_once(on_start)
defbuild(self):
return(
MDScreenManager(
MDScreen(
MDHeroFrom(
FitImage(
id="image",
```

(continues on next page) 

**Chapter 2. Contents** 

**86** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
source="kivymd/images/logo/kivymd-icon-512.png",
size_hint=(None,None),
),
id="hero_from",
tag="hero",
size_hint=(None,None),
size=("120dp","120dp"),
pos_hint={"top":.98},
x=24,
),
MDButton(
MDButtonText(
text="MoveHeroToScreenB"
),
id="button_b",
pos_hint={"center_x":.5},
y="36dp",
),
name="screenA",
md_bg_color="lightblue",
),
MDScreen(
MDHeroTo(
id="hero_to",
tag="hero",
size_hint=(None,None),
size=("220dp","220dp"),
pos_hint={"center_x":.5,"center_y":.5},
),
MDButton(
MDButtonText(
text="MoveHeroToScreenA"
),
id="button_a",
pos_hint={"center_x":.5},
y="36dp",
),
id="screen_b",
name="screenB",
md_bg_color="cadetblue",
)
)
)
Example().run()
```

Note that the child of the _`MDHeroFrom`_ widget must have the size of the parent: Declarative KV style 

**2.3. Components** 

**87** 

**KivyMD, Release 2.0.1.dev0** 

```
MDHeroFrom:
id:hero_from
tag:"hero"
FitImage:
size_hint:None,None
size:hero_from.size
```

Declarative python style 

```
classExample(MDApp):
defon_start(self):
defon_start(*args):
self.root.get_ids().image.size=self.root.get_ids().hero_from.size
Clock.schedule_once(on_start)
defbuild(self):
return(
[...]
MDHeroFrom(
FitImage(
id="image",
size_hint=(None,None),
),
id="hero_from",
),
[...]
)
```

To enable hero animation before setting the name of the current screen for the screen manager, you must specify the name of the tag of the _`MDHeroFrom`_ container in which the hero is located: 

Declarative KV style 

```
MDButton:
on_release:
root.current_heroes=["hero"]
root.current="screen2"
MDButtonText:
text:"MoveHeroToScreenB"
```

Declarative python style 

```
classExample(MDApp):
defgo_to_screen(self,*args):
self.root.current_heroes=["hero"]
self.root.current="screen2"
defon_start(self):
self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
```

(continues on next page) 

**Chapter 2. Contents** 

**88** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defbuild(self):
return(
[...]
MDButton(
MDButtonText(
text="MoveHeroToScreenB"
),
id="button_b",
),
[...]
)
```

If you need to switch to a screen that does not contain heroes, set the _current_hero_ attribute for the screen manager as “” (empty string): 

Declarative KV style 

```
MDButton:
on_release:
root.current_heroes=[]
root.current="anotherscreen"
MDButtonText:
text:"GoToAnotherScreen"
```

Declarative python style 

```
classExample(MDApp):
defgo_to_screen(self,*args):
self.root.current_heroes=[]
self.root.current="anotherscreen"
defon_start(self):
self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
defbuild(self):
return(
[...]
MDButton(
MDButtonText(
text="GoToAnotherScreen"
),
id="button_b",
),
[...]
)
```

**2.3. Components** 

**89** 

**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreenManager:
MDScreen:
name:"screenA"
md_bg_color:"lightblue"
MDHeroFrom:
id:hero_from
tag:"hero"
size_hint:None,None
size:"120dp","120dp"
pos_hint:{"top":.98}
x:24
FitImage:
source:"kivymd/images/logo/kivymd-icon-512.png"
size_hint:None,None
size:hero_from.size
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["hero"]
root.current="screenB"
MDButtonText:
text:"MoveHeroToScreenB"
MDScreen:
name:"screenB"
hero_to:hero_to
md_bg_color:"cadetblue"
MDHeroTo:
id:hero_to
tag:"hero"
size_hint:None,None
size:"220dp","220dp"
pos_hint:{"center_x":.5,"center_y":.5}
MDButton:
pos_hint:{"center_x":.5}
y:"52dp"
```

(continues on next page) 

**Chapter 2. Contents** 

**90** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
on_release:
root.current_heroes=[]
root.current="screenC"
MDButtonText:
text:"GoToScreenC"
MDButton:
pos_hint:{"center_x":.5}
y:"8dp"
on_release:
root.current_heroes=["hero"]
root.current="screenA"
MDButtonText:
text:"MoveHeroToScreenA"
MDScreen:
name:"screenC"
md_bg_color:"olive"
MDLabel:
text:"ScreenC"
halign:"center"
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current="screenB"
MDButtonText:
text:"BackToScreenB"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.heroimportMDHeroFrom,MDHeroTo
fromkivymd.uix.labelimportMDLabel
```

(continues on next page) 

**2.3. Components** 

**91** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classExample(MDApp):
defon_start(self):
defon_start(*args):
self.root.get_ids().screen_b.hero_to=self.root.get_ids().hero_to
Clock.schedule_once(on_start)
defbuild(self):
returnMDScreenManager(
MDScreen(
MDHeroFrom(
FitImage(
source="kivymd/images/logo/kivymd-icon-512.png",
size_hint=(None,None),
),
id="hero_from",
tag="hero",
size_hint=(None,None),
size=("120dp","120dp"),
pos_hint={"top":0.98},
x=24,
),
MDButton(
MDButtonText(text="MoveHeroToScreenB"),
pos_hint={"center_x":0.5},
y="36dp",
on_release=lambdax:(
setattr(self.root,"current_heroes",["hero"]),
setattr(self.root,"current","screenB")
)
),
name="screenA",
md_bg_color="lightblue",
),
MDScreen(
MDHeroTo(
id="hero_to",
tag="hero",
size_hint=(None,None),
size=("220dp","220dp"),
pos_hint={"center_x":0.5,"center_y":0.5},
),
MDButton(
MDButtonText(text="GoToScreenC"),
pos_hint={"center_x":0.5},
y="52dp",
on_release=lambdax:(
setattr(self.root,"current_heroes",[]),
```

(continues on next page) 

**Chapter 2. Contents** 

**92** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
setattr(self.root,"current","screenC")
)
),
MDButton(
MDButtonText(text="MoveHeroToScreenA"),
pos_hint={"center_x":0.5},
y="8dp",
on_release=lambdax:(
setattr(self.root,"current_heroes",["hero"]),
setattr(self.root,"current","screenA")
)
),
id="screen_b",
name="screenB",
md_bg_color="cadetblue",
),
MDScreen(
MDLabel(
text="ScreenC",
halign="center",
),
MDButton(
MDButtonText(text="BackToScreenB"),
pos_hint={"center_x":0.5},
y="36dp",
on_release=lambdax:setattr(self.root,"current","screenB")
),
name="screenC",
md_bg_color="olive",
)
)
Example().run()
```

###### **Events** 

Two events are available for the hero: 

- _on_transform_in_ - when the hero flies from screen **A** to screen **B** . 

- _on_transform_out_ - when the hero back from screen **B** to screen **A** . 

The _on_transform_in_ , _on_transform_out_ events relate to the _`MDHeroFrom`_ container. For example, let’s change the radius and background color of the hero during the flight between the screens: 

Declarative python style with KV 

```
fromkivyimportutils
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
```

(continues on next page) 

**2.3. Components** 

**93** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivy.utilsimportget_color_from_hex
fromkivymd.appimportMDApp
fromkivymd.uix.heroimportMDHeroFrom
fromkivymd.uix.relativelayoutimportMDRelativeLayout
KV='''
MDScreenManager:
MDScreen:
name:"screenA"
md_bg_color:"lightblue"
MyHero:
id:hero_from
tag:"hero"
size_hint:None,None
size:"120dp","120dp"
pos_hint:{"top":.98}
x:24
MDRelativeLayout:
size_hint:None,None
size:hero_from.size
md_bg_color:"blue"
radius:[24,12,24,12]
FitImage:
source:"kivymd/images/logo/kivymd-icon-512.png"
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["hero"]
root.current="screenB"
MDButtonText:
text:"MoveHeroToScreenB"
MDScreen:
name:"screenB"
hero_to:hero_to
md_bg_color:"cadetblue"
MDHeroTo:
id:hero_to
tag:"hero"
size_hint:None,None
size:"220dp","220dp"
pos_hint:{"center_x":.5,"center_y":.5}
```

(continues on next page) 

**Chapter 2. Contents** 

**94** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["hero"]
root.current="screenA"
MDButtonText:
text:"MoveHeroToScreenA"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
classMyHero(MDHeroFrom):
defon_transform_in(
self,instance_hero_widget:MDRelativeLayout,duration:float
):
'''
Firedwhentheherofliesfromscreen**A**toscreen**B**.
:paraminstance_hero_widget:dhildwidgetofthe�MDHeroFrom�class.
:paramdurationofthetransitionanimationbetweenscreens.
'''
Animation(
radius=[12,24,12,24],
duration=duration,
md_bg_color=(0,1,1,1),
).start(instance_hero_widget)
defon_transform_out(
self,instance_hero_widget:MDRelativeLayout,duration:float
):
'''Firedwhentheherobackfromscreen**B**toscreen**A**.'''
Animation(
radius=[24,12,24,12],
duration=duration,
md_bg_color=get_color_from_hex(utils.hex_colormap["blue"]),
).start(instance_hero_widget)
```

```
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivy.animationimportAnimation
```

(continues on next page) 

**2.3. Components** 

**95** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivy.utilsimportget_color_from_hex
fromkivyimportutils
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.heroimportMDHeroFrom,MDHeroTo
fromkivymd.uix.relativelayoutimportMDRelativeLayout
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
```

```
classMyHero(MDHeroFrom):
defon_transform_in(
self,instance_hero_widget:MDRelativeLayout,duration:float
):
'''
Firedwhentheherofliesfromscreen**A**toscreen**B**.
:paraminstance_hero_widget:dhildwidgetofthe�MDHeroFrom�class.
:paramdurationofthetransitionanimationbetweenscreens.
'''
Animation(
radius=[12,24,12,24],
duration=0.1,
md_bg_color=(0,1,1,1),
).start(instance_hero_widget)
defon_transform_out(
self,instance_hero_widget:MDRelativeLayout,duration:float
):
'''Firedwhentheherobackfromscreen**B**toscreen**A**.'''
Animation(
radius=[24,12,24,12],
duration=0.1,
md_bg_color=get_color_from_hex(utils.hex_colormap["blue"]),
).start(instance_hero_widget)
classExample(MDApp):
defgo_to_screen(self,*args):
self.root.current_heroes=["hero"]
ifself.root.current=="screenA":
self.root.current="screenB"
else:
self.root.current="screenA"
defon_start(self):
defon_start(*args):
self.root.get_ids().relative.size=self.root.get_ids().hero_from.size
```

(continues on next page) 

**Chapter 2. Contents** 

**96** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.get_ids().screen_b.hero_to=self.root.get_ids().hero_to
self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
self.root.get_ids().button_a.bind(on_release=self.go_to_screen)
Clock.schedule_once(on_start)
defbuild(self):
return(
MDScreenManager(
MDScreen(
MyHero(
MDRelativeLayout(
FitImage(
source="kivymd/images/logo/kivymd-icon-512.png",
),
id="relative",
size_hint=(None,None),
md_bg_color="blue",
radius=[24,12,24,12],
),
id="hero_from",
tag="hero",
size_hint=(None,None),
size=("120dp","120dp"),
pos_hint={"top":.98},
x=24,
),
MDButton(
MDButtonText(
text="MoveHeroToScreenB"
),
id="button_b",
pos_hint={"center_x":.5},
y="36dp",
),
name="screenA",
md_bg_color="lightblue",
),
MDScreen(
MDHeroTo(
id="hero_to",
tag="hero",
size_hint=(None,None),
size=("220dp","220dp"),
pos_hint={"center_x":.5,"center_y":.5},
),
MDButton(
MDButtonText(
text="MoveHeroToScreenA"
),
id="button_a",
pos_hint={"center_x":.5},
```

(continues on next page) 

**2.3. Components** 

**97** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
y="36dp",
),
id="screen_b",
name="screenB",
md_bg_color="cadetblue",
)
)
)
Example().run()
```

###### **Usage with ScrollView** 

Declarative python style with KV 

```
fromkivy.animationimportAnimation
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty,ObjectProperty
fromkivymd.appimportMDApp
fromkivymd.uix.heroimportMDHeroFrom
KV='''
<HeroItem>
size_hint_y:None
height:"200dp"
radius:"24dp"
MDSmartTile:
id:tile
size_hint:None,None
size:root.size
on_release:root.on_release()
MDSmartTileImage:
id:image
source:"kivymd/images/logo/kivymd-icon-512.png"
radius:dp(24)
MDSmartTileOverlayContainer:
id:overlay
md_bg_color:0,0,0,.5
adaptive_height:True
padding:"8dp"
spacing:"8dp"
radius:[0,0,dp(24),dp(24)]
```

(continues on next page) 

**Chapter 2. Contents** 

**98** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDLabel:
text:root.tag
theme_text_color:"Custom"
text_color:"white"
adaptive_height:True
MDScreenManager:
md_bg_color:self.theme_cls.backgroundColor
MDScreen:
name:"screenA"
ScrollView:
MDGridLayout:
id:box
cols:2
spacing:"12dp"
padding:"12dp"
adaptive_height:True
MDScreen:
name:"screenB"
heroes_to:[hero_to]
MDHeroTo:
id:hero_to
size_hint:1,None
height:"220dp"
pos_hint:{"top":1}
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=[hero_to.tag]
root.current="screenA"
MDButtonText:
text:"MoveHeroToScreenA"
'''
classHeroItem(MDHeroFrom):
text=StringProperty()
manager=ObjectProperty()
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.ids.image.ripple_duration_in_fast=0.05
```

(continues on next page) 

**2.3. Components** 

**99** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defon_transform_in(self,instance_hero_widget,duration):
forinstancein[
instance_hero_widget,
instance_hero_widget._overlay_container,
instance_hero_widget._image,
]:
Animation(radius=[0,0,0,0],duration=duration).start(instance)
defon_transform_out(self,instance_hero_widget,duration):
forinstance,radiusin{
instance_hero_widget:[dp(24),dp(24),dp(24),dp(24)],
instance_hero_widget._overlay_container:[0,0,dp(24),dp(24)],
instance_hero_widget._image:[dp(24),dp(24),dp(24),dp(24)],
}.items():
Animation(
radius=radius,
duration=duration,
).start(instance)
defon_release(self):
defswitch_screen(*args):
self.manager.current_heroes=[self.tag]
self.manager.ids.hero_to.tag=self.tag
self.manager.current="screenB"
Clock.schedule_once(switch_screen,0.2)
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
foriinrange(12):
hero_item=HeroItem(
text=f"Item{i+1}",tag=f"Tag{i}",manager=self.root
)
ifnoti%2:
hero_item.md_bg_color="lightgrey"
self.root.ids.box.add_widget(hero_item)
Example().run()
```

Declarative python style 

```
fromkivy.animationimportAnimation
fromkivy.clockimportClock
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty,ObjectProperty
```

(continues on next page) 

**Chapter 2. Contents** 

**100** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.gridlayoutimportMDGridLayout
fromkivymd.uix.heroimportMDHeroFrom,MDHeroTo
fromkivymd.uix.imagelistimport(
MDSmartTile,MDSmartTileImage,MDSmartTileOverlayContainer
)
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
fromkivymd.uix.scrollviewimportMDScrollView
classHeroItem(MDHeroFrom):
text=StringProperty()
manager=ObjectProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.size_hint_y=None
self.height="200dp"
self.radius="24dp"
Clock.schedule_once(self.build_widgets,0.4)
defbuild_widgets(self,*args):
self.add_widget(
MDSmartTile(
MDSmartTileImage(
id="image",
source="kivymd/images/logo/kivymd-icon-512.png",
radius=dp(24),
),
MDSmartTileOverlayContainer(
MDLabel(
text=self.tag,
theme_text_color="Custom",
text_color="white",
adaptive_height=True,
),
id="overlay",
md_bg_color=(0,0,0,.5),
adaptive_height=True,
padding="8dp",
spacing="8dp",
radius=[0,0,dp(24),dp(24)],
),
id="tile",
size_hint=(None,None),
size=self.size,
on_release=lambdax:self.on_release(),
)
)
```

(continues on next page) 

**2.3. Components** 

**101** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.get_ids().image.ripple_duration_in_fast=0.05
defon_transform_in(self,instance_hero_widget,duration):
forinstancein[
instance_hero_widget,
instance_hero_widget._overlay_container,
instance_hero_widget._image,
]:
Animation(radius=[0,0,0,0],duration=duration).start(instance)
defon_transform_out(self,instance_hero_widget,duration):
forinstance,radiusin{
instance_hero_widget:[dp(24),dp(24),dp(24),dp(24)],
instance_hero_widget._overlay_container:[0,0,dp(24),dp(24)],
instance_hero_widget._image:[dp(24),dp(24),dp(24),dp(24)],
}.items():
Animation(radius=radius,duration=duration).start(instance)
defon_release(self):
defswitch_screen(*args):
self.manager.current_heroes=[self.tag]
self.manager.get_ids().hero_to.tag=self.tag
self.manager.current="screenB"
```

```
Clock.schedule_once(switch_screen,0.2)
```

```
classExample(MDApp):
defbuild(self):
return(
MDScreenManager(
MDScreen(
MDScrollView(
MDGridLayout(
id="box",
cols=2,
spacing="12dp",
padding="12dp",
adaptive_height=True,
)
),
name="screenA"
),
MDScreen(
MDHeroTo(
id="hero_to",
size_hint=(1,None),
height="220dp",
pos_hint={"top":1},
),
MDButton(
MDButtonText(
```

(continues on next page) 

**Chapter 2. Contents** 

**102** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text="MoveHeroToScreenA"
),
id="button_move_to_screen_a",
pos_hint={"center_x":.5},
y="36dp",
),
id="screen_b",
name="screenB",
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defgo_to_screen(self,*args):
self.root.current_heroes=[self.root.get_ids().hero_to.tag]
self.root.current="screenA"
defon_start(self):
self.root.get_ids().screen_b.heroes_to=[self.root.get_ids().hero_to]
self.root.get_ids().button_move_to_screen_a.bind(
on_release=self.go_to_screen
)
foriinrange(12):
hero_item=HeroItem(
text=f"Item{i+1}",tag=f"Tag{i}",manager=self.root
)
ifnoti%2:
hero_item.md_bg_color="lightgrey"
self.root.get_ids().box.add_widget(hero_item)
Example().run()
```

###### **Using multiple heroes at the same time** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreenManager:
MDScreen:
name:"screenA"
md_bg_color:"lightblue"
MDHeroFrom:
```

(continues on next page) 

**2.3. Components** 

**103** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
id:hero_kivymd
tag:"kivymd"
size_hint:None,None
size:"200dp","200dp"
pos_hint:{"top":.98}
x:"24dp"
FitImage:
source:"kivymd/images/logo/kivymd-icon-512.png"
size_hint:None,None
size:hero_kivymd.size
radius:self.height/2
MDHeroFrom:
id:hero_kivy
tag:"kivy"
size_hint:None,None
size:"200dp","200dp"
pos_hint:{"top":.98}
x:"324dp"
FitImage:
source:"data/logo/kivy-icon-512.png"
size_hint:None,None
size:hero_kivy.size
radius:self.height/2
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["kivymd","kivy"]
root.current="screenB"
MDButtonText:
text:"MoveHeroToScreenB"
MDScreen:
name:"screenB"
heroes_to:hero_to_kivymd,hero_to_kivy
md_bg_color:"cadetblue"
MDHeroTo:
id:hero_to_kivy
tag:"kivy"
size_hint:None,None
pos_hint:{"center_x":.5,"center_y":.5}
MDHeroTo:
id:hero_to_kivymd
tag:"kivymd"
size_hint:None,None
```

(continues on next page) 

**Chapter 2. Contents** 

**104** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
pos_hint:{"right":1,"top":1}
MDButton:
pos_hint:{"center_x":.5}
y:"36dp"
on_release:
root.current_heroes=["kivy","kivymd"]
root.current="screenA"
MDButtonText:
text:"MoveHeroToScreenA"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.material_resourcesimportdp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.heroimportMDHeroFrom,MDHeroTo
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classExample(MDApp):
defgo_to_screen(self,*args):
ifself.root.current=="screenA":
self.root.current_heroes=["kivymd","kivy"]
self.root.current="screenB"
else:
self.root.current_heroes=["kivy","kivymd"]
self.root.current="screenA"
defon_start(self):
defon_start(*args):
logo_kivymd=self.root.get_ids().logo_kivymd
logo_kivy=self.root.get_ids().logo_kivy
logo_kivymd.size=self.root.get_ids().hero_kivymd.size
logo_kivymd.radius=logo_kivymd.height/2
logo_kivy.size=self.root.get_ids().hero_kivy.size
```

(continues on next page) 

**2.3. Components** 

**105** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
logo_kivy.radius=logo_kivy.height/2
self.root.get_ids().button_move_heto_to_screen_b.bind(
on_release=self.go_to_screen
)
self.root.get_ids().button_move_heto_to_screen_a.bind(
on_release=self.go_to_screen
)
self.root.get_ids().screen_b.heroes_to=[
self.root.get_ids().hero_to_kivymd,self.root.get_ids().hero_to_kivy
]
Clock.schedule_once(on_start)
```

`def build(self): return ( MDScreenManager( MDScreen( MDHeroFrom( FitImage( id="logo_kivymd", source="kivymd/images/logo/kivymd-icon-512.png", size_hint=(None, None), ), id="hero_kivymd", tag="kivymd", size_hint=(None, None), size=("200dp", "200dp"), pos_hint={"top": .98}, x=dp(24), ), MDHeroFrom( FitImage( id="logo_kivy", source="data/logo/kivy-icon-512.png", size_hint=(None, None), ), id="hero_kivy", tag="kivy", size_hint=(None, None), size=("200dp", "200dp"), pos_hint={"top": .98}, x="324dp", ), MDButton( MDButtonText( text="Move Hero To Screen B" ), id="button_move_heto_to_screen_b", pos_hint={"center_x": .5}, y="36dp", ),` (continues on next page) 

**Chapter 2. Contents** 

**106** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
name="screenA",
md_bg_color="lightblue",
),
MDScreen(
MDHeroTo(
id="hero_to_kivy",
tag="kivy",
size_hint=(None,None),
pos_hint={"center_x":.5,"center_y":.5},
),
MDHeroTo(
id="hero_to_kivymd",
tag="kivymd",
size_hint=(None,None),
pos_hint={"right":1,"top":1},
),
MDButton(
MDButtonText(
text="MoveHeroToScreenA"
),
id="button_move_heto_to_screen_a",
pos_hint={"center_x":.5},
y="36dp",
),
id="screen_b",
name="screenB",
md_bg_color="cadetblue",
)
)
)
Example().run()
```

**API -** `kivymd.uix.hero` 

`class kivymd.uix.hero.MDHeroFrom(` _*args_ , _**kwargs_ `)` 

The container from which the hero begins his flight. 

For more information, see in the _`MDBoxLayout`_ class documentation. 

###### **Events** 

###### **_on_transform_in_** 

when the hero flies from screen **A** to screen **B** . 

###### **_on_transform_out_** 

Fired when the hero back from screen **B** to screen **A** . 

###### `tag` 

Tag ID for heroes. 

_`tag`_ is an `StringProperty` and defaults to _‘’_ . 

**2.3. Components** 

**107** 

**KivyMD, Release 2.0.1.dev0** 

`on_transform_in(` _*args_ `)` 

Fired when the hero flies from screen **A** to screen **B** . 

`on_transform_out(` _*args_ `)` 

Fired when the hero back from screen **B** to screen **A** . 

`class kivymd.uix.hero.MDHeroTo(` _*args_ , _**kwargs_ `)` 

The container in which the hero comes. 

For more information, see in the _`MDBoxLayout`_ class documentation. 

```
tag
```

Tag ID for heroes. 

_`tag`_ is an `StringProperty` and defaults to _‘’_ . 

###### **2.3.14 AnchorLayout** 

Added in version 1.0.0. 

`AnchorLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **AnchorLayout** 

KV 

```
AnchorLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.anchorlayoutimportAnchorLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=AnchorLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

**Chapter 2. Contents** 

**108** 

**KivyMD, Release 2.0.1.dev0** 

###### **MDAnchorLayout** 

Imperative python style with KV 

```
MDAnchorLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.anchorlayoutimportMDAnchorLayout
fromkivymd.appimportMDApp
```

```
classMyApp(App):
defbuild(self):
returnMDAnchorLayout(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

**2.3. Components** 

**109** 

**KivyMD, Release 2.0.1.dev0** 

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**API -** `kivymd.uix.anchorlayout` 

`class kivymd.uix.anchorlayout.MDAnchorLayout(` _*args_ , _**kwargs_ `)` 

Anchor layout class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `AnchorLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.15 BoxLayout** 

`BoxLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **BoxLayout** 

KV 

```
BoxLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.boxlayoutimportBoxLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
```

```
classMyApp(App):
defbuild(self):
layout=BoxLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
```

(continues on next page) 

**Chapter 2. Contents** 

**110** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MyApp().run()
```

###### **MDBoxLayout** 

Imperative python style with KV 

```
MDBoxLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.boxlayoutimportBoxLayout
fromkivymd.appimportMDApp
```

```
classMyApp(App):
defbuild(self):
returnMDBoxLayout(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

**2.3. Components** 

**111** 

**KivyMD, Release 2.0.1.dev0** 

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

###### **API -** `kivymd.uix.boxlayout` 

`class kivymd.uix.boxlayout.MDBoxLayout(` _*args_ , _**kwargs_ `)` 

Box layout class. 

For more information see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `BoxLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.16 Widget** 

`Widget` class equivalent. Simplifies working with some widget properties. For example: 

###### **Widget** 

KV 

```
Widget:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

**Chapter 2. Contents** 

**112** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.uix.widgetimportWidget
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
widget=Widget()
withwidget.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnwidget
MyApp().run()
```

###### **MDWidget** 

Imperative python style with KV 

```
MDWidget:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.widgetimportMDWidget
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDWidget(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

**2.3. Components** 

**113** 

**KivyMD, Release 2.0.1.dev0** 

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
height:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

###### **API -** `kivymd.uix.widget` 

`class kivymd.uix.widget.MDWidget(` _*args_ , _**kwargs_ `)` 

Widget class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and _`MDAdaptiveWidget`_ and `Widget` and classes documentation. 

Added in version 1.0.0. 

**Chapter 2. Contents** 

**114** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.3.17 RecycleGridLayout** 

`RecycleGridLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **RecycleGridLayout** 

KV 

```
RecycleGridLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.recyclegridlayoutimportRecycleGridLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=RecycleGridLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

###### **MDRecycleGridLayout** 

Imperative python style with KV 

```
MDRecycleGridLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.recyclegridlayoutimportMDRecycleGridLayout
fromkivymd.appimportMDApp
classMyApp(App):
defbuild(self):
returnMDRecycleGridLayout(
```

(continues on next page) 

**2.3. Components** 

**115** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

###### **adaptive_size** 

```
adaptive_size:True
```

Equivalent 

```
size_hint:None,None
size:self.minimum_size
```

**Chapter 2. Contents** 

**116** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.recyclegridlayout` 

`class kivymd.uix.recyclegridlayout.MDRecycleGridLayout(` _*args_ , _**kwargs_ `)` 

Recycle grid layout class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `RecycleGridLayout` and _`MDAdaptiveWidget`_ classes documentation. 

###### **2.3.18 GridLayout** 

`GridLayout` class equivalent. Simplifies working with some widget properties. For example: 

###### **GridLayout** 

KV 

```
GridLayout:
canvas:
Color:
rgba:app.theme_cls.primaryColor
Rectangle:
pos:self.pos
size:self.size
```

Python 

```
fromkivy.uix.gridlayoutimportGridLayout
fromkivy.graphicsimportColor,Rectangle
fromkivy.appimportApp
classMyApp(App):
defbuild(self):
layout=GridLayout()
withlayout.canvas:
Color(*self.theme_cls.primary_color)
self.rect=Rectangle(pos=layout.pos,size=layout.size)
returnlayout
MyApp().run()
```

**2.3. Components** 

**117** 

**KivyMD, Release 2.0.1.dev0** 

###### **MDGridLayout** 

Imperative python style with KV 

```
MDGridLayout:
md_bg_color:app.theme_cls.primaryColor
```

Declarative python style 

```
fromkivymd.uix.gridlayoutimportMDGridLayout
fromkivymd.appimportMDApp
```

```
classMyApp(App):
defbuild(self):
returnMDGridLayout(
md_bg_color=self.theme_cls.primaryColor
)
MyApp().run()
```

###### **Available options are:** 

- _adaptive_height_ 

- _adaptive_width_ 

- _adaptive_size_ 

###### **adaptive_height** 

```
adaptive_height:True
```

Equivalent 

```
size_hint_y:None
height:self.minimum_height
```

###### **adaptive_width** 

```
adaptive_width:True
```

Equivalent 

```
size_hint_x:None
width:self.minimum_width
```

**Chapter 2. Contents** 

**118** 





<!-- Start of picture text -->
VAs<br>€ My saved media A :<br>T | a a J<br>“ re<br>Tabs organize content across different screens and views<br>i : ~<br><!-- End of picture text -->



<!-- Start of picture text -->
4 i @<br>Flights Trips Explore<br>@) Overview Specifications<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTabsItem(
MDTabsItemIcon(
MDTabsBadge(
text="99",
),
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
else:
self.root.ids.tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.ids.tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItem,
MDTabsItemIcon,
MDTabsItemText,
MDTabsBadge,
MDTabsPrimary,
)
```

```
classExample(MDApp):
defon_start(self):
fortab_icon,tab_namein{
"airplane":"Flights",
"treasure-chest":"Trips",
"compass-outline":"Explore",
```

(continues on next page) 

**2.3. Components** 

**121** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
}.items():
iftab_icon=="treasure-chest":
self.root.get_ids().tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
MDTabsBadge(
text="99",
),
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
else:
self.root.get_ids().tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.get_ids().tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTabsPrimary(
MDDivider(),
id="tabs",
pos_hint={"center_x":.5,"center_y":.5},
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**122** 



<!-- Start of picture text -->
x = @<br>Flights Trips Explore<br><!-- End of picture text -->



<!-- Start of picture text -->
MDTabsBadge<br>x MDTabsitemicon «— £2 @)<br>Flights Trips ——-* MDTabsltemText | Explore<br>MDTabsltem<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
id:tabs
pos_hint:{"center_x":.5,"center_y":.5}
MDDivider:
'''
classExample(MDApp):
defon_start(self):
fortab_icon,tab_namein{
"airplane":"Flights",
"treasure-chest":"Trips",
"compass-outline":"Explore",
}.items():
iftab_icon=="treasure-chest":
self.root.ids.tabs.add_widget(
MDTabsItemSecondary(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
MDTabsBadge(
text="5",
),
)
)
else:
self.root.ids.tabs.add_widget(
MDTabsItemSecondary(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.ids.tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
```

(continues on next page) 

**Chapter 2. Contents** 

**124** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItemIcon,
MDTabsItemText,
MDTabsBadge,
MDTabsSecondary,
MDTabsItemSecondary,
)
classExample(MDApp):
defon_start(self):
fortab_icon,tab_namein{
"airplane":"Flights",
"treasure-chest":"Trips",
"compass-outline":"Explore",
}.items():
iftab_icon=="treasure-chest":
self.root.get_ids().tabs.add_widget(
MDTabsItemSecondary(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
MDTabsBadge(
text="5",
),
)
)
else:
self.root.get_ids().tabs.add_widget(
MDTabsItemSecondary(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.get_ids().tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTabsSecondary(
MDDivider(),
id="tabs",
pos_hint={"center_x":.5,"center_y":.5},
```

(continues on next page) 

**2.3. Components** 

**125** 





<!-- Start of picture text -->
MDTabslitemSecondary MDTabsitemlcon<br>MDTabslitemText<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDDivider:
MDTabsCarousel:
id:related_content_container
size_hint_y:None
height:dp(320)
'''
classExample(MDApp):
defon_start(self):
fortab_icon,tab_namein{
"airplane":"Flights",
"treasure-chest":"Trips",
"compass-outline":"Explore",
}.items():
self.root.ids.tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.ids.related_content_container.add_widget(
MDLabel(
text=tab_name,
halign="center",
)
)
self.root.ids.tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.material_resourcesimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItemIcon,
MDTabsItemText,
```

(continues on next page) 

**2.3. Components** 

**127** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTabsPrimary,
MDTabsCarousel,
MDTabsItem,
)
classExample(MDApp):
defon_start(self):
fortab_icon,tab_namein{
"airplane":"Flights",
"treasure-chest":"Trips",
"compass-outline":"Explore",
}.items():
self.root.get_ids().tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=tab_icon,
),
MDTabsItemText(
text=tab_name,
),
)
)
self.root.get_ids().related_content_container.add_widget(
MDLabel(
text=tab_name,
halign="center",
)
)
self.root.get_ids().tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTabsPrimary(
MDDivider(),
MDTabsCarousel(
id="related_content_container",
size_hint_y=None,
height=dp(320),
),
id="tabs",
pos_hint={"center_x":.5,"center_y":.5},
size_hint_x=0.6,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**128** 

**KivyMD, Release 2.0.1.dev0** 

###### **Behaviors** 

###### **Scrollable tabs** 

When a set of tabs cannot fit on screen, use scrollable tabs. Scrollable tabs can use longer text labels and a larger number of tabs. They are best used for browsing on touch interfaces. 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.tabimportMDTabsItemText,MDTabsItem
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDTabsPrimary:
id:tabs
pos_hint:{"center_x":.5,"center_y":.5}
size_hint_x:.6
allow_stretch:False
label_only:True
MDDivider:
'''
classExample(MDApp):
defon_start(self):
fortab_namein[
"Moscow",
"SaintPetersburg",
"Novosibirsk",
"Yekaterinburg",
"Kazan",
"NizhnyNovgorod",
"Chelyabinsk",
]:
self.root.ids.tabs.add_widget(
MDTabsItem(
MDTabsItemText(
text=tab_name,
),
)
)
self.root.ids.tabs.switch_tab(text="Moscow")
defbuild(self):
self.theme_cls.primary_palette="Olive"
```

(continues on next page) 

**2.3. Components** 

**129** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItemText,
MDTabsPrimary,
MDTabsItem,
)
```

```
classExample(MDApp):
defon_start(self):
fortab_namein[
"Moscow",
"SaintPetersburg",
"Novosibirsk",
"Yekaterinburg",
"Kazan",
"NizhnyNovgorod",
"Chelyabinsk",
]:
self.root.get_ids().tabs.add_widget(
MDTabsItem(
MDTabsItemText(
text=tab_name,
),
)
)
self.root.get_ids().tabs.switch_tab(text="Moscow")
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTabsPrimary(
MDDivider(),
id="tabs",
pos_hint={"center_x":.5,"center_y":.5},
size_hint_x=0.6,
allow_stretch=False,
label_only=True,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
```

(continues on next page) 

**Chapter 2. Contents** 

**130** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

###### **Fixed tabs** 

Fixed tabs display all tabs in a set simultaneously. They are best for switching between related content quickly, such as between transportation methods in a map. To navigate between fixed tabs, tap an individual tab, or swipe left or right in the content area. 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.tabimportMDTabsItemText,MDTabsItem
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDTabsPrimary:
id:tabs
pos_hint:{"center_x":.5,"center_y":.5}
size_hint_x:.6
allow_stretch:True
label_only:True
MDDivider:
'''
classExample(MDApp):
defon_start(self):
fortab_namein[
"Moscow","SaintPetersburg","Novosibirsk"
]:
self.root.ids.tabs.add_widget(
MDTabsItem(
MDTabsItemText(
text=tab_name,
),
)
)
self.root.ids.tabs.switch_tab(text="Moscow")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
```

(continues on next page) 

**2.3. Components** 

**131** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItemText,
MDTabsPrimary,
MDTabsItem,
)
classExample(MDApp):
defon_start(self):
fortab_namein[
"Moscow","SaintPetersburg","Novosibirsk"
]:
self.root.get_ids().tabs.add_widget(
MDTabsItem(
MDTabsItemText(
text=tab_name,
),
)
)
self.root.get_ids().tabs.switch_tab(text="Moscow")
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTabsPrimary(
MDDivider(),
id="tabs",
pos_hint={"center_x":.5,"center_y":.5},
size_hint_x=0.6,
allow_stretch=True,
label_only=True,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**132** 



<!-- Start of picture text -->
Moscow Saint Petersburg Novosibirsk<br><!-- End of picture text -->





**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTabs:
id:tabs
on_ref_press:app.on_ref_press(*args)
<Tab>
MDIconButton:
id:icon
icon:app.icons[0]
icon_size:"48sp"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classTab(MDFloatLayout,MDTabsBase):
'''Classimplementingcontentforatab.'''
classExample(MDApp):
icons=list(md_icons.keys())[15:30]
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
forname_tabinself.icons:
self.root.ids.tabs.add_widget(
Tab(title=name_tab,icon=name_tab)
)
Example().run()
```

###### **2.0.0 version** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.uix.labelimportMDIcon
fromkivymd.uix.tabimportMDTabsItem,MDTabsItemIcon
fromkivymd.uix.tab.tabimportMDTabsItemText
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
```

(continues on next page) 

**Chapter 2. Contents** 

**134** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTabsPrimary:
id:tabs
allow_stretch:False
pos_hint:{"center_x":.5,"center_y":.5}
MDDivider:
MDTabsCarousel:
id:related_content
size_hint_y:None
-
height:root.heighttabs.ids.tab_scroll.height
'''
classExample(MDApp):
defon_start(self):
forname_tabinlist(md_icons.keys())[15:30]:
self.root.ids.tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=name_tab,
),
MDTabsItemText(
text=name_tab,
),
)
)
self.root.ids.related_content.add_widget(
MDIcon(
icon=name_tab,
pos_hint={"center_x":0.5,"center_y":0.5},
)
)
self.root.ids.tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.labelimportMDIcon
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tabimport(
MDTabsItemIcon,
MDTabsItemText,
MDTabsPrimary,
```

(continues on next page) 

**2.3. Components** 

**135** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTabsCarousel,
MDTabsItem,
)
classExample(MDApp):
defon_start(self):
tabs=self.root.get_ids().tabs
related_content=self.root.get_ids().related_content
related_content.height=(
self.root.height-tabs.ids.tab_scroll.height
)
forname_tabinlist(md_icons.keys())[15:30]:
tabs.add_widget(
MDTabsItem(
MDTabsItemIcon(
icon=name_tab,
),
MDTabsItemText(
text=name_tab,
),
)
)
related_content.add_widget(
MDIcon(
icon=name_tab,
pos_hint={"center_x":0.5,"center_y":0.5},
)
)
tabs.switch_tab(icon="airplane")
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnMDScreen(
MDTabsPrimary(
MDDivider(),
MDTabsCarousel(
id="related_content",
size_hint_y=None,
),
id="tabs",
pos_hint={"center_x":0.5,"center_y":0.5},
allow_stretch=False,
),
md_bg_color=self.theme_cls.backgroundColor,
)
Example().run()
```

**Chapter 2. Contents** 

**136** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.tab.tab` 

- `class kivymd.uix.tab.tab.MDTabsBadge(` _*args_ , _**kwargs_ `)` 

Implements an badge for secondary tabs. 

Added in version 2.0.0. 

For more information, see in the _`MDBadge`_ class documentation. 

- `class kivymd.uix.tab.tab.MDTabsCarousel(` _*args_ , _**kwargs_ `)` 

   - Implements a carousel for user-generated content. 

For more information, see in the `Carousel` class documentation. 

###### `lock_swiping` 

If True - disable switching tabs by swipe. 

_`lock_swiping`_ is an `BooleanProperty` and defaults to _False_ . 

- `on_touch_move(` _touch_ `)` _→_ str | bool | None 

Receive a touch move event. The touch is in parent coordinates. 

See `on_touch_down()` for more information. 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.tab.tab.MDTabsItemText(` _*args_ , _**kwargs_ `)` 

Implements an label for the _`MDTabsItem`_ class. 

For more information, see in the _`MDLabel`_ class documentation. 

- Added in version 2.0.0. 

**2.3. Components** 

**137** 

**KivyMD, Release 2.0.1.dev0** 

###### `class kivymd.uix.tab.tab.MDTabsItemIcon(` _*args_ , _**kwargs_ `)` 

Implements an icon for the _`MDTabsItem`_ class. 

For more information, see in the _`MDIcon`_ class documentation. 

Added in version 2.0.0. 

- `class kivymd.uix.tab.tab.MDTabsItem(` _*args_ , _**kwargs_ `)` 

Implements a item with an icon and text for _`MDTabsPrimary`_ class. 

Added in version 2.0.0. 

For more information, see in the `MDTabsItemBase` and `BoxLayout` classes documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### `class kivymd.uix.tab.tab.MDTabsPrimary(` _*args_ , _**kwargs_ `)` 

Tabs primary class. 

Changed in version 2.0.0: Rename from _MDTabs_ to _MDTabsPrimary_ class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and `BoxLayout` classes documentation. 

###### **Events** 

###### **_on_tab_switch_** 

Fired when switching tabs. 

###### `md_bg_color` 

The background color of the widget. 

_`md_bg_color`_ is an `ColorProperty` and defaults to _None_ . 

**Chapter 2. Contents** 

**138** 

**KivyMD, Release 2.0.1.dev0** 

###### `label_only` 

Tabs with a label only or with an icon and a label. 

Added in version 2.0.0. 

_`label_only`_ is an `BooleanProperty` and defaults to _False_ . 

###### `allow_stretch` 

Whether to stretch tabs to the width of the panel. 

_`allow_stretch`_ is an `BooleanProperty` and defaults to _True_ . 

###### `lock_swiping` 

If True - disable switching tabs by swipe. 

_`lock_swiping`_ is an `BooleanProperty` and defaults to _False_ . 

###### `anim_duration` 

Duration of the slide animation. 

_`anim_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `indicator_anim` 

Tab indicator animation. If you want use animation set it to `True` . 

Changed in version 2.0.0: Rename from _tab_indicator_anim_ to _indicator_anim_ attribute. 

_`indicator_anim`_ is an `BooleanProperty` and defaults to _True_ . 

###### `indicator_radius` 

Radius of the tab indicator. 

Added in version 2.0.0. 

_`indicator_radius`_ is an `VariableListProperty` and defaults to _[dp(2), dp(2), 0, 0]_ . 

###### `indicator_height` 

Height of the tab indicator. 

Changed in version 2.0.0: Rename from _tab_indicator_height_ to _indicator_height_ attribute. 

_`indicator_height`_ is an `NumericProperty` and defaults to _‘4dp’_ . 

###### `indicator_duration` 

The duration of the animation of the indicator movement when switching tabs. 

Added in version 2.0.0. 

_`indicator_duration`_ is an `NumericProperty` and defaults to _0.5_ . 

###### `indicator_transition` 

The transition name of animation of the indicator movement when switching tabs. 

Added in version 2.0.0. 

_`indicator_transition`_ is an `StringProperty` and defaults to **`** ’out_expo’. 

###### `last_scroll_x` 

Is the carousel reference of the next tab/slide. When you go from _‘Tab A’_ to _‘Tab B’_ , _‘Tab B’_ will be the target tab/slide of the carousel. 

_`last_scroll_x`_ is an `AliasProperty` . 

**2.3. Components** 

**139** 

**KivyMD, Release 2.0.1.dev0** 

###### `target` 

It is the carousel reference of the next tab / slide. When you go from _‘Tab A’_ to _‘Tab B’_ , _‘Tab B’_ will be the target tab / slide of the carousel. 

_`target`_ is an `ObjectProperty` and default to _None_ . 

```
indicator
```

It is the `SmoothRoundedRectangle` instruction reference of the tab indicator. 

###### _`indicator`_ is an `AliasProperty` . 

```
get_last_scroll_x()
```

```
get_rect_instruction()
```

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`do_autoscroll_tabs(` _instance:_ MDTabsItem, _value: float_ `)` _→_ None 

Automatically scrolls the list of tabs when swiping the carousel slide (related content). 

Changed in version 2.0.0: Rename from _tab_bar_autoscroll_ to _do_autoscroll_tabs_ method. 

`android_animation(` _instance:_ MDTabsCarousel, _offset: float_ `)` _→_ None Fired when swiping a carousel slide (related content). 

`update_indicator(` _x: float = 0.0_ , _w: float = 0.0_ , _instance:_ MDTabsItem _= None_ `)` _→_ None Update position and size of the indicator. 

`switch_tab(` _instance:_ MDTabsItem _= None_ , _text: str = ''_ , _icon: str = ''_ `)` _→_ None Switches tabs by tab object/tab text/tab icon name. 

`set_active_item(` _item:_ MDTabsItem `)` _→_ None 

Sets the active tab item. 

**Chapter 2. Contents** 

**140** 

**KivyMD, Release 2.0.1.dev0** 

###### `get_tabs_list()` _→_ list 

Returns a list of _`MDTabsItem`_ objects. 

Changed in version 2.0.0: Rename from _get_tab_list_ to _get_tabs_list_ method. 

###### `get_slides_list()` _→_ list 

Returns a list of user tab objects. 

Changed in version 2.0.0: Rename from _get_slides_ to _get_slides_list_ method. 

###### `get_current_tab()` _→ MDTabsItem_ 

Returns current tab object. 

Added in version 1.0.0. 

###### `get_current_related_content()` _→_ kivy.uix.widget.Widget 

Returns the carousel slide object (related content). 

Added in version 2.0.0. 

###### `on_tab_switch(` _*args_ `)` _→_ None 

This event is launched every time the current tab is changed. 

###### `on_slide_progress(` _*args_ `)` _→_ None 

This event is deployed every available frame while the tab is scrolling. 

`on_carousel_index(` _instance:_ MDTabsCarousel, _value: int_ `)` _→_ None 

Fired when the Tab index have changed. This event is deployed by the builtin carousel of the class. 

###### `on_size(` _instance_ , _size_ `)` _→_ None 

Fired when the application screen size changes. 

###### `recalculate_tab_widths()` _→_ None 

Recalculates and updates the width of each tab in the tab bar. 

This method ensures that all tabs are evenly distributed across the available horizontal space when _allow_stretch_ is enabled. It is automatically called after a new tab is added. 

If no tabs are present, the method exits without making changes. 

- `class kivymd.uix.tab.tab.MDTabsItemSecondary(` _*args_ , _**kwargs_ `)` 

Implements a item with an icon and text for _`MDTabsSecondary`_ class. 

Added in version 2.0.0. 

For more information, see in the `MDTabsItemBase` and `AnchorLayout` classes documentation. 

###### `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**2.3. Components** 

**141** 

**KivyMD, Release 2.0.1.dev0** 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.tab.tab.MDTabsSecondary(` _*args_ , _**kwargs_ `)` 

Tabs secondary class. 

Added in version 2.0.0. 

For more information, see in the _`MDTabsPrimary`_ class documentation. 

###### `indicator_radius` 

Radius of the tab indicator. 

_`indicator_radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `indicator_height` 

Height of the tab indicator. 

_`indicator_height`_ is an `NumericProperty` and defaults to _‘2dp’_ . 

###### **2.3.20 LoadingIndicator** 

Added in version 2.0.0. 

###### **See also:** 

Material Design spec, Loading indicator Shapes preview 

###### **Loading indicators display the status of a process using continuous or sequential shape animations.** 

- Used to represent indeterminate operations (no fixed end). 

- Each shape is based on Material 3 geometry guidelines. 

- Animations can cycle between multiple predefined shapes. 

**Chapter 2. Contents** 

**142** 

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

Declarative Python style with KV 

```
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:app.theme_cls.surfaceColor
MDLoadingIndicator:
id:indicator
shape_size:dp(100)
'''
classExampleApp(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
#startthemorphinganimation
self.root.ids.indicator.start()
#printavailableshapenames
print(self.root.ids.indicator.get_shape_names())
#optionallystopanimationafter5seconds
#Clock.schedule_once(self.root.ids.indicator.stop,5)
ExampleApp().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.loadingindicatorimportMDLoadingIndicator
classExampleApp(MDApp):
defbuild(self):
returnMDScreen(
MDLoadingIndicator(
id="indicator",
shape_size="100dp",
),
md_bg_color=self.theme_cls.surfaceColor,
)
defon_start(self):
#startthemorphinganimation
```

(continues on next page) 

**2.3. Components** 

**143** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.children[0].start()
#printavailableshapenames
print(self.root.children[0].get_shape_names())
#optionallystopanimationafter5seconds
#Clock.schedule_once(self.root.ids.indicator.stop,5)
ExampleApp().run()
```

###### **API -** `kivymd.uix.loadingindicator.loadingindicator` 

- `class kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicator(` _*args_ , _**kwargs_ `)` 

Implementation of a morphing and rotating loading indicator. 

For more information, see the `AnchorLayout` and `RotateBehavior` classes documentation. 

###### `shape` 

Current shape name displayed by the loading indicator. 

The shape corresponds to one of the predefined shapes available in the `MaterialShape` library. 

You can view all available shape names using _`get_shape_names()`_ . 

_`shape`_ is a `StringProperty` and defaults to _‘cookie12Sided’_ . 

###### `shape_sequence` 

Sequence of shape names through which the indicator cycles. 

Each shape in the list is morphed into the next one over time, looping continuously while the indicator is active. 

_`shape_sequence`_ is a `ListProperty` and defaults to: 

```
[
"cookie12Sided",
"pentagon",
"pill",
"verySunny",
"cookie4Sided",
"oval",
"flower",
"softBoom",
]
```

###### `shape_size` 

Size of the loading indicator. 

_`shape_size`_ is a `NumericProperty` and defaults to _dp(48)_ . 

###### `duration` 

Duration of one morph-and-rotate cycle in seconds. 

This value controls the overall speed of the loading indicator. 

**Chapter 2. Contents** 

**144** 

ae | ) 3 



<!-- Start of picture text -->
“m Amplitude |wes<br><!-- End of picture text -->



<!-- Start of picture text -->
Wavelength<br>$A<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
size_hint_x:.7
pos_hint:{'center_x':.5,'center_y':.5}
amplitude:dp(3)
wave_length:dp(40)
wave_speed:dp(20)
value:30
'''
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.exprogressindicatorimportMDExLinearProgressIndicator
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDExLinearProgressIndicator(
size_hint_x=.7,
amplitude="3dp",
wave_length="40dp",
wave_speed="20dp",
pos_hint={"center_x":.5,"center_y":.5},
value=30,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```



**2.3. Components** 

**147** 

**KivyMD, Release 2.0.1.dev0** 

###### **Circular** 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDExCircularProgressIndicator:
size_hint:None,None
size:"48dp","48dp"
pos_hint:{'center_x':.5,'center_y':.5}
value:30
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.exprogressindicatorimportMDExCircularProgressIndicator
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDExCircularProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
pos_hint={"center_x":.5,"center_y":.5},
value=30,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**148** 

**KivyMD, Release 2.0.1.dev0** 



###### **Determinate and indeterminate modes** 

Both linear and circular indicators support determinate and indeterminate variants. Set _`MDExBaseProgressBar. determinate`_ to toggle modes. 

###### **Determinate with animated progress** 

To improve the visual flow of your progress bars, favor the `easing_emphasized` transition over linear movement when using `kivy.animation.Animation` . 

Declarative Python style with KV 

```
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDExLinearProgressIndicator:
id:progress
size_hint_x:.7
determinate:True
pos_hint:{'center_x':.5,'center_y':.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_start(self,*_):
anim=Animation(
value=100,
d=1.6,
t="easing_emphasized",
)
anim.start(self.root.ids.progress)
Example().run()
```

**2.3. Components** 

**149** 

**KivyMD, Release 2.0.1.dev0** 

Declarative Python style 

```
fromkivy.animationimportAnimation
fromkivymd.appimportMDApp
fromkivymd.uix.exprogressindicatorimportMDExLinearProgressIndicator
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnMDScreen(
MDExLinearProgressIndicator(
id="progress",
size_hint_x=0.7,
determinate=True,
pos_hint={"center_x":0.5,"center_y":0.5},
),
md_bg_color=self.theme_cls.backgroundColor,
)
defon_start(self):
anim=Animation(
value=100,
d=1.6,
t="easing_emphasized",
)
anim.start(self.root.get_ids().progress)
Example().run()
```

###### **Indeterminate animation modes** 

###### **Linear indeterminate modes** 

- `contiguous` : a single bar that flows continuously across the track. 

- `discontinuous` : two separate bars with gaps between them. 

Set the mode with _`MDExLinearProgressIndicator.indeterminate_animator`_ . 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
```

(continues on next page) 

**Chapter 2. Contents** 

**150** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
MDExLinearProgressIndicator:
size_hint:None,None
size:"48dp","48dp"
pos_hint:{"center_x":.5,"center_y":.5}
determinate:False
indeterminate_animator:"contiguous"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.exprogressindicatorimportMDExLinearProgressIndicator
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDExLinearProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
pos_hint={"center_x":.5,"center_y":.5},
determinate=False,
indeterminate_animator="contiguous",
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
```

(continues on next page) 

**2.3. Components** 

**151** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
MDExLinearProgressIndicator:
size_hint:None,None
size:"48dp","48dp"
pos_hint:{"center_x":.5,"center_y":.5}
determinate:False
indeterminate_animator:"discontinuous"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

###### Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.exprogressindicatorimportMDExLinearProgressIndicator
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDExLinearProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
pos_hint={"center_x":.5,"center_y":.5},
determinate=False,
indeterminate_animator="discontinuous",
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**152** 

**KivyMD, Release 2.0.1.dev0** 

###### **Circular indeterminate modes** 

- `advanced` : multi-phase expansion/collapse with smooth color transitions. 

- `retreat` : a single arc that grows and shrinks with rotating emphasis. 

Set the mode with _`MDExCircularProgressIndicator.indeterminate_animator`_ . 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDExCircularProgressIndicator:
size_hint:None,None
size:[dp(50)]*2
pos_hint:{'center_x':.5,'center_y':.5}
indeterminate_animator:"advanced"
determinate:False
wave_length:0
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.exprogressindicatorimportMDExCircularProgressIndicator
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDExCircularProgressIndicator(
size_hint=(None,None),
size=[dp(50)]*2,
pos_hint={'center_x':.5,'center_y':.5},
indeterminate_animator="advanced",
```

(continues on next page) 

**2.3. Components** 

**153** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
determinate=False,
wave_length=0,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDExCircularProgressIndicator:
size_hint:None,None
size:[dp(50)]*2
pos_hint:{'center_x':.5,'center_y':.5}
indeterminate_animator:"retreat"
determinate:False
wave_length:dp(12)
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.exprogressindicatorimportMDExCircularProgressIndicator
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
```

(continues on next page) 

**Chapter 2. Contents** 

**154** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDScreen(
MDExCircularProgressIndicator(
size_hint=(None,None),
size=[dp(50)]*2,
pos_hint={'center_x':.5,'center_y':.5},
indeterminate_animator="retreat",
determinate=False,
wave_length=dp(12),
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Note:** A comprehensive interactive demo is available in `examples/exprogressindicator.py` . 

###### **API -** `kivymd.uix.exprogressindicator.exprogressindicator` 

`class kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar(` _**kwargs_ `)` 

Base class for extended progress indicators. 

Handles shared properties, frame context caching, and wave rendering hooks used by both linear and circular indicators. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and classes documentation. 

###### `value` 

Current value used for the slider. 

_`value`_ is an `AliasProperty` that returns the value of the progress bar. If the value is < 0 or > _`max`_ , it will be normalized to those boundaries. 

###### `value_normalized` 

Normalized value inside the range 0-1: 

```
>>>pb=ProgressBar(value=50,max=100)
>>>pb.value
50
>>>pb.value_normalized
0.5
```

_`value_normalized`_ is an `AliasProperty` . 

###### `max` 

Maximum value allowed for _`value`_ . 

_`max`_ is a `NumericProperty` and defaults to 100. 

**2.3. Components** 

**155** 

**KivyMD, Release 2.0.1.dev0** 

###### `active_track_color` 

Color of active track 

_`active_track_color`_ is a `ColorProperty` and defaults to None. 

###### `inactive_track_color` 

Color of inactive track 

_`inactive_track_color`_ is a `ColorProperty` and defaults to None. 

###### `thickness` 

Thickness of tracks 

_`thickness`_ is an `NumericProperty` and defaults to _dp(4)_ . 

###### `spacing` 

Spacing between tracks/segments. 

_`spacing`_ is an `NumericProperty` and defaults to _dp(4)_ . 

###### `amplitude` 

Amplitude of the wave effect. 

_`amplitude`_ is an `NumericProperty` and defaults to _dp(3)_ . 

###### `wave_speed` 

Speed of the wave effect. 

_`wave_speed`_ is an `NumericProperty` and defaults to _-dp(40)_ per second. 

###### `wave_length` 

Wavelength of the wave effect. 

_`wave_length`_ is an `NumericProperty` and defaults to _dp(40)_ . 

###### `determinate` 

Switch between determinate and indeterminate modes. 

_`determinate`_ is an `BooleanProperty` and defaults to _False_ . 

###### `color_array` 

List of RGBA colors used by indeterminate animations. 

_`color_array`_ is an `ListProperty` and defaults to three RGBA colors. 

###### `get_norm_value()` 

`set_norm_value(` _value_ `)` 

`color_obj(` _line_name_ `)` 

Get color object from line. 

```
reset_colors()
```

`refresh_lines(` _line_list_ `)` 

Clears points and returns a reusable queue. 

`setup_lines(` _*args_ `)` 

init line objs 

```
render_determinate_wave()
```

**Chapter 2. Contents** 

**156** 

**KivyMD, Release 2.0.1.dev0** 

###### `render_indeterminate_wave()` 

###### `save_frame_context(` _*args_ `)` 

###### `on_determinate(` _instance_ , _value_ `)` 

###### `get_amplitude(` _A_ , _t_ `)` 

fade in/out for amplitude using quadratic easing. 

- `class kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicator(` _**kwargs_ `)` Implementation of the linear progress indicator. 

For more information, see in the `MDExBaseProgressBar` and classes documentation. 

###### `orientation` 

Orientation of progressbar. Available options are: _‘horizontal ‘_ , _‘vertical’_ . 

_`orientation`_ is an `OptionProperty` and defaults to _‘horizontal’_ . 

###### `indeterminate_animator` 

Name of the indeterminate animator to use for linear mode. Available options are: _‘contiguous’_ , _‘discontinuous’_ . 

_`indeterminate_animator`_ is a `StringProperty` and defaults to _‘discontinuous’_ . 

###### `save_frame_context(` _*args_ `)` 

Pre-calculate geometry and spacing factors for the current frame. 

- `on_color_array(` _instance_ , _value_ `)` 

###### `on_indeterminate_animator(` _instance_ , _value_ `)` 

###### `on_orientation(` _*args_ `)` 

- `w_seg(` _start_ , _end_ `)` _→_ list 

High-performance wave point generator. 

`cleanup_lines(` _line_groups_ `)` 

###### `compute_inactive_segments(` _active_bars_ `)` 

###### `render_determinate_wave()` 

- `get_segment_coords(` _s_f_ , _e_f_ , _do_fade=True_ `)` 

Calculates points ensuring consistent visual gaps. 

###### `render_discts_wave()` 

###### `render_cont_wave()` 

###### `render_indeterminate_wave()` 

- `class kivymd.uix.exprogressindicator.exprogressindicator.MDExCircularProgressIndicator(` _**kwargs_ `)` Implementation of the circular progress indicator. 

For more information, see in the `MDExBaseProgressBar` and classes documentation. 

###### `indeterminate_animator` 

Name of the indeterminate animator to use for circular mode. Available options are: _‘advanced’_ , _‘retreat’_ . 

_`indeterminate_animator`_ is a `StringProperty` and defaults to _‘retreat’_ . 

**2.3. Components** 

**157** 



<!-- Start of picture text -->
ORDER NAME occupation conract EDUCATION<br>9841 Sampson Murphy Mobile Dev 4013521125 0192 Senior High veTans<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.datatables.datatables` 

`class kivymd.uix.datatables.datatables.MDDataTable(` _**kwargs_ `)` 

Datatable class. 

For more information, see in the _`ThemableBehavior`_ and `AnchorLayout` classes documentation. 

###### **Events** 

```
on_row_press
```

Called when a table row is clicked. 

```
on_check_press
```

Called when the check box in the table row is checked. 

###### **Use events as follows** 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.data_tables=MDDataTable(
use_pagination=True,
check=True,
column_data=[
("No.",dp(30)),
("Status",dp(30)),
("SignalName",dp(60),self.sort_on_signal),
("Severity",dp(30)),
("Stage",dp(30)),
("Schedule",dp(30),self.sort_on_schedule),
("TeamLead",dp(30),self.sort_on_team),
],
row_data=[
(
"1",
("alert",[255/256,165/256,0,1],"NoSignal"),
"Astrid:NEsharedmanaged",
"Medium",
"Triaged",
"0:33",
"ChaseNguyen",
),
(
"2",
("alert-circle",[1,0,0,1],"Offline"),
"Cosmo:prodsharedares",
"Huge",
"Triaged",
```

(continues on next page) 

**2.3. Components** 

**159** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
"0:39",
"BrieFurman",
),
(
"3",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Phoenix:prodsharedlyra-lists",
"Minor",
"NotTriaged",
"3:12",
"Jeremylake",
),
(
"4",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Sirius:NWprodsharedlocations",
"Negligible",
"Triaged",
"13:18",
"AngelicaHowards",
),
(
"5",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Sirius:prodindependentaccount",
"Negligible",
"Triaged",
"22:06",
"DianeOkuma",
),
],
sorted_on="Schedule",
sorted_order="ASC",
elevation=2,
)
self.data_tables.bind(on_row_press=self.on_row_press)
self.data_tables.bind(on_check_press=self.on_check_press)
screen=MDScreen()
screen.add_widget(self.data_tables)
returnscreen
```

(continues on next page) 

**Chapter 2. Contents** 

**160** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defon_row_press(self,instance_table,instance_row):
'''Calledwhenatablerowisclicked.'''
print(instance_table,instance_row)
defon_check_press(self,instance_table,current_row):
'''Calledwhenthecheckboxinthetablerowischecked.'''
print(instance_table,current_row)
#SortingMethods:
#sincethehttps://github.com/kivymd/KivyMD/pull/914request,the
#sortingmethodrequiresyoutosortouttheindexesofeachdatavalue
#forthesupportofselections.
#
#Themostcommonmethodtodothisiswiththeuseofthebuiltinfunction
#zipandenumerate,seetheexamplebelowformoreinfo.
#
#Theresultgivenbythesefuncitonsmustbealistintheformatof
#[Indexes,Sorted_Row_Data]
defsort_on_signal(self,data):
returnzip(*sorted(enumerate(data),key=lambdal:l[1][2]))
defsort_on_schedule(self,data):
returnzip(
*sorted(
enumerate(data),
key=lambdal:sum(
[
int(l[1][-2].split(":")[0])*60,
int(l[1][-2].split(":")[1]),
]
),
)
)
defsort_on_team(self,data):
returnzip(*sorted(enumerate(data),key=lambdal:l[1][-1]))
Example().run()
```

```
column_data
```

Data for header columns. 

Imperative python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
```

(continues on next page) 

**2.3. Components** 

**161** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`from kivymd.uix.datatables import MDDataTable from kivy.uix.anchorlayout import AnchorLayout class Example(MDApp): def build(self): self.theme_cls.theme_style = "Dark" self.theme_cls.primary_palette = "Orange" layout = AnchorLayout() self.data_tables = MDDataTable( size_hint=(0.7, 0.6), use_pagination=True, check=True,` _`# name column, width column, sorting function column(optional),`_ `␣` _˓→_ _`custom tooltip`_ `column_data=[ ("No.", dp(30), None, "Custom tooltip"), ("Status", dp(30)), ("Signal Name", dp(60)), ("Severity", dp(30)), ("Stage", dp(30)), ("Schedule", dp(30), lambda *args: print("Sorted using Schedule "` _˓→_ `)), ("Team Lead", dp(30)), ], ) layout.add_widget(self.data_tables) return layout Example().run()` 

Declarative python style 

`from kivy.metrics import dp from kivymd.app import MDApp from kivymd.uix.anchorlayout import MDAnchorLayout from kivymd.uix.datatables import MDDataTable class Example(MDApp): def build(self): self.theme_cls.theme_style = "Dark" self.theme_cls.primary_palette = "Orange" return MDAnchorLayout( MDDataTable( size_hint=(0.7, 0.6), use_pagination=True, check=True,` _`# name column, width column, sorting function column(optional)`_ (continues on next page) 

**Chapter 2. Contents** 

**162** 





<!-- Start of picture text -->
[] No. Status Signal Name Severity Stage<br>Rowsperpage 0 4 1-5 0f 0 < ><br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
"Offline",
"Cosmo:prodsharedares",
"Huge",
"Triaged",
"0:39",
"BrieFurman",
],
[
"3",
"Online",
"Phoenix:prodsharedlyra-lists",
"Minor",
"NotTriaged",
"3:12",
"Jeremylake",
],
[
"4",
"Online",
"Sirius:NWprodsharedlocations",
"Negligible",
"Triaged",
"13:18",
"AngelicaHowards",
],
[
"5",
"Online",
"Sirius:prodindependentaccount",
"Negligible",
"Triaged",
"22:06",
"DianeOkuma",
],
]
```

You must sort inner lists in ascending order and return the sorted data in the same format. 

###### `row_data` 

Data for rows. To add icon in addition to a row data, include a tuple with This property stores the row data used to display each row in the DataTable To show an icon inside a column in a row, use the folowing format in the row’s columns. 

Format: 

_(“MDicon-name”, [icon color in rgba], “Column Value”)_ 

Example: 

```
[...]
row_data=[
#row1
```

(continues on next page) 

**Chapter 2. Contents** 

**164** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
[
"value1",
"value2",
#thethirdvaluewillhaveaniconinsidethebox
["home",[128/255,48/255,76/255,1],"Offie"]
],
#row2
[
"value1",
"value2",
#thethirdvaluewillhaveaniconinsidethebox
["git",[1,0.1,0.1,1],"GitRepo"]
]
]
```

For a more complex example see below. 

`from kivy.metrics import dp from kivy.uix.anchorlayout import AnchorLayout from kivymd.app import MDApp from kivymd.uix.datatables import MDDataTable class Example(MDApp): def build(self): self.theme_cls.theme_style = "Dark" self.theme_cls.primary_palette = "Orange" layout = AnchorLayout() data_tables = MDDataTable( size_hint=(0.9, 0.6), column_data=[ ("Column 1", dp(30)), ("Column 2", dp(30)), ("Column 3", dp(50), self.sort_on_col_3), ("Column 4", dp(30)), ("Column 5", dp(30)), ("Column 6", dp(30)), ("Column 7", dp(30), self.sort_on_col_2), ], row_data=[` _`# The number of elements must match the length # of the`  column_data`  list.`_ `( "1", ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"), "Astrid: NE shared managed", "Medium", "Triaged", "0:33",` (continues on next page) 

**2.3. Components** 

**165** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
"ChaseNguyen",
),
(
"2",
("alert-circle",[1,0,0,1],"Offline"),
"Cosmo:prodsharedares",
"Huge",
"Triaged",
"0:39",
"BrieFurman",
),
(
"3",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Phoenix:prodsharedlyra-lists",
"Minor",
"NotTriaged",
"3:12",
"Jeremylake",
),
(
"4",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Sirius:NWprodsharedlocations",
"Negligible",
"Triaged",
"13:18",
"AngelicaHowards",
),
(
"5",
(
"checkbox-marked-circle",
[39/256,174/256,96/256,1],
"Online",
),
"Sirius:prodindependentaccount",
"Negligible",
"Triaged",
"22:06",
"DianeOkuma",
),
```

```
],
)
```

(continues on next page) 

**Chapter 2. Contents** 

**166** 



Column 1 Column 2 Column 3 Column 4 Column 5 Column 6 1 A No Signal Astrid: NE shared managed Medium Triaged 0:33 2 Offline Cosmo: prod shared ares Huge Triaged 0:39 3 Online Phoenix: prod shared lyra-lists Minor Not Triaged 3:12 4 Online Sirius: NW prod shared locations Negligible Triaged 13:18 5 Online Sirius: prod independent account Negligible Triaged 22:06 



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text="Chip"
),
]
classMyMDButton(MDButton):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDButtonText(
text="Button"
)
]
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
```

```
layout=AnchorLayout()
```

```
defon_activate(row_index:int,row_data:list)->None:
'''
```

```
Callbackfunctionfortheswitchwidgetinthetablerow.
```

```
CalledwhentheMDSwitchinatablerowistoggled.
```

```
:paramrow_index:Indexoftherowinthetable(0-based)
:paramrow_data:Listofdatavaluesfortherow(allcolumns)
Example:
```

`When a switch is toggled in the "Status" column: >>> on_activate(0, ['1', 'John Doe', {'viewclass': 'MDSwitch', .` _˓→_ `..}]) Activate row 0: ['1', 'John Doe', {'viewclass': 'MDSwitch', ...}` _˓→_ `] '''` 

`print(f"Activate row {row_index}: {row_data}") def on_press(row_index: int, row_data: list) -> None: ''' Callback function for button widgets in the table row. Called when a button (e.g., MyMDButton) in a table row is pressed/` _˓→_ `released. ''' print(f"Press button {row_index}: {row_data}") def on_release(row_index: int, row_data: list) -> None: '''` 

(continues on next page) 

**Chapter 2. Contents** 

**168** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`Callback function for check widgets in the table row. Called when a button (e.g., MyMDChip) in a table row is pressed/` _˓→_ `released. ''' print(f"Press check {row_index}: {row_data}") data_tables = MDDataTable( size_hint=(0.95, 0.8), use_pagination=True, rows_num=5, check=True, column_data=[ ("ID", dp(40)), ("Name", dp(40)), ("Status", dp(40)), ], row_data=[ ( "1", "John Doe", {"viewclass": "MyMDButton", "on_press": on_press}, ), ( "2", "Jane Smith", {"viewclass": "MDSwitch", "on_active": on_activate}, ), ( "3", "Nicol Andersson", {"viewclass": "MyMDChip", "on_release": on_release}, ), ] ) layout.add_widget(data_tables) return layout if __name__ == "__main__": Example().run()` 

**2.3. Components** 

**169** 



<!-- Start of picture text -->
ID Name Status<br>1 John Doe Button<br>2 Jane Smith . @<br>3 Nicol Andersson Chip<br>Rows per page 3 & 1-50f3<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classMyMDButton(MDButton):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDButtonText(
text="Button"
)
]
```

```
classExample(MDApp):
```

```
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
```

```
layout=AnchorLayout()
```

```
defon_activate(row_index:int,row_data:list)->None:
print(f"Activaterow{row_index}:{row_data}")
```

```
defon_press(row_index:int,row_data:list)->None:
print(f"Pressbutton{row_index}:{row_data}")
```

```
defon_release(row_index:int,row_data:list)->None:
print(f"Releasechip{row_index}:{row_data}")
```

```
defon_edit(row_index:int,row_data:list)->None:
print(f"Editrow{row_index}:{row_data}")
```

```
defon_delete(row_index:int,row_data:list)->None:
print(f"Deleterow{row_index}:{row_data}")
```

```
defon_view(row_index:int,row_data:list)->None:
print(f"Viewrow{row_index}:{row_data}")
```

```
data_tables=MDDataTable(
size_hint=(0.95,0.8),
use_pagination=True,
rows_num=5,
check=True,
column_data=[
("ID",dp(30)),
("Name",dp(40)),
("Status",dp(40)),
("Actions",dp(40)),
],
row_data=[
(
"1",
"JohnDoe",
```

(continues on next page) 

**2.3. Components** 

**171** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
{"viewclass":"MyMDButton","on_press":on_press},
{
"viewclass":"MDBoxLayout",
"spacing":dp(4),
"children":[
{
"viewclass":"MDIconButton",
"icon":"eye",
"on_release":on_view,
},
{
"viewclass":"MDIconButton",
"icon":"pencil",
"on_release":on_edit,
},
{
"viewclass":"MDIconButton",
"icon":"delete",
"on_release":on_delete,
},
]
},
),
(
"2",
"JaneSmith",
{"viewclass":"MDSwitch","on_active":on_activate},
{
"viewclass":"MDBoxLayout",
"spacing":dp(4),
"children":[
{
"viewclass":"MDIconButton",
"icon":"eye",
"on_release":on_view,
},
{
"viewclass":"MDIconButton",
"icon":"pencil",
"on_release":on_edit,
},
{
"viewclass":"MDIconButton",
"icon":"delete",
"on_release":on_delete,
},
]
},
),
(
"3",
"NicolAndersson",
```

(continues on next page) 

**Chapter 2. Contents** 

**172** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`{"viewclass": "MyMDChip", "text": "Delete", "on_release":␣` _˓→_ `on_release}, { "viewclass": "MDBoxLayout", "spacing": dp(4), "children": [ { "viewclass": "MDIconButton", "icon": "eye", "on_release": on_view, }, { "viewclass": "MDIconButton", "icon": "pencil", "on_release": on_edit, }, { "viewclass": "MDIconButton", "icon": "delete", "on_release": on_delete, }, ] }, ), ( "4", "Alice Brown", { "viewclass": "MDBoxLayout", "spacing": dp(4), "children": [ { "viewclass": "MyMDChip", "text": "Active", }, { "viewclass": "MDIconButton", "icon": "information", "on_release": on_view, }, ] }, { "viewclass": "MDBoxLayout", "spacing": dp(4), "children": [ { "viewclass": "MDIconButton", "icon": "pencil", "on_release": on_edit, }, {` 

(continues on next page) 

**2.3. Components** 

**173** 

**KivyMD, Release 2.0.1.dev0** 



<!-- Start of picture text -->
(continued from previous page)<br>"viewclass": "MDIconButton",<br>"icon": "delete",<br>"on_release": on_delete,<br>},<br>]<br>},<br>),<br>(<br>"5",<br>"Bob Johnson",<br>{<br>"viewclass": "MDBoxLayout",<br>"spacing": dp(4),<br>"children": [<br>{<br>"viewclass": "MyMDChip",<br>"text": "Pending",<br>},<br>{<br>"viewclass": "MDIconButton",<br>"icon": "information",<br>"on_release": on_view,<br>},<br>]<br>},<br>{<br>"viewclass": "MDBoxLayout",<br>"spacing": dp(4),<br>"children": [<br>{<br>"viewclass": "MDIconButton",<br>"icon": "pencil",<br>"on_release": on_edit,<br>},<br>{<br>"viewclass": "MDIconButton",<br>"icon": "delete",<br>"on_release": on_delete,<br>},<br>]<br>},<br>),<br>]<br>)<br><!-- End of picture text -->

```
layout.add_widget(data_tables)
returnlayout
if__name__=="__main__":
Example().run()
```

**Chapter 2. Contents** 

**174** 



<!-- Start of picture text -->
ID Name Status Actions<br>1 John Doe Button Oo 47. —8<br>2 Jane Smith. Oo 47° —58<br>3 Nicol. Andersson Delete © 47° —_—<br>4 Alice. Brown Active | @ 4° —_os<br>5 Bob Johnson a 4. —G6<br>Rows per page 5 & 1-50f5<br><!-- End of picture text -->



<!-- Start of picture text -->
(}  Column1 Column 2 Column 3 Column 4 Column 5 Column 6<br>1 A No Signal Astrid: NE shared managed Medium Triaged 0:33<br>2 Offline Cosmo: prod shared ares Huge Triaged 0:39<br>3 Online Phoenix: prod shared lyra-lists Minor Not Triaged 3:12<br>4 Online Sirius: NW prod shared locations Negligible Triaged 13:18<br>5 Online Sirius: prod independent account Negligible Triaged 22:06<br><!-- End of picture text -->





<!-- Start of picture text -->
No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112<br>21 2 3 4 5<br>312<br>41 2 3 4 5<br>5 1 2 3 4 5<br>Rowsperpage 5 4 1-50 of 50 < ><br><!-- End of picture text -->

|No.<br>Column 1|Column 2|Column 3|Column 4|Column 5|
|---|---|---|---|---|
||||||
|1|2|3|4|5|
||||||
|1|2|3|4|5|
|5<br>1|2|3|4|5|
||||Rowsperpage<br>5<br>4|1-50of50<br><<br>>|





<!-- Start of picture text -->
No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112345<br>21 2 3 4 5<br>4] 1 2 3 4 5)<br>5<br>4 1 2 3 4 )<br>10<br>5 1 2 3 4 5<br>Rowsperpage 15 4 1-15 of 50 < ><br><!-- End of picture text -->



<!-- Start of picture text -->
No. Column 1 Column 2 Column 3 Column 4 Column 5<br>1123“S<br>21 2 3 4 5<br>3 1 2 3 4<br>5<br>4 1 2 3 4<br>10<br>5 1 2 3 4<br>Rowsperpage 5 4 1-50 of 50 < ><br><!-- End of picture text -->



<!-- Start of picture text -->
No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112345<br>21 2 3 4 5<br>S| 1 2 3 4 5<br>412345<br>51 2 3 4 5<br>Rowsperpage 5 LTA < ><br>5<br>10<br>No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112345<br>5<br>21 2 3 4 5<br>10<br>3 1 2 3 4 5<br>15<br>4 1 2 3 4 5<br>20<br>5 1 2 3 4 5<br>Rowsperpage 5 4 1-50 of 50 < ><br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Use markup strings** 

```
fromkivy.metricsimportdp
fromkivy.uix.anchorlayoutimportAnchorLayout
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
layout=AnchorLayout()
data_tables=MDDataTable(
size_hint=(0.9,0.6),
use_pagination=True,
column_data=[
("No.",dp(30)),
("Column1",dp(30)),
("[color=#52251B]Column2[/color]",dp(30)),
("Column3",dp(30)),
("[size=24][color=#C042B8]Column4[/color][/size]",dp(30)),
("Column5",dp(30)),
],
row_data=[
(
f"{i+1}",
"[color=#297B50]1[/color]",
"[color=#C552A1]2[/color]",
"[color=#6C9331]3[/color]",
"4",
"5",
)
foriinrange(50)
],
)
layout.add_widget(data_tables)
returnlayout
Example().run()
```

**2.3. Components** 

**179** 



<!-- Start of picture text -->
No. Column 1 Column 3 Column 5<br>145<br>24 5<br>345<br>44 5<br>5 4 5<br>Rowsperpage 5 4 1-50 of 50 < ><br>No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112345<br>21 2 3 4 5<br>312345<br>41 2 3 4 5<br>5 1 2 3 4 5<br>Rowsperpage 5 4 1-50 of 50 < ><br><!-- End of picture text -->





<!-- Start of picture text -->
No. Column 1 Column 2 Column 3 Column 4 Column 5<br>112345<br>21 2 3 4 5<br>312345<br>41 2 3 4 5<br>5 1 2 3 4 5<br>Rowsperpage 5 4 1-50 of 50 ><br>No. Column 1 Column 2 Column 3 Column 4 Column 5<br>1 1 2 3] 4 5<br>212345<br>31 2 3 4 5<br>412345<br>51 2 3 4 5<br>Rowsperpage 5 4 1-50 of 50 ><br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

Added in version 2.0.0. 

###### **Parameters** 

- `row_index` – Row index in _row_data_ 

- `checked` – True - check the row, False - uncheck the row 

```
fromkivy.metricsimportdp
fromkivy.langimportBuilder
fromkivy.propertiesimportObjectProperty
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.anchorlayoutimportMDAnchorLayout
KV='''
<TableScreen>
tablebox:tablebox
md_bg_color:self.theme_cls.backgroundColor
MainCard:
pos_hint:{"center_x":.5,"center_y":.55}
TableBox:
id:tablebox
MDButton:
pos_hint:{"center_x":.5,"center_y":.1}
on_press:root.check_row_0()
MDButtonText:
text:"Checkrow0"
<TableBox>
<MainCard>
size_hint:None,None
size:"400dp","450dp"
pos_hint:{"center_x":.5,"center_y":.5}
elevation:3
padding:"10dp"
spacing:"25dp"
'''
Builder.load_string(KV)
classMainCard(MDScreen):...
classTableBox(MDAnchorLayout):
```

(continues on next page) 

**Chapter 2. Contents** 

**182** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
table:MDDataTable
```

```
defadd_table(
self,
column_fields,
table_data,
refresh=False,
use_pagination=True,
use_check=True,
rows_num=10,
):
ifrefresh:
self.clear_widgets()
data_table=MDDataTable(
use_pagination=use_pagination,
check=use_check,
rows_num=rows_num,
column_data=column_fields,
row_data=table_data,
)
self.table=data_table
self.add_widget(data_table)
```

```
classTableScreen(MDScreen):
tablebox=ObjectProperty(None)
```

```
def__init__(self,**kwargs):
super().__init__(**kwargs)
col_fields=["field1","field2"]
col_data=[(f,dp(30))forfincol_fields]
table_data=[(f"col1_{i}",f"col2_{i}")foriinrange(30)]
self.tablebox.add_table(col_data,table_data)
defcheck_row_0(self):
'''Selectthecheckboxforrow0.'''
self.tablebox.table.set_row_checked(0,True)
```

```
classMainApp(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnTableScreen()
if__name__=="__main__":
MainApp().run()
```

**2.3. Components** 

**183** 

**KivyMD, Release 2.0.1.dev0** 

You can select multiple rows at once: 

```
defcheck_row_0_4(self):
'''Selectthecheckboxforrow0-4.'''
self.tablebox.table.set_rows_checked([0,1,2,3,4],True)
```

Or toggle the selected row: 

```
deftoggle_row_5(self):
'''Togglethecheckboxforrow5.'''
self.tablebox.table.toggle_row_checked(5)
```

`set_rows_checked(` _row_indices: list_ , _checked: bool_ `)` _→_ None 

Sets the checkbox state for multiple rows. 

Added in version 2.0.0. 

###### **Parameters** 

- `row_indices` – List of row indices in _row_data_ 

- `checked` – True - check the rows, False - uncheck the rows 

`set_all_rows_checked(` _checked: bool_ `)` _→_ None 

Sets the state of all checkboxes in the table. 

###### **Parameters** 

`checked` – True - check all rows, False - uncheck all rows 

`toggle_row_checked(` _row_index: int_ `)` _→_ None 

Toggles the checkbox state for a specific row. 

Added in version 2.0.0. 

###### **Parameters** 

`row_index` – Row index in _row_data_ 

`is_row_checked(` _row_index: int_ `)` _→_ bool 

Checks if a specific row is checked. 

Added in version 2.0.0. 

###### **Parameters** 

`row_index` – Row index in _row_data_ 

###### **Returns** 

True if the row is checked, False otherwise 

`get_checked_row_indices()` _→_ list 

Returns a list of indices of all checked rows. 

###### **Returns** 

List of checked row indices 

`clear_all_checks()` _→_ None 

Unchecks all rows in the table. 

**Chapter 2. Contents** 

**184** 

**KivyMD, Release 2.0.1.dev0** 

###### `check_all_rows()` _→_ None 

Checks all rows in the table. 

`update_row_data(` _instance_data_table_ , _data: list_ `)` _→_ None 

Called when a the widget data must be updated. 

Remember that this is a heavy function. since the whole data set must be updated. you can get better results calling this metod with in a coroutine. 

- `add_row(` _data: list | tuple_ `)` _→_ None 

Added new row to common table. Argument _data_ is the row data from the list _`row_data`_ . 

###### **Add/remove row** 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.buttonimportMDButton
fromkivymd.uix.buttonimportMDButtonText
```

```
classExample(MDApp):
data_tables=None
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
layout=MDFloatLayout()#rootlayout
#Creatingcontrolbuttons.
button_box=MDBoxLayout(
pos_hint={"center_x":0.5},
adaptive_size=True,
padding="24dp",
spacing="24dp",
)
forbutton_textin["Addrow","Removerow"]:
button_box.add_widget(
MDButton(
MDButtonText(
text=button_text
),
on_release=lambdax,y=button_text:self.on_button_press(y)
)
)
#Createatable.
self.data_tables=MDDataTable(
pos_hint={"center_y":0.5,"center_x":0.5},
```

(continues on next page) 

**2.3. Components** 

**185** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `size_hint=(0.9, 0.6), use_pagination=False, column_data=[ ("No.", dp(30)), ("Column 1", dp(40)), ("Column 2", dp(40)), ("Column 3", dp(40)), ], row_data=[("1", "1", "2", "3")], )` _`# Adding a table and buttons to the toot layout.`_ `layout.add_widget(self.data_tables) layout.add_widget(button_box) return layout def on_button_press(self, button_text: str) -> None: '''Called when a control button is clicked.''' try: { "Add row": self.add_row, "Remove row": self.remove_row, }[button_text]() except KeyError: pass def add_row(self) -> None: last_num_row = int(self.data_tables.row_data[-1][0]) self.data_tables.add_row((str(last_num_row + 1), "1", "2", "3")) def remove_row(self) -> None: if len(self.data_tables.row_data) > 1: self.data_tables.remove_row(self.data_tables.row_data[-1]) Example().run()` 

###### **Deleting checked rows** 

```
fromkivy.metricsimportdp
fromkivy.langimportBuilder
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
fromkivymd.uix.screenimportMDScreen
KV='''
```

(continues on next page) 

**Chapter 2. Contents** 

**186** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDBoxLayout:
orientation:"vertical"
padding:"56dp"
spacing:"24dp"
MDData:
id:table_screen
MDButton:
on_release:table_screen.delete_checked_rows()
MDButtonText:
text:"DELETECHECKEDROWS"
'''
classMDData(MDScreen):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.data=[
["1","AsepSudrajat","Male","Soccer"],
["2","Egy","Male","Soccer"],
["3","Tanos","Demon","Soccer"],
]
self.data_tables=MDDataTable(
use_pagination=True,
check=True,
column_data=[
("No",dp(30)),
("NoUrut.",dp(30)),
("AlamatPengirim",dp(30)),
("NoSurat",dp(60)),
]
)
self.data_tables.row_data=self.data
self.add_widget(self.data_tables)
defdelete_checked_rows(self):
defdeselect_rows(*args):
self.data_tables.table_data.select_all("normal")
fordatainself.data_tables.get_row_checks():
self.data_tables.remove_row(data)
```

```
Clock.schedule_once(deselect_rows)
```

```
classMyApp(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
returnBuilder.load_string(KV)
```

(continues on next page) 

**2.3. Components** 

**187** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MyApp().run()
```

Added in version 1.0.0. 

- `remove_row(` _data: list | tuple_ `)` _→_ None 

Removed row from common table. Argument _data_ is the row data from the list _`row_data`_ . 

See the code in the doc string for the _`add_row`_ method for more information. 

Added in version 1.0.0. 

- `update_row(` _old_data: list | tuple_ , _new_data: list | tuple_ `)` _→_ None 

Updates a table row. Argument _old_data/new_data_ is the row data from the list _`row_data`_ . 

###### **Update row** 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.datatablesimportMDDataTable
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.buttonimportMDButton,MDButtonText
```

```
classExample(MDApp):
data_tables=None
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
layout=MDFloatLayout()
layout.add_widget(
MDButton(
MDButtonText(
text="Change2row"
),
pos_hint={"center_x":0.5},
on_release=self.update_row,
y=24,
)
)
self.data_tables=MDDataTable(
pos_hint={"center_y":0.5,"center_x":0.5},
size_hint=(0.9,0.6),
use_pagination=False,
column_data=[
("No.",dp(30)),
("Column1",dp(40)),
```

(continues on next page) 

**Chapter 2. Contents** 

**188** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `("Column 2", dp(40)), ("Column 3", dp(40)), ], row_data=[(f"{i + 1}", "1", "2", "3") for i in range(3)], ) layout.add_widget(self.data_tables) return layout def update_row(self, instance_button: MDButton) -> None: self.data_tables.update_row( self.data_tables.row_data[1],` _`# old row data`_ `["2", "A", "B", "C"],` _`# new row data`_ `) Example().run()` 

Added in version 1.0.0. 

`on_row_press(` _instance_cell_row_ `)` _→_ None Called when a table row is clicked. 

`on_check_press(` _row_data: list_ `)` _→_ None 

Called when the check box in the table row is checked. 

###### **Parameters** 

`row_data` – One of the elements from the _`MDDataTable.row_data`_ list. 

`get_row_checks()` _→_ list 

Returns all rows that are checked. 

`create_pagination_menu(` _interval: int | float_ `)` _→_ None 

**2.3. Components** 

**189** 



<!-- Start of picture text -->
looltipse ; |<br>Tooltips display brief labels or messages<br><!-- End of picture text -->



<!-- Start of picture text -->
Add others<br>Grant value is calculated using the closing stock price<br>from the day before the grant date. Amounts do not<br>. . ; .<br>Grant value is calculated using the closing stock price reflect tax witholdings.<br>from the day before the grant date. Amounts do not Learn more<br>reflect tax witholdings.<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Usage of tooltip plain** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.uix.buttonimportMDButton
fromkivymd.uix.tooltipimportMDTooltip
fromkivymd.appimportMDApp
KV='''
<YourTooltipClass>
MDTooltipPlain:
text:
"Grantvalueiscalculatedusingtheclosingstockprice\n"
"fromthedaybeforethegrantdate.Amountsdonot\n"
"reflecttaxwitholdings."
<TooltipMDIconButton>
MDButtonText:
text:root.text
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
TooltipMDIconButton:
text:"Tooltipbutton"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classYourTooltipClass(MDTooltip):
'''Implementsyourtooltipbaseclass.'''
classTooltipMDIconButton(YourTooltipClass,MDButton):
'''Implementsabuttonwithtooltipbehavior.'''
text=StringProperty()
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

**2.3. Components** 

**191** 

**KivyMD, Release 2.0.1.dev0** 

Declarative Python style 

```
fromkivy.propertiesimportStringProperty
fromkivy.clockimportClock
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tooltipimportMDTooltip,MDTooltipPlain
fromkivymd.appimportMDApp
```

```
classYourTooltipClass(MDTooltip):
'''Implementsyourtooltipbaseclass.'''
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.widgets=[
MDTooltipPlain(
text=(
"Grantvalueiscalculatedusingtheclosingstockprice
```

###### **“** 

“from the day before the grant date. Amounts do not 

**“** 

“reflect tax witholdings.” ), ) ] 

###### **class TooltipMDIconButton(YourTooltipClass, MDButton):** 

‘”Implements a button with tooltip behavior.”’ text = StringProperty() 

**def __init__(self, **kwargs):** super().__init__( ****** kwargs) Clock.schedule_once(self.set_widgets) 

**def set_widgets(self, *args):** 

**self.widgets = [** 

**MDButtonText(** text=self.text, pos_hint={“center_x”: .5, “center_y”: .5} ) ] 

###### **class Example(MDApp):** 

**def build(self):** 

self.theme_cls.primary_palette = “Olive” return ( 

###### **MDScreen(** 

###### **TooltipMDIconButton(** 

text=”Tooltip button”, pos_hint={“center_x”: .5, “center_y”: .5}, 

**Chapter 2. Contents** 

**192** 

MDTooltipPlain Grant value is calculated using the closing stock price from the day before the grant date. Amounts do not reflect tax witholdings. 



<!-- Start of picture text -->
MDTooltip<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTooltipRichActionButton:
on_press:tooltip.dismiss()
MDButtonText:
text:"Learnmore"
<TooltipMDIconButton>
MDButtonText:
text:root.text
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
TooltipMDIconButton:
text:"Tooltipbutton"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classYourTooltipClass(MDTooltip):
'''Implementsyourtooltipbaseclass.'''
classTooltipMDIconButton(YourTooltipClass,MDButton):
'''Implementsabuttonwithtooltipbehavior.'''
text=StringProperty()
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.propertiesimportStringProperty
fromkivy.clockimportClock
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.tooltipimport(
MDTooltip,
MDTooltipRich,
MDTooltipRichSubhead,
MDTooltipRichSupportingText,
```

(continues on next page) 

**Chapter 2. Contents** 

**194** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTooltipRichActionButton,
)
fromkivymd.appimportMDApp
classYourTooltipClass(MDTooltip):
'''Implementsyourtooltipbaseclass.'''
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.widgets=[
MDTooltipRich(
MDTooltipRichSubhead(
text="Addothers",
),
MDTooltipRichSupportingText(
text=(
"Grantvalueiscalculatedusingtheclosingstockprice
```

###### **“** 

“from the day before the grant date. Amounts do not 

###### **“** 

“reflect tax witholdings.” 

), 

- ), MDTooltipRichActionButton( 

###### **MDButtonText(** 

text=”Learn more”, 

), on_press=self.tooltip_dismiss, 

), id=”tooltip”, auto_dismiss=False, 

), 

] 

###### **def tooltip_dismiss(self, *args):** 

MDApp.get_running_app().root.get_ids().tooltip.dismiss() 

###### **class TooltipMDIconButton(YourTooltipClass, MDButton):** 

‘”Implements a button with tooltip behavior.”’ 

text = StringProperty() 

###### **def __init__(self, **kwargs):** 

super().__init__( ****** kwargs) Clock.schedule_once(self.set_widgets) 

###### **def set_widgets(self, *args):** 

###### **self.widgets = [** 

###### **MDButtonText(** 

text=self.text, pos_hint={“center_x”: .5, “center_y”: .5} 

) 

] 

**2.3. Components** 

**195** 



<!-- Start of picture text -->
MDTooltipRichSubhead <«—— addothers<br>Grant value is calculated using the closing stock price<br>MDTooltipRichSupportingText <«—— fromthereflect tax daywitholdings.before the grant date.Amountsdo not<br>MDTooltipRichActionButton «—— Leammore<br>MDTooltipRich<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `shift_right` 

Shifting the tooltip to the right. 

Added in version 1.0.0. 

_`shift_right`_ is an `NumericProperty` and defaults to _0_ . 

###### `shift_left` 

Shifting the tooltip to the left. 

Added in version 1.0.0. 

_`shift_left`_ is an `NumericProperty` and defaults to _0_ . 

- `delete_clock(` _widget_ , _touch_ , _*args_ `)` 

Removes a key event from _touch.ud_ . 

###### `adjust_tooltip_position()` _→_ tuple 

Returns the coordinates of the tooltip that fit into the borders of the screen. 

- `display_tooltip(` _*args_ `)` _→_ None 

Adds a tooltip widget to the screen and animates its display. 

###### `animation_tooltip_show(` _*args_ `)` _→_ None 

Animation of opening tooltip on the screen. 

###### `animation_tooltip_dismiss(` _*args_ `)` _→_ None 

Animation of closing tooltip on the screen. 

Added in version 1.0.0. 

`remove_tooltip(` _*args_ `)` _→_ None 

Removes the tooltip widget from the screen. 

###### `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

- `on_long_touch(` _touch_ , _*args_ `)` _→_ None 

Fired when the widget is pressed for a long time. 

- `on_enter(` _*args_ `)` _→_ None 

Fired when mouse enter the bbox of the widget. 

- `on_leave(` _*args_ `)` _→_ None 

Fired when the mouse goes outside the widget border. 

- `on_open()` _→_ None 

Default display event handler. 

Changed in version 2.0.0: Rename from _on_show_ to _on_open_ . 

- `on_dismiss()` _→_ None 

Default dismiss event handler. 

Added in version 1.0.0. 

###### `class kivymd.uix.tooltip.tooltip.MDTooltipPlain(` _*args_ , _**kwargs_ `)` 

Tooltip plain class. 

Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ and _`ScaleBehavior`_ classes documentation. 

**2.3. Components** 

**197** 

**KivyMD, Release 2.0.1.dev0** 

- `class kivymd.uix.tooltip.tooltip.MDTooltipRichSupportingText(` _*args_ , _**kwargs_ `)` 

Implements supporting text for the _`MDTooltipRich`_ class. 

- Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ class documentation. 

- `class kivymd.uix.tooltip.tooltip.MDTooltipRichSubhead(` _*args_ , _**kwargs_ `)` 

   - Implements subhead text for the _`MDTooltipRich`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ class documentation. 

- `class kivymd.uix.tooltip.tooltip.MDTooltipRichActionButton(` _*args_ , _**kwargs_ `)` 

Implements action button for the _`MDTooltipRich`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDButton`_ class documentation. 

- `on_enter()` _→_ None 

Fired when mouse enter the bbox of the widget. 

- `on_leave()` _→_ None 

Fired when the mouse goes outside the widget border. 

- `class kivymd.uix.tooltip.tooltip.MDTooltipRich(` _*args_ , _**kwargs_ `)` 

Tooltip rich class. 

Added in version 2.0.0. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and _`CommonElevationBehavior`_ and _`ScaleBehavior`_ and _`StateLayerBehavior`_ and `BoxLayout` and classes documentation. 

###### `auto_dismiss` 

This property determines if the view is automatically dismissed when the cursor goes outside of the tooltip body. 

_`auto_dismiss`_ is a `BooleanProperty` and defaults to True. 

###### `on_leave()` _→_ None 

Fired when the mouse goes outside the widget border. 

`dismiss()` _→_ None 

Hides the tooltip. 

###### **2.3.24 Swiper** 

**Chapter 2. Contents** 

**198** 

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

Declarative KV style 

```
MDSwiper:
MDSwiperItem:
MDSwiperItem:
MDSwiperItem:
```

Declarative Python style 

```
MDSwiper(
MDSwiperItem(),
MDSwiperItem(),
MDSwiperItem(),
)
```

###### **Example** 

Declarative KV style `from kivy.lang.builder import Builder from kivymd.app import MDApp kv = ''' <MySwiper@MDSwiperItem> FitImage: source: "bg.jpg" radius: [dp(20),] MDScreen: md_bg_color: self.theme_cls.backgroundColor MDSwiper: size_hint_y: None - height: root.height dp(40) y: root.height - self.height - dp(20) MySwiper: MySwiper: MySwiper: MySwiper: MySwiper:` 

(continues on next page) 

**2.3. Components** 

**199** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
'''
classMain(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(kv)
Main().run()
```

Declarative Python style 

```
fromkivymd.material_resourcesimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.swiperimportMDSwiper,MDSwiperItem
classMySwiper(MDSwiperItem):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
FitImage(
source="bg.jpg",
radius=[dp(20),],
)
]
classMain(MDApp):
defon_start(self):
swiper=self.root.get_ids().swiper
swiper.height=(self.root.height-dp(40))
swiper.y=(self.root.height-swiper.height-dp(20))
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDSwiper(
MySwiper(),
MySwiper(),
MySwiper(),
MySwiper(),
MySwiper(),
size_hint_y=None,
id="swiper",
),
md_bg_color=self.theme_cls.backgroundColor,
```

(continues on next page) 

**Chapter 2. Contents** 

**200** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 



<!-- Start of picture text -->
)<br>)<br>Main().run()<br><!-- End of picture text -->

**Warning:** The width of _`MDSwiperItem`_ is adjusted automatically. Consider changing that by `width_mult` . 

**Warning:** The width of _`MDSwiper`_ is automatically adjusted according to the width of the window. 

###### `MDSwiper` **provides the following events for use:** 

```
__events__=(
"on_swipe",
"on_pre_swipe",
"on_overswipe_right",
"on_overswipe_left",
"on_swipe_left",
"on_swipe_right"
)
```

```
MDSwiper:
on_swipe:print("on_swipe")
on_pre_swipe:print("on_pre_swipe")
on_overswipe_right:print("on_overswipe_right")
on_overswipe_left:print("on_overswipe_left")
on_swipe_left:print("on_swipe_left")
on_swipe_right:print("on_swipe_right")
```

###### **API -** `kivymd.uix.swiper.swiper` 

`class kivymd.uix.swiper.swiper.MDSwiperItem(` _*args_ , _**kwargs_ `)` 

Swiper item class. 

For more information, see in the _`MDBoxLayout`_ class documentation. 

- `class kivymd.uix.swiper.swiper.MDSwiper(` _*args_ , _**kwargs_ `)` Swiper class. 

For more information, see in the `ScrollView` class documentation. 

###### `items_spacing` 

- The space between each _`MDSwiperItem`_ . 

- _`items_spacing`_ is an `NumericProperty` and defaults to _20dp_ . 

**2.3. Components** 

**201** 

**KivyMD, Release 2.0.1.dev0** 

###### `transition_duration` 

Duration of switching between _`MDSwiperItem`_ . 

_`transition_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `size_duration` 

Duration of changing the size of _`MDSwiperItem`_ . 

_`transition_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `size_transition` 

The type of animation used for changing the size of _`MDSwiperItem`_ . 

_`size_transition`_ is an `StringProperty` and defaults to _out_quad_ . 

###### `swipe_transition` 

The type of animation used for swiping. 

_`swipe_transition`_ is an `StringProperty` and defaults to _out_quad_ . 

###### `swipe_distance` 

Distance to move before swiping the _`MDSwiperItem`_ . 

_`swipe_distance`_ is an `NumericProperty` and defaults to _70dp_ . 

###### `width_mult` 

This number is multiplied by _`items_spacing`_ x2 and then subtracted from the width of window to specify the width of _`MDSwiperItem`_ . So by decreasing the _`width_mult`_ the width of _`MDSwiperItem`_ increases and vice versa. 

_`width_mult`_ is an `NumericProperty` and defaults to _3_ . 

###### `swipe_on_scroll` 

Wheter to swipe on mouse wheel scrolling or not. 

_`swipe_on_scroll`_ is an `BooleanProperty` and defaults to _True_ . 

###### `add_widget(` _widget_ , _index=0_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**Chapter 2. Contents** 

**202** 

**KivyMD, Release 2.0.1.dev0** 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`remove_widget(` _widget_ `)` 

Remove a widget from the children of this widget. 

###### **Parameters** 

**_widget_ :** `Widget` 

Widget to remove from our children list. 

```
>>>fromkivy.uix.buttonimportButton
>>>root=Widget()
>>>button=Button()
>>>root.add_widget(button)
>>>root.remove_widget(button)
```

`set_current(` _index_ `)` 

Switch to given _`MDSwiperItem`_ index. 

```
get_current_index()
```

Returns the current _`MDSwiperItem`_ index. 

```
get_current_item()
```

Returns the current _`MDSwiperItem`_ instance. 

```
get_items()
```

Returns the list of _`MDSwiperItem`_ children. 

**Note:** Use _get_items()_ to get the list of children instead of _MDSwiper.children_ . 

```
on_swipe()
on_pre_swipe()
on_overswipe_right()
on_overswipe_left()
on_swipe_left()
on_swipe_right()
swipe_left()
swipe_right()
```

`on_scroll_start(` _touch_ , _check_children=True_ `)` 

**2.3. Components** 

**203** 



<!-- Start of picture text -->
®<br>= dette<br>4<br>Text fields let users enter text into a UI 9<br>j i<br><!-- End of picture text -->



<!-- Start of picture text -->
Text field<br>Text field<br>Filled ETIlined<br>Supporting text Supporting text<br><!-- End of picture text -->









<!-- Start of picture text -->
MDTextFieldHintText<br>MDTextFieldLeadinglcon | MDTextFieldTrailinglcon<br>| Hint text |<br>Q Input text wD<br>Helper text 10/10<br>MDTextFieldHelperText MDTextFieldMaxLengthText<br><!-- End of picture text -->







<!-- Start of picture text -->
Filled mode<br><!-- End of picture text -->







<!-- Start of picture text -->
| OutlinedInput text |<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTextFieldLeadingIcon:
icon:"account"
MDTextFieldHintText:
text:"Outlined"
MDTextFieldHelperText:
text:"Helpertext"
mode:"persistent"
MDTextFieldTrailingIcon:
icon:"information"
MDTextFieldMaxLengthText:
max_text_length:10
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.uix.textfieldimport(
MDTextField,
MDTextFieldLeadingIcon,
MDTextFieldHintText,
MDTextFieldHelperText,
MDTextFieldTrailingIcon,
MDTextFieldMaxLengthText,
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnMDScreen(
MDTextField(
MDTextFieldLeadingIcon(
icon="account",
),
MDTextFieldHintText(
text="Hinttext",
```

(continues on next page) 

**Chapter 2. Contents** 

**208** 





<!-- Start of picture text -->
| Outlined& Input text ri] |<br>Helper text 10/10<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

**Note:** The text field with the _round_ type was removed in version _2.0.0_ . 

Declarative KV style 

```
MDTextField:
mode:"outlined"
MDTextFieldLeadingIcon:
icon:"phone"
MDTextFieldTrailingIcon:
icon:"information"
MDTextFieldHintText:
text:"Hinttext"
MDTextFieldHelperText:
text:"Helpertext"
mode:"persistent"
MDTextFieldMaxLengthText:
max_text_length:10
```

Declarative Python style 

```
MDTextField(
MDTextFieldLeadingIcon(
icon="magnify",
),
MDTextFieldHintText(
text="Hinttext",
),
MDTextFieldHelperText(
text="Helpertext",
mode="persistent",
),
MDTextFieldTrailingIcon(
icon="information",
),
MDTextFieldMaxLengthText(
max_text_length=10,
),
)
```

**Chapter 2. Contents** 

**210** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.textfield.textfield` 

###### `class kivymd.uix.textfield.textfield.AutoFormatTelephoneNumber` 

Implements automatic formatting of the text entered in the text field according to the mask, for example ‘+38 (###) ### ## ##’. 

**Warning:** This class has not yet been implemented and it is not recommended to use it yet. 

`isnumeric(` _value_ `)` _→_ bool 

###### `do_backspace(` _*args_ `)` _→_ None 

Do backspace operation from the current cursor position. 

`field_filter(` _value_ , _boolean_ `)` _→_ None 

`format(` _value_ `)` _→_ None 

```
classkivymd.uix.textfield.textfield.Validator
```

Container class for various validation methods. 

###### `datetime_date` 

The last valid date as a <class ‘datetime.date’> object. 

_`datetime_date`_ is an `ObjectProperty` and defaults to _None_ . 

###### `date_interval` 

The date interval that is valid for input. Can be entered as <class ‘datetime.date’> objects or a string format. Both values or just one value can be entered. 

In string format, must follow the current date_format. Example: Given date_format -> “mm/dd/yyyy” Input examples -> “12/31/1900”, “12/31/2100” or “12/31/1900”, None. 

_`date_interval`_ is an `ListProperty` and defaults to _[None, None]_ . 

###### `date_format` 

Format of date strings that will be entered. Available options are: _‘dd/mm/yyyy’_ , _‘mm/dd/yyyy’_ , _‘yyyy/mm/dd’_ . 

_`date_format`_ is an `OptionProperty` and defaults to _None_ . 

- `is_number_valid(` _text: str_ `)` _→_ bool 

Checks if the text contains only digits. 

- `is_email_valid(` _text: str_ `)` _→_ bool 

Checks the validity of the email. 

- `is_time_valid(` _text: str_ `)` _→_ bool 

Checks the validity of the time. 

- `is_date_valid(` _text: str_ `)` _→_ bool 

Checks the validity of the date. 

- `on_date_interval(` _*args_ `)` _→_ None 

Default event handler for date_interval input. 

**2.3. Components** 

**211** 

**KivyMD, Release 2.0.1.dev0** 

`class kivymd.uix.textfield.textfield.BaseTextFieldLabel(` _*args_ , _**kwargs_ `)` 

Base texture for _`MDTextField`_ class (helper text, max length, hint text). 

For more information, see in the _`MDLabel`_ class documentation. 

Added in version 2.0.0. 

###### `text_color_normal` 

Text color in (r, g, b, a) or string format when text field is out of focus. 

Added in version 1.0.0. 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ class and renamed from _helper_text_color_normal_ to _text_color_normal_ . 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldHintText:
text:"Hinttextcolornormal"
text_color_normal:"brown"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHintText(
text="Hinttextcolornormal",
text_color_normal="brown",
),
mode="filled",
)
```



_`text_color_normal`_ is an `ColorProperty` and defaults to _None_ . 

###### `text_color_focus` 

Text color in (r, g, b, a) or string format when the text field has focus. 

Added in version 1.0.0. 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ class and renamed from _helper_text_color_focus_ to _text_color_focus_ . 

Declarative KV style 

```
MDTextField:
MDTextFieldHelperText:
```

(continues on next page) 

**Chapter 2. Contents** 

**212** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text:"Helpertextcolorfocus"
text_color_focus:"brown"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Helpertextcolorfocus",
text_color_normal="brown",
),
)
```



_`text_color_focus`_ is an `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.textfield.textfield.MDTextFieldHelperText(` _*args_ , _**kwargs_ `)` 

   - Implements the helper text label. 

For more information, see in the _`BaseTextFieldLabel`_ class documentation. 

Added in version 2.0.0. 

```
mode
```

Helper text mode. Available options are: _‘on_error’_ , _‘persistent’_ , _‘on_focus’_ . 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ class and renamed from _helper_text_mode_ to _mode_ . 

###### **On focus** 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldHelperText:
text:"Helpertext"
mode:"on_focus"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Helpertext",
mode="on_focus",
```

(continues on next page) 

**2.3. Components** 

**213** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
),
mode="filled",
)
```

###### **On error** 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldHelperText:
text:"Helpertext"
mode:"on_error"
MDTextFieldMaxLengthText:
max_text_length:5
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Helpertext",
mode="on_error",
),
MDTextFieldMaxLengthText(
max_text_length=5,
),
mode="filled",
)
```

###### **Persistent** 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldHelperText:
text:"Helpertext"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Helpertext",
```

(continues on next page) 

**Chapter 2. Contents** 

**214** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
mode="persistent",
),
mode="filled",
)
```

_`mode`_ is an `OptionProperty` and defaults to _‘on_focus’_ . 

###### `class kivymd.uix.textfield.textfield.MDTextFieldMaxLengthText(` _*args_ , _**kwargs_ `)` 

Implements the max length text label. 

For more information, see in the _`BaseTextFieldLabel`_ class documentation. 

Added in version 2.0.0. 

###### `max_text_length` 

Maximum allowed value of characters in a text field. 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ . 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldMaxLengthText:
max_text_length:10
```

Declarative Python style 

```
MDTextField(
MDTextFieldMaxLengthText(
max_text_length=10,
),
mode="filled",
)
```



_`max_text_length`_ is an `NumericProperty` and defaults to _None_ . 

###### `class kivymd.uix.textfield.textfield.MDTextFieldHintText(` _*args_ , _**kwargs_ `)` 

Implements the hint text label. 

For more information, see in the _`BaseTextFieldLabel`_ class documentation. 

Added in version 2.0.0. 

- Declarative KV style 

**2.3. Components** 

**215** 

**KivyMD, Release 2.0.1.dev0** 

```
MDTextField:
mode:"filled"
MDTextFieldHintText:
text:"Hinttext"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHintText(
text="Hinttext",
),
mode="filled",
)
```

`class kivymd.uix.textfield.textfield.BaseTextFieldIcon(` _*args_ , _**kwargs_ `)` 

Base texture for _`MDTextField`_ class (helper text, max length, hint text). 

For more information, see in the _`MDIcon`_ class documentation. 

Changed in version 2.0.0. 

###### `icon_color_normal` 

Icon color in (r, g, b, a) or string format when text field is out of focus. 

Added in version 1.0.0. 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ class and renamed from _icon_right_color_normal/icon_left_color_normal_ to _icon_color_normal_ . 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldLeadingIcon:
icon:"phone"
theme_icon_color:"Custom"
icon_color_normal:"lightgreen"
MDTextFieldHintText:
text:"Leadingiconcolornormal"
```

Declarative Python style 

```
MDTextField(
MDTextFieldLeadingIcon(
icon="phone",
theme_icon_color="Custom",
icon_color_normal="lightgreen",
),
MDTextFieldHintText(
text="Leadingiconcolornormal",
),
```

(continues on next page) 

**Chapter 2. Contents** 

**216** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
mode="filled",
)
```



_`icon_color_normal`_ is an `ColorProperty` and defaults to _None_ . 

###### `icon_color_focus` 

Icon color in (r, g, b, a) or string format when the text field has focus. 

Added in version 1.0.0. 

Changed in version 2.0.0: The property was moved from class: _~MDTextField_ class and renamed from _icon_right_color_focus/icon_left_color_focus ` to `icon_color_focus_ . 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldLeadingIcon:
icon:"phone"
theme_icon_color:"Custom"
icon_color_focus:"lightgreen"
MDTextFieldHintText:
text:"Leadingiconcolorfocus"
```

Declarative Python style 

```
MDTextField(
MDTextFieldLeadingIcon(
icon="phone",
theme_icon_color="Custom",
icon_color_focus="lightgreen",
),
MDTextFieldHintText(
text="Leadingiconcolorfocus",
),
mode="filled",
)
```

**2.3. Components** 

**217** 

**KivyMD, Release 2.0.1.dev0** 



_`icon_color_focus`_ is an `ColorProperty` and defaults to _None_ . 

- `on_icon_color_normal(` _instance:_ BaseTextFieldIcon _|_ MDTextFieldTrailingIcon, _value: list | str_ `)` 

Called when the _icon_color_normal_ property of the icon is changed. 

If the associated text field is set, this method triggers an update to the icon’s color appearance, ensuring that the correct color is used based on the focus state of the text field. 

Typically used to visually reflect property changes in real time in response to user interaction or theme updates. 

###### **Parameters** 

- `instance` – The instance of _BaseTextFieldIcon_ that had its _icon_color_normal_ property changed. 

- `value` – The new color value, either as a list of RGBA components or a string (e.g., a hex color or color name). 

`class kivymd.uix.textfield.textfield.MDTextFieldLeadingIcon(` _*args_ , _**kwargs_ `)` 

Implements the leading icon. 

For more information, see in the _`BaseTextFieldIcon`_ class documentation. 

Added in version 2.0.0. 

Declarative KV style 

```
MDTextField:
mode:"filled"
MDTextFieldLeadingIcon:
icon:"phone"
MDTextFieldHintText:
text:"Fieldwithleadingicon"
```

Declarative Python style 

```
MDTextField(
MDTextFieldLeadingIcon(
icon="phone",
),
MDTextFieldHintText(
text="Fieldwithleadingicon",
),
mode="filled",
)
```

**Chapter 2. Contents** 

**218** 



<!-- Start of picture text -->
es Field with leading leon<br><!-- End of picture text -->







<!-- Start of picture text -->
Fleld with trailing leon es<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `font_style` 

Name of the style for the input text. 

Added in version 2.0.0. 

**See also:** 

Font style names 

_`font_style`_ is an `StringProperty` and defaults to _‘Body’_ . 

```
role
```

Role of font style. 

Added in version 2.0.0. 

**See also:** 

Font style roles 

_`role`_ is an `StringProperty` and defaults to _‘large’_ . 

```
mode
```

Text field mode. Available options are: _‘outlined’_ , _‘filled’_ . 

_`mode`_ is an `OptionProperty` and defaults to _‘outlined’_ . 

###### `error_color` 

Error color in (r, g, b, a) or string format for _required = True_ or when the text field is in _error_ state. 

_`error_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `error` 

If True, then the text field goes into _error_ mode. 

_`error`_ is an `BooleanProperty` and defaults to _False_ . 

###### `text_color_normal` 

Text color in (r, g, b, a) or string format when text field is out of focus. 

Added in version 1.0.0. 

Declarative KV style 

###### <u>`MDTextField:`</u> 

```
theme_text_color:"Custom"
text_color_normal:"green"
text:"Textcolornormal"
```

Declarative Python style 

```
MDTextField(
theme_text_color="Custom",
text_color_normal="green",
text="Textcolornormal",
)
```

**Chapter 2. Contents** 

**220** 

**KivyMD, Release 2.0.1.dev0** 



_`text_color_normal`_ is an `ColorProperty` and defaults to _None_ . 

###### `text_color_focus` 

Text color in (r, g, b, a) or string format when text field has focus. 

Added in version 1.0.0. 

Declarative KV style 

```
MDTextField:
theme_text_color:"Custom"
text_color_focus:"green"
text:"Textcolorfocus"
```

Declarative Python style 

```
MDTextField(
theme_text_color="Custom",
text_color_focus="green",
text="Textcolorfocus",
)
```



_`text_color_focus`_ is an `ColorProperty` and defaults to _None_ . 

###### `radius` 

The corner radius for a text field in _filled/outlined_ mode. 

_`radius`_ is a `VariableListProperty` and defaults to _[dp(4), dp(4), 0, 0]_ . 

###### `required` 

Required text. If True then the text field requires text. 

_`required`_ is an `BooleanProperty` and defaults to _False_ . 

###### `line_color_normal` 

Line color normal (active indicator) in (r, g, b, a) or string format. 

Declarative KV style 

**2.3. Components** 

**221** 

**KivyMD, Release 2.0.1.dev0** 

```
MDTextField:
mode:"filled"
theme_line_color:"Custom"
line_color_normal:"green"
MDTextFieldHelperText:
text:"Linecolornormal"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Linecolornormal",
mode="persistent",
),
mode="filled",
theme_line_color="Custom",
line_color_normal="green",
)
```



_`line_color_normal`_ is an `ColorProperty` and defaults to _None_ . 

###### `line_color_focus` 

Line color focus (active indicator) in (r, g, b, a) or string format. 

Declarative KV style 

```
MDTextField:
mode:"filled"
theme_line_color:"Custom"
line_color_focus:"green"
MDTextFieldHelperText:
text:"Linecolorfocus"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Linecolorfocus",
mode="persistent",
),
mode="filled",
```

(continues on next page) 

**Chapter 2. Contents** 

**222** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
theme_line_color="Custom",
line_color_focus="green",
)
```



_`line_color_focus`_ is an `ColorProperty` and defaults to _None_ . 

###### `fill_color_normal` 

Fill background color in (r, g, b, a) or string format in ‘fill’ mode when] text field is out of focus. 

Declarative KV style 

```
MDTextField:
mode:"filled"
theme_bg_color:"Custom"
fill_color_normal:0,1,0,.2
MDTextFieldHelperText:
text:"Fillcolornormal"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Fillcolornormal",
mode="persistent",
),
mode="filled",
theme_bg_color="Custom",
fill_color_normal=[0,1,0,.2],
)
```



_`fill_color_normal`_ is an `ColorProperty` and defaults to _None_ . 

###### `fill_color_focus` 

Fill background color in (r, g, b, a) or string format in ‘fill’ mode when the text field has focus. 

**2.3. Components** 

**223** 

**KivyMD, Release 2.0.1.dev0** 

Declarative KV style 

```
MDTextField:
mode:"filled"
theme_bg_color:"Custom"
fill_color_focus:0,1,0,.2
MDTextFieldHelperText:
text:"Fillcolorfocus"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="Fillcolorfocus",
mode="persistent",
),
mode="filled",
theme_bg_color="Custom",
fill_color_focus=[0,1,0,.2],
)
```



_`fill_color_focus`_ is an `ColorProperty` and defaults to _None_ . 

###### `max_height` 

Maximum height of the text box when _multiline = True_ . 

Declarative KV style 

```
MDTextField:
mode:"filled"
max_height:"200dp"
multiline:True
MDTextFieldHelperText:
text:"multiline=True"
mode:"persistent"
```

Declarative Python style 

```
MDTextField(
MDTextFieldHelperText(
text="multiline=True",
mode="persistent",
),
```

(continues on next page) 

**Chapter 2. Contents** 

**224** 









<!-- Start of picture text -->
Emailemail ®<br>“weegmalcom<br>Q maluser@gmaitcom  @<br>weregmalcom<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
orientation:"vertical"
spacing:"28dp"
adaptive_height:True
size_hint_x:.8
pos_hint:{"center_x":.5,"center_y":.5}
MDTextField:
validator:"date"
date_format:"dd/mm/yyyy"
MDTextFieldHintText:
text:"Datedd/mm/yyyywithoutlimits"
MDTextFieldHelperText:
text:"Enteravaliddd/mm/yyyydate"
MDTextField:
validator:"date"
date_format:"mm/dd/yyyy"
MDTextFieldHintText:
text:"Datemm/dd/yyyywithoutlimits"
MDTextFieldHelperText:
text:"Enteravalidmm/dd/yyyydate"
MDTextField:
validator:"date"
date_format:"yyyy/mm/dd"
MDTextFieldHintText:
text:"Dateyyyy/mm/ddwithoutlimits"
MDTextFieldHelperText:
text:"Enteravalidyyyy/mm/dddate"
MDTextField:
validator:"date"
date_format:"dd/mm/yyyy"
date_interval:"01/01/1900","01/01/2100"
MDTextFieldHintText:
```

(continues on next page) 

**Chapter 2. Contents** 

**226** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `text: "Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval" MDTextFieldHelperText: text: "Enter a valid dd/mm/yyyy date" MDTextField: validator: "date" date_format: "dd/mm/yyyy" date_interval: "01/01/1900", None MDTextFieldHintText: text: "Date dd/mm/yyyy in [01/01/1900, None] interval" MDTextFieldHelperText: text: "Enter a valid dd/mm/yyyy date" MDTextField: validator: "date" date_format: "dd/mm/yyyy" date_interval: None, "01/01/2100" MDTextFieldHintText: text: "Date dd/mm/yyyy in [None, 01/01/2100] interval" MDTextFieldHelperText: text: "Enter a valid dd/mm/yyyy date" ''' class Example(MDApp): def build(self): self.theme_cls.primary_palette = "Olive" return Builder.load_string(KV) Example().run()` 

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.textfieldimport(
MDTextField,MDTextFieldHintText,MDTextFieldHelperText
)
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
```

(continues on next page) 

**2.3. Components** 

**227** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`MDBoxLayout( MDTextField( MDTextFieldHintText( text="Date dd/mm/yyyy without limits", ), MDTextFieldHelperText( text="Enter a valid dd/mm/yyyy date", ), validator="date", date_format="dd/mm/yyyy", ), MDTextField( MDTextFieldHintText( text="Date mm/dd/yyyy without limits", ), MDTextFieldHelperText( text="Enter a valid mm/dd/yyyy date", ), validator="date", date_format="mm/dd/yyyy", ), MDTextField( MDTextFieldHintText( text="Date yyyy/mm/dd without limits", ), MDTextFieldHelperText( text="Enter a valid yyyy/mm/dd date", ), validator="date", date_format="yyyy/mm/dd", ), MDTextField( MDTextFieldHintText( text="Date dd/mm/yyyy in [01/01/1900, 01/01/2100]␣` _˓→_ `interval", ), MDTextFieldHelperText( text="Enter a valid dd/mm/yyyy date", ), validator="date", date_format="dd/mm/yyyy", date_interval=["01/01/1900", "01/01/2100"], ), MDTextField( MDTextFieldHintText( text="Date dd/mm/yyyy in [01/01/1900, None]␣` _˓→_ `interval", ), MDTextFieldHelperText( text="Enter a valid dd/mm/yyyy date", ), validator="date",` 

(continues on next page) 

**Chapter 2. Contents** 

**228** 



| Date12/12/2023 dd/mmy/yyyy without limits | Entera valid dd/mmi/yyyy date Date mm/dd/yyyy without limits Date yyyy/mm/dd without limits Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval Date dd/mm/yyyy in [01/01/1900, None] interval Date dd/mm/yyyy in [None, 01/01/2100] interval 

**KivyMD, Release 2.0.1.dev0** 

_`validator`_ is an `OptionProperty` and defaults to _None_ . 

`update_colors(` _theme_manager:_ kivymd.theming.ThemeManager, _theme_color: str_ `)` _→_ None 

Fired when the _primary_palette_ or _theme_style_ value changes. 

- `add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

- `set_texture_color(` _texture_ , _canvas_group_ , _color: list_ , _error: bool = False_ `)` _→_ None 

Animates the color of the leading/trailing icons/hint/helper/max length text. 

###### `get_adjusted_pos_max_length_label()` _→_ tuple 

Calculates the position of the max length label. 

###### **Returns:** 

tuple: (x, y) coordinates for positioning the max length label. 

###### `get_adjusted_pos_helper_text_label()` _→_ tuple 

Calculates the position of the helper text label based on the textfield mode. 

###### **Returns:** 

tuple: (x, y) coordinates for positioning the helper text label. 

###### `get_adjusted_pos_trailing_icon()` _→_ tuple 

Calculates the adjusted position of the trailing icon. 

###### **Returns:** 

tuple: (x, y) coordinates for positioning the trailing icon. 

###### `get_adjusted_pos_leading_icon()` _→_ tuple 

Calculates the adjusted position of the leading icon based on the textfield mode and icon size. 

###### **Returns:** 

tuple: (x, y) coordinates for positioning the leading icon. 

**Chapter 2. Contents** 

**230** 

**KivyMD, Release 2.0.1.dev0** 

###### `get_adjusted_pos_hint_text_label()` _→_ tuple 

Calculates the adjusted position of the hint text label based on the presence of a leading icon and whether the textfield is multiline. 

###### **Returns:** 

tuple: (x, y) position coordinates for the hint text label. 

`set_pos_hint_text(` _y: float_ , _x: float_ `)` _→_ None 

Animates the x-axis width and y-axis height of the hint text. 

`set_hint_text_font_size()` _→_ None 

Animates the font size of the hint text. 

`set_space_in_line(` _left_width: float | int_ , _right_width: float | int_ `)` _→_ None 

Animates the length of the right line of the text field for the hint text. 

###### `set_max_text_length()` _→_ None 

Fired when text is entered into a text field. Set max length text and updated max length texture. 

###### `adjust_height(` _*args_ `)` _→_ None 

Adjusts the height of the text field in multiline mode. 

- `set_text(` _instance_ , _text: str_ `)` _→_ None 

Fired when text is entered into a text field. 

- `on_focus(` _instance_ , _focus: bool_ `)` _→_ None 

Fired when the _focus_ value changes. 

- `on_disabled(` _instance_ , _disabled: bool_ `)` _→_ None 

Fired when the _disabled_ value changes. 

- `on_error(` _instance_ , _error: bool_ `)` _→_ None 

Changes the primary colors of the text box to match the _error_ value (text field is in an error state or not). 

`on_height(` _instance_ , _value_height: float_ `)` _→_ None 

###### **2.3.26 DropdownItem** 



**2.3. Components** 

**231** 

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.appimportMDApp
KV='''
MDScreen
md_bg_color:self.theme_cls.backgroundColor
MDDropDownItem:
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.open_menu(self)
MDDropDownItemText:
id:drop_text
text:"Item"
'''
classExample(MDApp):
defopen_menu(self,item):
menu_items=[
{
"text":f"{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
MDDropdownMenu(caller=item,items=menu_items).open()
defmenu_callback(self,text_item):
self.root.ids.drop_text.text=text_item
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.uix.dropdownitemimportMDDropDownItem,MDDropDownItemText
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defopen_menu(self,item):
menu_items=[
```

(continues on next page) 

**Chapter 2. Contents** 

**232** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
{
"text":f"{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
MDDropdownMenu(caller=item,items=menu_items).open()
defmenu_callback(self,text_item):
self.root.get_ids().drop_text.text=text_item
defbuild(self):
return(
MDScreen(
MDDropDownItem(
MDDropDownItemText(
id="drop_text",
text="Item",
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.open_menu,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

###### **See also:** 

Work with the class MDDropdownMenu see here 

###### **API break** 

###### **1.2.0 version** 

```
MDDropDownItem:
text:'Item'
on_release:print(*args)
```

###### **2.0.0 version** 

```
MDDropDownItem:
on_release:print(*args)
MDDropDownItemText:
text:"Itemtext"
```

**2.3. Components** 

**233** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.dropdownitem.dropdownitem` 

###### `class kivymd.uix.dropdownitem.dropdownitem.MDDropDownItemText(` _*args_ , _**kwargs_ `)` 

- Base texture for _`MDDropDownItem`_ class (item text). 

For more information, see in the _`MDLabel`_ class documentation. 

Added in version 2.0.0. 

- `class kivymd.uix.dropdownitem.dropdownitem.MDDropDownItem(` _*args_ , _**kwargs_ `)` 

Dropdown item class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and `ButtonBehavior` and `BoxLayout` classes documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

- **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`update_text_item(` _instance_ , _value_ `)` _→_ None 

Updates the text of the item. 

- `on_disabled(` _instance_ , _value_ `)` _→_ None 

Fired when the values of `disabled` change. 

- `on__drop_down_text(` _instance_ , _value_ `)` _→_ None 

Fired when the values of `_drop_down_text` change. 

**Chapter 2. Contents** 

**234** 



<!-- Start of picture text -->
7" Good healthy lunch idea 9:20 AM<br>, Alejandro Ortega<br>WP" ~ SofiabonjourSacchide Par Thr ago<br>S OF cxasenchi te 7<br>Badg e Carmen Villanueva<br>Badges show notifications, counts, or status information on > x) a rR)<br>navigation items and icons =<br><!-- End of picture text -->









<!-- Start of picture text -->
avigation - 2<br>Navigation rails let people switch between UI views on mid-sized a<br>devices<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationRailMenuButton:
icon:"menu"
MDNavigationRailFabButton:
icon:"home"
CommonNavigationRailItem:
icon:"folder-outline"
text:"Files"
CommonNavigationRailItem:
icon:"bookmark-outline"
text:"Bookmark"
CommonNavigationRailItem:
icon:"library-outline"
text:"Library"
MDScreen:
md_bg_color:self.theme_cls.secondaryContainerColor
'''
classCommonNavigationRailItem(MDNavigationRailItem):
text=StringProperty()
icon=StringProperty()
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.clockimportClock
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.navigationrailimport(
MDNavigationRailItem,
MDNavigationRail,
MDNavigationRailMenuButton,
MDNavigationRailFabButton,
MDNavigationRailItemIcon,
MDNavigationRailItemLabel,
)
fromkivymd.uix.screenimportMDScreen
```

(continues on next page) 

**Chapter 2. Contents** 

**238** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classCommonNavigationRailItem(MDNavigationRailItem):
text=StringProperty()
icon=StringProperty()
defon_icon(self,instance,value):
defon_icon(*ars):
self.add_widget(MDNavigationRailItemIcon(icon=value))
Clock.schedule_once(on_icon)
```

```
defon_text(self,instance,value):
defon_text(*ars):
self.add_widget(MDNavigationRailItemLabel(text=value))
Clock.schedule_once(on_text)
```

```
classExample(MDApp):
defbuild(self):
returnMDBoxLayout(
MDNavigationRail(
MDNavigationRailMenuButton(
icon="menu",
),
MDNavigationRailFabButton(
icon="home",
),
CommonNavigationRailItem(
icon="bookmark-outline",
text="Files",
),
CommonNavigationRailItem(
icon="folder-outline",
text="Bookmark",
),
CommonNavigationRailItem(
icon="library-outline",
text="Library",
),
type="selected",
),
MDScreen(
md_bg_color=self.theme_cls.secondaryContainerColor,
),
)
Example().run()
```

**2.3. Components** 

**239** 



<!-- Start of picture text -->
o<br>Files<br>a<br>ao<br><!-- End of picture text -->







= ——_=MDNavigationRailMenuButton ge MDNavigationRailFabButton 



<!-- Start of picture text -->
MDNavigationRailltem<br>Files<br>Oo<br>mo<br><!-- End of picture text -->

——_—=S—MDNavigationRail 







0 —_]|§_ _——> Files —________________§%& Oo m 

MDNavigationRailltem MDNavigationRailltemicon lViDNavigationRailltemLabel 



<!-- Start of picture text -->
Va VA Va<br>Label Label<br>A<br>A A<br>Label<br>Oo Oo Oo<br>Label<br>ce] ce] ce]<br>Label<br><!-- End of picture text -->

|Va|VA|Va|
|---|---|---|
|Label||@<br>e<br>Label|
|A|A|A<br>Label|
|Oo<br>ce]|Oo<br>ce]|Oo<br>Label<br>ce]<br>Label|



**KivyMD, Release 2.0.1.dev0** 

###### **Selected** 

```
MDNavigationRail:
type:"selected"#default
```

###### **Unselected** 

```
MDNavigationRail:
type:"unselected"
```

###### **Labeled** 

```
MDNavigationRail:
type:"labeled"
```

**Chapter 2. Contents** 

**244** 



<!-- Start of picture text -->
Va VA Va<br>@<br>Label<br>A @<br>Label<br>Oo<br>A<br>ce]<br>Oo<br>@<br>Qo Label<br>A<br>Oo<br>a<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Top** 

```
MDNavigationRail:
anchor:"top"
```

###### **Center** 

```
MDNavigationRail:
anchor:"center"#default
```

###### **Bottom** 

```
MDNavigationRail:
anchor:"bottom"
```

###### **API break** 

###### **1.2.0 version** 

```
MDNavigationRail:
```

```
MDNavigationRailMenuButton:
icon:"menu"
MDNavigationRailFabButton:
icon:"home"
MDNavigationRailItem:
icon:icon
text:text
```

###### **2.2.0 version** 

Declarative KV style 

```
MDNavigationRail:
```

```
#Optional.
MDNavigationRailMenuButton:
icon:"menu"
#Optional.
MDNavigationRailFabButton:
icon:"home"
MDNavigationRailItem
```

(continues on next page) 

**Chapter 2. Contents** 

**246** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationRailItemIcon:
icon:icon
MDNavigationRailItemLabel:
text:text
```

Declarative Python style 

```
MDNavigationRail(
#Optional.
MDNavigationRailMenuButton(
icon="menu"
),
#Optional.
MDNavigationRailFabButton(
icon="home"
),
MDNavigationRailItem(
MDNavigationRailItemIcon(
icon=icon
),
MDNavigationRailItemLabel(
text=text
),
)
)
```

###### **API -** `kivymd.uix.navigationrail.navigationrail` 

- `class kivymd.uix.navigationrail.navigationrail.MDNavigationRailFabButton(` _**kwargs_ `)` Implements a floating action button (FAB). 

For more information, see in the _`MDFabButton`_ class documentation. 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the switch when the widget is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.navigationrail.navigationrail.MDNavigationRailMenuButton(` _**kwargs_ `)` Implements a menu button. 

For more information, see in the _`MDIconButton`_ class documentation. 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the switch when the widget is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemIcon(` _*args_ , _**kwargs_ `)` Implements an icon for the _`MDNavigationRailItem`_ class. 

For more information, see in the _`MDIcon`_ class documentation. 

- Changed in version 2.0.0. 

**2.3. Components** 

**247** 

**KivyMD, Release 2.0.1.dev0** 

###### `active_indicator_color` 

Background color of the active indicator in (r, g, b, a) or string format. 

_`active_indicator_color`_ is an `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemLabel(` _*args_ , _**kwargs_ `)` 

Implements an label for the _`MDNavigationRailItem`_ class. 

For more information, see in the _`ScaleBehavior`_ and _`MDLabel`_ classes documentation. 

Changed in version 2.0.0. 

```
scale_value_y
```

Y-axis value. 

_`scale_value_y`_ is an `NumericProperty` and defaults to _0_ . 

- `on__active(` _instance_ , _value_ `)` _→_ None 

Fired when the `_active` value changes. 

- `class kivymd.uix.navigationrail.navigationrail.MDNavigationRailItem(` _*args_ , _**kwargs_ `)` 

Implements a menu item with an icon and text. 

For more information, see in the _`DeclarativeBehavior`_ and `ButtonBehavior` and _`ThemableBehavior`_ and _`StateFocusBehavior`_ `BoxLayout` classes documentation. 

###### `active` 

Is the element active. 

_`active`_ is an `BooleanProperty` and defaults to _False_ . 

###### `radius` 

Item radius. 

Changed in version 2.0.0. 

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

- `on_active(` _instance_ , _value_ `)` _→_ None 

Fired when the _`active`_ value changes. 

- `on_enter(` _*args_ `)` _→_ None 

Fired when mouse enter the bbox of the widget. 

- `on_leave(` _*args_ `)` _→_ None 

Fired when the mouse goes outside the widget border. 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**Chapter 2. Contents** 

**248** 

**KivyMD, Release 2.0.1.dev0** 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.navigationrail.navigationrail.MDNavigationRail(` _*args_ , _**kwargs_ `)` Navigation rail class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `RelativeLayout` classes documentation. 

```
radius
```

Rail radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `anchor` 

The position of the panel with menu items. Available options are: _‘top’_ , _‘bottom’_ , _‘center’_ . 

_`anchor`_ is an `OptionProperty` and defaults to _‘center’_ . 

###### `type` 

Type of switching menu items. Available options are: _‘labeled’_ , _‘selected’_ , _‘unselected’_ . 

_`type`_ is an `OptionProperty` and defaults to _‘labeled’_ . 

```
fab_button:MDNavigationRailFabButton
```

```
menu_button:MDNavigationRailFabButton
```

`on_size(` _*args_ `)` _→_ None 

Fired when the application screen size changes. 

`get_items()` _→_ list 

Returns a list of _`MDNavigationRailItem`_ objects. 

`set_active_item(` _item:_ MDNavigationRailItem `)` _→_ None 

Sets the active menu list item. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

**2.3. Components** 

**249** 

**KivyMD, Release 2.0.1.dev0** 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### **2.3.29 FileManager** 

A simple manager for selecting directories and files. 

###### **Usage** 

`path = os.path.expanduser("~")` _`# path to the directory that will be opened in the file`_ `␣` _˓→_ _`manager`_ `file_manager = MDFileManager( exit_manager=self.exit_manager,` _`# function called when the user reaches directory`_ `␣` _˓→_ _`tree root`_ `select_path=self.select_path,` _`# function called when selecting a file/directory`_ `) file_manager.show(path)` 

**Chapter 2. Contents** 

**250** 



<!-- Start of picture text -->
<  /Users/macbookair 3<br>fs Applications<br>fe Desktop<br>fs Documents<br>fs Downloads<br>fe sLibrary<br>f Movies<br>fs Music<br>= A]<br>po<br><!-- End of picture text -->





<!-- Start of picture text -->
=<br>/Users/macbo...tom-menu.png /Users/macbo...rt_screen.png /Users/macbo...aplication.png<br>/Users/macbo...t-key-item.png /Users/macbo...tem-menu.png /Users/macbo...gation-rail.png<br>fos}<br>=<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
'''
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
Window.bind(on_keyboard=self.events)
self.manager_open=False
self.file_manager=MDFileManager(
exit_manager=self.exit_manager,select_path=self.select_path
)
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
deffile_manager_open(self):
self.file_manager.show(
os.path.expanduser("~"))#outputmanagertothescreen
self.manager_open=True
defselect_path(self,path:str):
'''
Itwillbecalledwhenyouclickonthefilename
orthecatalogselectionbutton.
:parampath:pathtotheselecteddirectoryorfile;
'''
self.exit_manager()
MDSnackbar(
MDSnackbarText(
text=path,
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.8,
).open()
defexit_manager(self,*args):
'''Calledwhentheuserreachestherootofthedirectorytree.'''
self.manager_open=False
self.file_manager.close()
defevents(self,instance,keyboard,keycode,text,modifiers):
'''Calledwhenbuttonsarepressedonthemobiledevice.'''
ifkeyboardin(1001,27):
ifself.manager_open:
self.file_manager.back()
returnTrue
```

(continues on next page) 

**2.3. Components** 

**253** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Declarative python style 

```
importos
fromkivy.core.windowimportWindow
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.filemanagerimportMDFileManager
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarText
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
Window.bind(on_keyboard=self.events)
self.manager_open=False
self.file_manager=MDFileManager(
exit_manager=self.exit_manager,select_path=self.select_path
)
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmanager"
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.file_manager_open,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
deffile_manager_open(self,*args):
self.file_manager.show(
os.path.expanduser("~"))#outputmanagertothescreen
self.manager_open=True
defselect_path(self,path:str):
'''
Itwillbecalledwhenyouclickonthefilename
orthecatalogselectionbutton.
```

(continues on next page) 

**Chapter 2. Contents** 

**254** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
:parampath:pathtotheselecteddirectoryorfile;
'''
self.exit_manager()
MDSnackbar(
MDSnackbarText(
text=path,
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.8,
).open()
defexit_manager(self,*args):
'''Calledwhentheuserreachestherootofthedirectorytree.'''
self.manager_open=False
self.file_manager.close()
defevents(self,instance,keyboard,keycode,text,modifiers):
'''Calledwhenbuttonsarepressedonthemobiledevice.'''
ifkeyboardin(1001,27):
ifself.manager_open:
self.file_manager.back()
returnTrue
Example().run()
```

Added in version 1.0.0. 

Added a feature that allows you to show the available disks first, then the files contained in them. Works correctly on: _Windows_ , _Linux_ , _OSX_ , _Android_ . Not tested on _iOS_ . 

```
deffile_manager_open(self):
self.file_manager.show_disks()
```

**2.3. Components** 

**255** 



<!-- Start of picture text -->
‘ x)<br>Qs<br>(3) /System/Volumes/Data<br>{)  /System/Volumes/Data/home<br>1@ / dev<br>{  /private/var/vm<br><!-- End of picture text -->



<!-- Start of picture text -->
<«  /Users/macbookair x |<br>O& Applications<br>fs Desktop<br>f Documents<br>f Downloads<br>Oe sLibrary<br>fs Movies<br>i Music<br><!-- End of picture text -->





<!-- Start of picture text -->
<  /Users/macbookair x<br>f= Applications<br>fs Desktop<br>f Documents<br>fs Downloads<br>Oe sLibrary<br>fs Movies<br>Of Music<br>fe Opt<br><!-- End of picture text -->



f= Applications fs Desktop fs Documents fs Downloads Oe sLibrary fs Movies f Music fe Opt 





<!-- Start of picture text -->
—<br>Meguatexka Photo Booth Menuatexa ®...0.photoslibrary /Users/macbo...1366x7/68.jpg<br>/Users/macbo...allpapper.png<br><!-- End of picture text -->





<!-- Start of picture text -->
Applications<br>Desktop<br>Documents<br>Downloads<br>Library<br>Movies<br>Music<br>Opt<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `show_hidden_files` 

Shows hidden files. 

_`show_hidden_files`_ is an `BooleanProperty` and defaults to _False_ . 

###### `sort_by` 

It can take the values ‘nothing’ ‘name’ ‘date’ ‘size’ ‘type’ - sorts files by option. By default, sort by name. Available options are: _‘nothing’_ , _‘name’_ , _‘date’_ , _‘size’_ , _‘type’_ . 

_`sort_by`_ is an `OptionProperty` and defaults to _name_ . 

```
sort_by_desc
```

Sort by descending. 

_`sort_by_desc`_ is an `BooleanProperty` and defaults to _False_ . 

###### `selector` 

It can take the values ‘any’ ‘file’ ‘folder’ ‘multi’ By default, any. Available options are: _‘any’_ , _‘file’_ , _‘folder’_ , _‘multi’_ . 

_`selector`_ is an `OptionProperty` and defaults to _any_ . 

###### `selection` 

Contains the list of files that are currently selected. 

_`selection`_ is a read-only `ListProperty` and defaults to _[]_ . 

###### `selection_button` 

The instance of the directory/path selection button. 

Added in version 1.1.0. 

_`selection_button`_ is a read-only `ObjectProperty` and defaults to _None_ . 

`show_disks()` _→_ None 

`show(` _path: str_ `)` _→_ None 

Forms the body of a directory tree. 

###### **Parameters** 

`path` – The path to the directory that will be opened in the file manager. 

`get_access_string(` _path: str_ `)` _→_ str 

- `get_content()` _→_ Tuple[List[str], List[str]] | Tuple[None, None] 

   - Returns a list of the type [[Folder List], [file list]]. 

- `close()` _→_ None 

Closes the file manager window. 

- `select_dir_or_file(` _path: str_ , _widget: MDFileManagerItemPreview | MDFileManagerItem_ `)` _→_ None Called by tap on the name of the directory or file. 

- `back()` _→_ None 

Returning to the branch down in the directory tree. 

- `select_directory_on_press_button(` _*args_ `)` _→_ None 

Called when a click on a floating button. 

- `on_icon(` _instance_file_manager_ , _icon_name: str_ `)` _→_ None 

   - Called when the _`icon`_ property is changed. 

**2.3. Components** 

**261** 

**KivyMD, Release 2.0.1.dev0** 

`on_background_color_toolbar(` _instance_file_manager_ , _color: str | list_ `)` _→_ None Called when the _`background_color_toolbar`_ property is changed. 

`on_pre_open(` _*args_ `)` _→_ None Default pre-open event handler. Added in version 1.1.0. 

`on_open(` _*args_ `)` _→_ None Default open event handler. Added in version 1.1.0. `on_pre_dismiss(` _*args_ `)` _→_ None Default pre-dismiss event handler. Added in version 1.1.0. `on_dismiss(` _*args_ `)` _→_ None Default dismiss event handler. Added in version 1.1.0. 

###### **2.3.30 RefreshLayout** 

###### **Example** 

Declarative Python style with KV 

```
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.uix.listimport(
MDListItem,MDListItemHeadlineText,MDListItemTrailingIcon
)
importasynckivy
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
orientation:'vertical'
MDTopAppBar:
MDTopAppBarLeadingButtonContainer:
MDActionTopAppBarButton:
icon:'menu'
```

(continues on next page) 

**Chapter 2. Contents** 

**262** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDTopAppBarTitle:
text:'ExampleRefreshLayout'
MDScrollViewRefreshLayout:
id:refresh_layout
refresh_callback:app.refresh_callback
root_layout:root
spinner_color:"brown"
circle_color:"white"
MDGridLayout:
id:box
adaptive_height:True
cols:1
'''
classExample(MDApp):
x=0
y=15
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
returnBuilder.load_string(KV)
defon_start(self):
self.set_list()
defset_list(self):
asyncdefset_list():
names_icons_list=list(md_icons.keys())[self.x:self.y]
forname_iconinnames_icons_list:
awaitasynckivy.sleep(0)
self.root.ids.box.add_widget(
MDListItem(
MDListItemHeadlineText(
text=name_icon
),
MDListItemTrailingIcon(
icon=name_icon
)
)
)
asynckivy.start(set_list())
defrefresh_callback(self,*args):
'''
Amethodthatupdatesthestateofyourapplication
whilethespinnerremainsonthescreen.
```

(continues on next page) 

**2.3. Components** 

**263** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
'''
defrefresh_callback(interval):
self.root.ids.box.clear_widgets()
ifself.x==0:
self.x,self.y=15,30
else:
self.x,self.y=0,15
self.set_list()
self.root.ids.refresh_layout.refresh_done()
self.tick=0
```

```
Clock.schedule_once(refresh_callback,1)
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.gridlayoutimportMDGridLayout
fromkivymd.uix.refreshlayoutimportMDScrollViewRefreshLayout
fromkivymd.uix.listimport(
MDListItem,MDListItemHeadlineText,MDListItemTrailingIcon
)
fromkivymd.uix.appbarimport(
MDTopAppBar,
MDTopAppBarLeadingButtonContainer,
MDActionTopAppBarButton,
MDTopAppBarTitle,
)
importasynckivy
classExample(MDApp):
x=0
y=15
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
return(
MDFloatLayout(
MDBoxLayout(
MDTopAppBar(
MDTopAppBarLeadingButtonContainer(
```

(continues on next page) 

**Chapter 2. Contents** 

**264** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDActionTopAppBarButton(
icon='menu'
)
),
MDTopAppBarTitle(
text='ExampleRefreshLayout'
)
),
MDScrollViewRefreshLayout(
MDGridLayout(
id="box",
adaptive_height=True,
cols=1,
),
id="refresh_layout",
refresh_callback=self.refresh_callback,
spinner_color="red",
circle_color="white",
),
orientation='vertical'
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_start(self):
self.root.get_ids().refresh_layout.root_layout=self.root
self.set_list()
defset_list(self):
asyncdefset_list():
names_icons_list=list(md_icons.keys())[self.x:self.y]
forname_iconinnames_icons_list:
awaitasynckivy.sleep(0)
self.root.get_ids().box.add_widget(
MDListItem(
MDListItemHeadlineText(
text=name_icon
),
MDListItemTrailingIcon(
icon=name_icon
)
)
)
asynckivy.start(set_list())
defrefresh_callback(self,*args):
'''
Amethodthatupdatesthestateofyourapplication
whilethespinnerremainsonthescreen.
'''
```

(continues on next page) 

**2.3. Components** 

**265** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defrefresh_callback(interval):
self.root.get_ids().box.clear_widgets()
ifself.x==0:
self.x,self.y=15,30
else:
self.x,self.y=0,15
self.set_list()
self.root.get_ids().refresh_layout.refresh_done()
self.tick=0
Clock.schedule_once(refresh_callback,1)
Example().run()
```

**API -** `kivymd.uix.refreshlayout.refreshlayout` 

`class kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout(` _*args_ , _**kwargs_ `)` Refresh layout class. 

For more information, see in the _`MDScrollView`_ and _`ThemableBehavior`_ class documentation. 

###### `root_layout` 

The spinner will be attached to this layout. 

_`root_layout`_ is a `ObjectProperty` and defaults to _None_ . 

###### `refresh_callback` 

The method that will be called at the on_touch_up event, provided that the overscroll of the list has been registered. 

_`refresh_callback`_ is a `ObjectProperty` and defaults to _None_ . 

###### `spinner_color` 

Color of the spinner in (r, g, b, a) or string format. 

Added in version 1.2.0. 

_`spinner_color`_ is a `ColorProperty` and defaults to _[1, 1, 1, 1]_ . 

```
circle_color
```

Color of the ellipse around the spinner in (r, g, b, a) or string format. 

Added in version 1.2.0. 

_`circle_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `show_transition` 

Transition of the spinner’s opening. 

Added in version 1.2.0. 

_`show_transition`_ is a `StringProperty` and defaults to _‘out_elastic’_ . 

**Chapter 2. Contents** 

**266** 



<!-- Start of picture text -->
aCoyotesAdaptablein Creatures:North 1 = 4<br>Genetic code for a<br>o ® * ah<br>Navigation bars offer a persistent and convenient way »<br>to switch between primary destinations in an app. — ae5<br><!-- End of picture text -->







<!-- Start of picture text -->
MDNavigationBar MDNavigationitem MDNavigationltemicon<br>e Al A A |<br>Label Label Label<br>MDNavigationltemLabel<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.navigationbarimportMDNavigationBar,MDNavigationItem
fromkivymd.uix.screenimportMDScreen
classBaseMDNavigationItem(MDNavigationItem):
icon=StringProperty()
text=StringProperty()
classBaseScreen(MDScreen):
image_size=StringProperty()
KV='''
<BaseMDNavigationItem>
MDNavigationItemIcon:
icon:root.icon
MDNavigationItemLabel:
text:root.text
<BaseScreen>
FitImage:
source:f"https://picsum.photos/{root.image_size}/{root.image_size}"
size_hint:.9,.9
pos_hint:{"center_x":.5,"center_y":.5}
radius:dp(24)
MDBoxLayout:
orientation:"vertical"
md_bg_color:self.theme_cls.backgroundColor
MDScreenManager:
id:screen_manager
BaseScreen:
name:"Screen1"
image_size:"1024"
BaseScreen:
name:"Screen2"
```

(continues on next page) 

**2.3. Components** 

**269** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
image_size:"800"
BaseScreen:
name:"Screen3"
image_size:"600"
MDNavigationBar:
on_switch_tabs:app.on_switch_tabs(*args)
BaseMDNavigationItem
icon:"gmail"
text:"Screen1"
active:True
BaseMDNavigationItem
icon:"twitter"
text:"Screen2"
BaseMDNavigationItem
icon:"linkedin"
text:"Screen3"
'''
classExample(MDApp):
defon_switch_tabs(
self,
bar:MDNavigationBar,
item:MDNavigationItem,
item_icon:str,
item_text:str,
):
self.root.ids.screen_manager.current=item_text
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.navigationbarimport(
MDNavigationBar,
```

(continues on next page) 

**Chapter 2. Contents** 

**270** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationItem,
MDNavigationItemLabel,
MDNavigationItemIcon,
)
fromkivymd.appimportMDApp
classBaseMDNavigationItem(MDNavigationItem):
icon=StringProperty()
text=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.add_widget(MDNavigationItemIcon(icon=self.icon))
self.add_widget(MDNavigationItemLabel(text=self.text))
classBaseScreen(MDScreen):
image_size=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.add_widget(
FitImage(
source=f"https://picsum.photos/{self.image_size}/{self.image_size}",
size_hint=(0.9,0.9),
pos_hint={"center_x":0.5,"center_y":0.5},
radius=dp(24),
),
)
classExample(MDApp):
defon_switch_tabs(
self,
bar:MDNavigationBar,
item:MDNavigationItem,
item_icon:str,
item_text:str,
):
self.root.get_ids().screen_manager.current=item_text
defbuild(self):
returnMDBoxLayout(
MDScreenManager(
BaseScreen(
name="Screen1",
image_size="1024",
),
BaseScreen(
name="Screen2",
image_size="800",
```

(continues on next page) 

**2.3. Components** 

**271** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
),
BaseScreen(
name="Screen3",
image_size="600",
),
id="screen_manager",
),
MDNavigationBar(
BaseMDNavigationItem(
icon="gmail",
text="Screen1",
active=True,
),
BaseMDNavigationItem(
icon="twitter",
text="Screen2",
),
BaseMDNavigationItem(
icon="linkedin",
text="Screen3",
),
on_switch_tabs=self.on_switch_tabs,
),
orientation="vertical",
md_bg_color=self.theme_cls.backgroundColor,
)
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(
'''
MDScreen:
MDBottomNavigation:
MDBottomNavigationItem:
name:'screen1'
```

(continues on next page) 

**Chapter 2. Contents** 

**272** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text:'Mail'
icon:'gmail'
badge_icon:"numeric-10"
MDLabel:
text:'Screen1'
halign:'center'
MDBottomNavigationItem:
name:'screen2'
text:'Twitter'
icon:'twitter'
MDLabel:
text:'Screen2'
halign:'center'
'''
)
Example().run()
```

###### **2.0.0 version** 

MDNavigationBar in version 2.0.0 no longer provides a screen manager for content placement. You have to implement it yourself. This is due to the fact that when using MDNavigationBar and MDTabs widgets at the same time, there were conflicts between their screen managers. 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.navigationbarimportMDNavigationBar,MDNavigationItem
fromkivymd.uix.screenimportMDScreen
classBaseMDNavigationItem(MDNavigationItem):
icon=StringProperty()
text=StringProperty()
classBaseScreen(MDScreen):
...
KV='''
<BaseMDNavigationItem>
MDNavigationItemIcon:
```

(continues on next page) 

**2.3. Components** 

**273** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon:root.icon
MDNavigationItemLabel:
text:root.text
<BaseScreen>
MDLabel:
text:root.name
halign:"center"
MDBoxLayout:
orientation:"vertical"
md_bg_color:self.theme_cls.backgroundColor
MDScreenManager:
id:screen_manager
BaseScreen:
name:"Screen1"
BaseScreen:
name:"Screen2"
MDNavigationBar:
on_switch_tabs:app.on_switch_tabs(*args)
BaseMDNavigationItem
icon:"gmail"
text:"Screen1"
active:True
BaseMDNavigationItem
icon:"twitter"
text:"Screen2"
'''
classExample(MDApp):
defon_switch_tabs(
self,
bar:MDNavigationBar,
item:MDNavigationItem,
item_icon:str,
item_text:str,
):
self.root.ids.screen_manager.current=item_text
defbuild(self):
```

(continues on next page) 

**Chapter 2. Contents** 

**274** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative python style 

```
fromkivy.propertiesimportStringProperty
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.navigationbarimport(
MDNavigationBar,
MDNavigationItem,
MDNavigationItemIcon,
MDNavigationItemLabel,
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classBaseMDNavigationItem(MDNavigationItem):
icon=StringProperty()
text=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
Clock.schedule_once(self.builds)
defbuilds(self,*args):
self.add_widget(
MDNavigationItemIcon(
icon=self.icon
)
)
self.add_widget(
MDNavigationItemLabel(
text=self.text
)
)
```

```
classBaseScreen(MDScreen):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
Clock.schedule_once(self.builds)
defbuilds(self,*args):
self.add_widget(
MDLabel(
```

(continues on next page) 

**2.3. Components** 

**275** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text=self.name,
halign="center",
)
)
classExample(MDApp):
defon_switch_tabs(
self,
bar:MDNavigationBar,
item:MDNavigationItem,
item_icon:str,
item_text:str,
):
self.root.get_ids().screen_manager.current=item_text
defbuild(self):
return(
MDBoxLayout(
MDScreenManager(
BaseScreen(
name="Screen1"
),
BaseScreen(
name="Screen2"
),
id="screen_manager"
),
MDNavigationBar(
BaseMDNavigationItem(
icon="gmail",
text="Screen1",
active=True,
),
BaseMDNavigationItem(
icon="twitter",
text="Screen2",
),
on_switch_tabs=lambda*args:self.on_switch_tabs(*args)
),
orientation="vertical",
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**276** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.navigationbar.navigationbar` 

- `class kivymd.uix.navigationbar.navigationbar.MDNavigationItemLabel(` _*args_ , _**kwargs_ `)` 

Implements a text label for the _`MDNavigationItem`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ class documentation. 

###### `text_color_active` 

Item icon color in (r, g, b, a) or string format. 

_`text_color_active`_ is a `ColorProperty` and defaults to _None_ . 

###### `text_color_normal` 

Item icon color in (r, g, b, a) or string format. 

_`text_color_normal`_ is a `ColorProperty` and defaults to _None_ . 

###### `class kivymd.uix.navigationbar.navigationbar.MDNavigationItemIcon(` _*args_ , _**kwargs_ `)` 

Implements a icon for the _`MDNavigationItem`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDIcon`_ class documentation. 

###### `icon_color_active` 

Item icon color in (r, g, b, a) or string format. 

_`icon_color_active`_ is a `ColorProperty` and defaults to _None_ . 

###### `icon_color_normal` 

Item icon color in (r, g, b, a) or string format. 

_`icon_color_normal`_ is a `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.navigationbar.navigationbar.MDNavigationItem(` _*args_ , _**kwargs_ `)` 

Bottom item class. 

For more information, see in the _`DeclarativeBehavior`_ and _`RectangularRippleBehavior`_ and `AnchorLayout` and `ButtonBehavior` classes documentation. 

Changed in version 2.0.0: Rename class from _MDBottomNavigationItem_ to _MDNavigationItem_ . 

###### `active` 

Indicates if the bar item is active or inactive. 

_`active`_ is a `BooleanProperty` and defaults to _False_ . 

###### `indicator_color` 

The background color in (r, g, b, a) or string format of the highlighted item. 

Added in version 1.0.0. 

Changed in version 2.0.0: Rename property from _selected_color_background_ to _indicator_color_ . 

_`indicator_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `indicator_transition` 

Animation type of the active element indicator. 

_`indicator_transition`_ is an `StringProperty` and defaults to _‘in_out_sine’_ . 

**2.3. Components** 

**277** 

**KivyMD, Release 2.0.1.dev0** 

###### `indicator_duration` 

Duration of animation of the active element indicator. 

_`indicator_duration`_ is an `NumericProperty` and defaults to _0.1_ . 

- `on_active(` _instance_ , _value_ `)` _→_ None 

Fired when the values of _`active`_ change. 

`on_release()` _→_ None 

Fired when clicking on a panel item. 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.navigationbar.navigationbar.MDNavigationBar(` _*args_ , _**kwargs_ `)` 

A navigation bar class. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBoxLayout`_ classes documentation. 

###### **Events** 

_`on_switch_tabs`_ Fired when switching tabs. 

Added in version 1.0.0. 

Changed in version 2.0.0: Rename class from _MDBottomNavigation_ to _MDNavigationBar_ . 

```
set_bars_color
```

If _True_ the background color of the navigation bar will be set automatically according to the current color of the toolbar. 

Added in version 1.0.0. 

_`set_bars_color`_ is an `BooleanProperty` and defaults to _False_ . 

**Chapter 2. Contents** 

**278** 

Carousels showa collection of items that can be scrolled on and off the screen Resources a $% & mm 



<!-- Start of picture text -->
9:30 VAun<br>+ RPE EAM OR es \s ~~<br>gy py eres Soe as<br>BasSat ons Ee 4 a"<br>a ie ie | ce : e<br>A es a cn SP Be = ie<br>gis ee iy [be 7<br>< oe nee Sa ——<br>Your lists<br>a Starred places :<br>Private - 62 places .<br>Labeled -<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

Imperative python style 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.carouselimportMDCarouselItem
fromkivymd.uix.fitimageimportFitImage
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDCarousel:
id:carousel
layouts:"multi-browse"
'''
classExampleApp(MDApp):
defon_start(self):
foriinrange(1,20):
carousel_item=MDCarouselItem()
image=FitImage(
source=f"https://picsum.photos/800/600?random={i}",
radius=[dp(28)],
)
carousel_item.add_widget(image)
self.root.ids.carousel.add_widget(carousel_item)
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
if__name__=="__main__":
ExampleApp().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.carouselimportMDCarousel,MDCarouselItem
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.screenimportMDScreen
classMyCarousel(MDCarousel):
```

(continues on next page) 

**Chapter 2. Contents** 

**280** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
def__init__(self,**kwargs):
super().__init__(**kwargs)
images=[
f"https://picsum.photos/800/600?random={i}"foriinrange(1,20)
]
self.widgets=[
MDCarouselItem(
FitImage(source=img_url,radius=[dp(28)])
)forimg_urlinimages
]
classExampleApp(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnMDScreen(
MyCarousel(
layouts="multi-browse",
),
md_bg_color=self.theme_cls.backgroundColor,
)
if__name__=="__main__":
ExampleApp().run()
```

**2.3. Components** 

**281** 

**KivyMD, Release 2.0.1.dev0** 

###### **Anatomy** 



###### **API -** `kivymd.uix.carousel.carousel` 

- `class kivymd.uix.carousel.carousel.MDCarouselItem(` _*args_ , _**kwargs_ `)` 

   - Implements a item for _`MDCarousel`_ class. 

For more information, see in the _`MDCard`_ class documentation. 

###### **Events** 

###### **_on_slide_left_** 

- Fired when user slides/swipes to the left. 

###### **_on_slide_right_** 

- Fired when user slides/swipes to the right. 

###### **_on_slide_up_** 

- Fired when user slides/swipes up. 

###### **_on_slide_down_** 

- Fired when user slides/swipes down. 

###### **_on_index_** 

Fired when the active slide index changes. 

**Chapter 2. Contents** 

**282** 

**KivyMD, Release 2.0.1.dev0** 

###### `full_screen_radius` 

Corner radius used during scrolling for items in full-screen layout modes. 



_`full_screen_radius`_ is a `NumericProperty` and defaults to _dp(16)_ . 

###### `radius` 

Item radius by default. 

**2.3. Components** 

**283** 



<!-- Start of picture text -->
@ Example<br>1 3<br>os<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

_`padding`_ is an `ListProperty` and defaults to `[dp(16), dp(16), dp(16), dp(16)]` . 

###### `spacing` 

Distance between items in the carousel. 

_`spacing`_ is an `NumericProperty` and defaults to `dp(12)` . 

###### `shrink_extent` 

Size of the collapsed or shrinked extent for trailing items. 

_`shrink_extent`_ is an `NumericProperty` and defaults to `dp(56)` . 

###### `item_snapping` 

If `True` , enables automatic snapping of items to the closest slot upon touch release. 

_`item_snapping`_ is an `BooleanProperty` and defaults to `True` . 

###### `scroll_offset` 

Current scroll offset value of the carousel. 

_`scroll_offset`_ is an `NumericProperty` and defaults to `0` . 

###### `layouts` 

Layout type of the carousel view. 

Available options are: - `"multi-browse"` : Standard layout displaying multiple items of varying sizes. - `"uncontained"` : Items maintain a fixed width and overflow beyond the carousel edge. - `"hero"` : Highlights a single large hero item aligned to the start. - `"center-aligned"` : Displays a centered hero item flanked by smaller preview items. - `"full-screen-horizontal"` : Items occupy the full width and height of the carousel, scrolling horizontally. - `"full-screen-vertical"` : Items occupy the full width and height of the carousel, scrolling vertically. 

_`layouts`_ is an `OptionProperty` and defaults to `"multi-browse"` . 

###### **Multi-browse** 

```
MDCarousel:
layouts:"multi-browse"
```

###### **Uncontained** 

```
MDCarousel:
layouts:"uncontained"
```

**2.3. Components** 

**285** 

**KivyMD, Release 2.0.1.dev0** 

###### **Hero** 

```
MDCarousel:
```

```
layouts:"hero"
```

###### **Center-aligned** 

```
MDCarousel:
layouts:"center-aligned"
```

###### **Full-screen-vertical** 

```
MDCarousel:
layouts:"full-screen-vertical"
```

###### **Full-screen-horizontal** 

```
MDCarousel:
layouts:"full-screen-horizontal"
```

###### `uncontained_item_width` 

Width of individual items when using the `"uncontained"` layout mode. 

_`uncontained_item_width`_ is an `NumericProperty` and defaults to `dp(280)` . 

###### `index` 

Index of the currently active item. 

_`index`_ is an `NumericProperty` and defaults to `0` . 

###### `add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**Chapter 2. Contents** 

**286** 

**KivyMD, Release 2.0.1.dev0** 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

**_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

###### `on_touch_move(` _touch_ `)` 

Receive a touch move event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

###### `on_touch_up(` _touch_ `)` 

Receive a touch up event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

###### `on_index(` _instance_ , _value_ `)` 

Fired when the active slide index changes. 

###### `on_slide_left()` 

Fired when user slides/swipes to the left. 

###### `on_slide_right()` 

Fired when user slides/swipes to the right. 

###### `on_slide_up()` 

Fired when user slides/swipes up. 

###### `on_slide_down()` 

Fired when user slides/swipes down. 

**2.3. Components** 

**287** 



<!-- Start of picture text -->
+ Enabled Enabled<br><!-- End of picture text -->

Enabled Q 



<!-- Start of picture text -->
Enabled Enabled<br>Y Selected Enabled Enabled<br><!-- End of picture text -->



<!-- Start of picture text -->
WA @ Enabled<br><!-- End of picture text -->



<!-- Start of picture text -->
+ Elevated tried) Tonal Text<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonIcon,MDButtonText
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
return(
MDScreen(
MDButton(
MDButtonIcon(
icon="plus",
),
MDButtonText(
text="Elevated",
),
style="elevated",
pos_hint={"center_x":0.5,"center_y":0.5},
),
md_bg_color=self.theme_cls.surfaceColor,
)
)
Example().run()
```

Common buttons can contain an icon or be without an icon: 

```
MDButton:
```

```
style:"elevated"
text:"Elevated"
```

**Chapter 2. Contents** 

**290** 

**KivyMD, Release 2.0.1.dev0** 



###### **Filled** 

```
MDButton:
style:"filled"
MDButtonText:
text:"Filled"
```

###### **Tonal** 

```
MDButton:
style:"tonal"
MDButtonText:
text:"Tonal"
```

###### **Outlined** 

```
MDButton:
style:"outlined"
MDButtonText:
text:"Outlined"
```

**2.3. Components** 

**291** 

**KivyMD, Release 2.0.1.dev0** 

###### **Text** 

```
MDButton:
style:"text"
MDButtonText:
text:"Text"
```

###### **Customization of buttons** 

###### **Text positioning and button size** 

```
MDButton:
style:"tonal"
theme_width:"Custom"
height:"56dp"
size_hint_x:.5
MDButtonIcon:
x:text.x-(self.width+dp(10))
icon:"plus"
MDButtonText:
id:text
text:"Tonal"
pos_hint:{"center_x":.5,"center_y":.5}
```



###### **Font of the button text** 

```
MDButton:
style:"filled"
MDButtonIcon:
icon:"plus"
MDButtonText:
```

(continues on next page) 

**Chapter 2. Contents** 

**292** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text:"Filled"
font_style:"Title"
```



```
MDButton:
style:"elevated"
MDButtonText:
text:"Elevated"
theme_font_name:"Custom"
font_name:"path/to/font.ttf"
```



###### **Custom button color** 

```
MDButton:
style:"elevated"
theme_shadow_color:"Custom"
shadow_color:"red"
MDButtonIcon:
icon:"plus"
theme_icon_color:"Custom"
icon_color:"green"
```

(continues on next page) 

**2.3. Components** 

**293** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDButtonText:
text:"Elevated"
theme_text_color:"Custom"
text_color:"red"
```



###### **Icon buttons** 

**Use icon buttons when a compact button is required, such as in a toolbar or image list. There are two types of icon buttons: standard and contained.** 

###### **See also:** 

Material Design spec, Icon buttons 



1. Standard icon button 

2. Contained icon button (including filled, filled tonal, and outlined styles) 

_StandardIcon FilledIcon TonalIcon OutlinedIcon_ 

**Chapter 2. Contents** 

**294** 

**KivyMD, Release 2.0.1.dev0** 

###### **StandardIcon** 

```
MDIconButton:
icon:"heart-outline"
style:"standard"
```

###### **FilledIcon** 

###### <u>`MDIconButton:`</u> 

```
icon:"heart-outline"
style:"filled"
```

###### **TonalIcon** 

```
MDIconButton:
icon:"heart-outline"
style:"tonal"
```

###### **OutlinedIcon** 

```
MDIconButton:
```

```
icon:"heart-outline"
style:"outlined"
```

###### **Custom icon size** 

###### <u>`MDIconButton:`</u> 

```
icon:"heart-outline"
style:"tonal"
theme_font_size:"Custom"
font_size:"48sp"
radius:[self.height/2,]
size_hint:None,None
size:"84dp","84dp"
```

**2.3. Components** 

**295** 











~~r~~ e 

**KivyMD, Release 2.0.1.dev0** 



###### **Large** 

###### <u>`MDFabButton:`</u> 

```
icon:"pencil-outline"
style:"large"
```

###### **Additional color mappings** 

FABs can use other combinations of container and icon colors. The color mappings below provide the same legibility and functionality as the default, so the color mapping you use depends on style alone. 



1. Surface 

2. Secondary 

3. Tertiary 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDFabButton
```

(continues on next page) 

**Chapter 2. Contents** 

**298** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
md_bg_color:app.theme_cls.surfaceColor
MDBoxLayout:
id:box
adaptive_size:True
spacing:"32dp"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
returnBuilder.load_string(KV)
defon_start(self):
styles={
"standard":"surface",
"small":"secondary",
"large":"tertiary",
}
forstyleinstyles.keys():
self.root.ids.box.add_widget(
MDFabButton(
style=style,icon="pencil-outline",color_map=styles[style]
)
)
Example().run()
```



**2.3. Components** 

**299** 



<!-- Start of picture text -->
A Navigate Reroute<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.theme_cls.primary_palette="Green"
returnBuilder.load_string(KV)
```

```
Example().run()
```

###### **Without icon** 

###### <u>`MDExtendedFabButton:`</u> 

```
fab_state:"expand"
```

```
MDExtendedFabButtonText:
text:"Compose"
```



###### **API break** 

###### **1.2.0 version** 

```
MDFloatingActionButton:
icon:"plus"
```

###### <u>`MDRoundFlatButton:`</u> 

```
text:"Outlined"
```

###### <u>`MDRoundFlatIconButton:`</u> 

```
text:"Outlinedwithicon"
icon:"plus"
```

```
MDFillRoundFlatButton
text:"Filled"
```

**2.3. Components** 

**301** 

**KivyMD, Release 2.0.1.dev0** 

```
MDFillRoundFlatIconButton
text:"Filledwithicon"
icon:"plus"
```

###### **2.0.0 version** 

**Note:** _MDFloatingActionButtonSpeedDial_ type buttons were removed in version _2.0.0_ . 

###### <u>`MDFabButton:`</u> 

```
icon:"plus"
```

```
MDButton:
style:"outlined"
MDButtonText:
text:"Outlined"
```

```
MDButton:
style:"outlined"
MDButtonIcon:
icon:"plus"
MDButtonText:
text:"Outlinedwithicon"
```

```
MDButton:
style:"filled"
MDButtonText:
text:"Filled"
```

```
MDButton:
```

```
style:"filled"
MDButtonIcon:
icon:"plus"
MDButtonText:
text:"Filled"
```

**Chapter 2. Contents** 

**302** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.button.button` 

```
classkivymd.uix.button.button.BaseFabButton
```

Implements the basic properties for the _`MDExtendedFabButton`_ and _`MDFabButton`_ classes. 

Added in version 2.0.0. 

###### `elevation_levels` 

Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps). 

Added in version 1.2.0. 

_`elevation_levels`_ is an `DictProperty` and defaults to _{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}_ . 

###### `color_map` 

Additional color mappings. 

Available options are: ‘surface’, ‘secondary’, ‘tertiary’. 

_`color_map`_ is an `OptionProperty` and defaults to _‘secondary’_ . 

###### `icon_color_disabled` 

The icon color in (r, g, b, a) or string format of the list item when the widget item is disabled. 

_`icon_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

###### `style` 

Button type. 

Available options are: ‘standard’, ‘small’, ‘large’. 

_`style`_ is an `OptionProperty` and defaults to _‘standard’_ . 

###### `fab_state` 

The state of the button. 

Available options are: ‘collapse’ or ‘expand’. 

_`fab_state`_ is an `OptionProperty` and defaults to “collapse”. 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the list item when the list button is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

###### `radius` 

Canvas radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(16), dp(16), dp(16), dp(16)]_ . 

`class kivymd.uix.button.button.BaseButton(` _*args_ , _**kwargs_ `)` 

Base button class. 

For more information, see in the _`DeclarativeBehavior`_ and _`BackgroundColorBehavior`_ and _`RectangularRippleBehavior`_ and `ButtonBehavior` and _`ThemableBehavior`_ and _`StateLayerBehavior`_ classes documentation. 

**2.3. Components** 

**303** 

**KivyMD, Release 2.0.1.dev0** 

###### `elevation_levels` 

Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps). 

Added in version 1.2.0. 

_`elevation_levels`_ is an `DictProperty` and defaults to _{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}_ . 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the button when the button is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

###### `shadow_radius` 

Button shadow radius. 

_`shadow_radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `md_bg_color` 

Button background color in (r, g, b, a) or string format. 

_`md_bg_color`_ is a `ColorProperty` and defaults to _None_ . 

```
line_color
```

Outlined color. 

_`line_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `line_width` 

Line width for button border. 

_`line_width`_ is a `NumericProperty` and defaults to _1_ . 

- `on_press(` _*args_ `)` _→_ None 

Fired when the button is pressed. 

- `on_release(` _*args_ `)` _→_ None 

Fired when the button is released (i.e. the touch/click that pressed the button goes away). 

`on_touch_down(` _touch_ `)` 

```
finish_ripple()
```

- `class kivymd.uix.button.button.MDButton(` _*args_ , _**kwargs_ `)` 

Base class for all buttons. 

Added in version 2.2.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`BaseButton`_ and `RelativeLayout` classes documentation. 

###### `style` 

Button type. 

Available options are: ‘filled’, ‘elevated’, ‘outlined’, ‘tonal’, ‘text’. 

_`style`_ is an `OptionProperty` and defaults to _‘elevated’_ . 

###### `radius` 

Button radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(20), dp(20), dp(20), dp(20)]_ . 

**Chapter 2. Contents** 

**304** 

**KivyMD, Release 2.0.1.dev0** 

###### `adjust_pos(` _*args_ `)` _→_ None 

Adjusts the pos of the button according to the content. 

###### `adjust_width(` _*args_ `)` _→_ None 

Adjusts the width of the button according to the content. 

###### `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

- **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### `set_properties_widget()` _→_ None 

Fired _on_release/on_press/on_enter/on_leave_ events. 

- `on_disabled(` _instance_ , _value_ `)` _→_ None 

Fired when the _disabled_ value changes. 

- `class kivymd.uix.button.button.MDButtonText(` _*args_ , _**kwargs_ `)` 

The class implements the text for the _`MDButton`_ class. 

For more information, see in the _`MDLabel`_ class documentation. 

- `class kivymd.uix.button.button.MDButtonIcon(` _*args_ , _**kwargs_ `)` 

The class implements an icon for the _`MDButton`_ class. 

For more information, see in the _`MDIcon`_ class documentation. 

- `class kivymd.uix.button.button.MDIconButton(` _**kwargs_ `)` 

Base class for icon buttons. 

For more information, see in the _`RectangularRippleBehavior`_ and `ButtonBehavior` and `MDIcon` classes documentation. 

**2.3. Components** 

**305** 

**KivyMD, Release 2.0.1.dev0** 

###### `style` 

Button type. 

Added in version 2.0.0. 

Available options are: ‘standard’, ‘filled’, ‘tonal’, ‘outlined’. 

_`style`_ is an `OptionProperty` and defaults to _‘standard’_ . 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the list item when the list button is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

- `on_line_color(` _instance_ , _value_ `)` _→_ None 

Fired when the values of `line_color` change. 

- `class kivymd.uix.button.button.MDFabButton(` _**kwargs_ `)` 

Base class for FAB buttons. 

For more information, see in the _`BaseFabButton`_ and _`CommonElevationBehavior`_ and _`RectangularRippleBehavior`_ and `ButtonBehavior` and _`MDIcon`_ classes documentation. 

`on_press(` _*args_ `)` _→_ None 

Fired when the button is pressed. 

- `on_release(` _*args_ `)` _→_ None 

Fired when the button is released (i.e. the touch/click that pressed the button goes away). 

- `set_properties_widget()` _→_ None 

Fired _on_release/on_press/on_enter/on_leave_ events. 

`class kivymd.uix.button.button.MDExtendedFabButtonIcon(` _*args_ , _**kwargs_ `)` 

Implements an icon for the _`MDExtendedFabButton`_ class. 

Added in version 2.0.0. 

- `class kivymd.uix.button.button.MDExtendedFabButtonText(` _*args_ , _**kwargs_ `)` 

Implements the text for the class _`MDExtendedFabButton`_ class. 

Added in version 2.0.0. 

- `class kivymd.uix.button.button.MDExtendedFabButton(` _*args_ , _**kwargs_ `)` 

Base class for Extended FAB buttons. 

Added in version 2.0.0. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`MotionExtendedFabButtonBehavior`_ and _`CommonElevationBehavior`_ and _`StateLayerBehavior`_ and _`BaseFabButton`_ and `ButtonBehavior` and `RelativeLayout` classes documentation. 

###### **Events** 

###### **_on_collapse_** 

Fired when the button is collapsed. 

###### **_on_expand_** 

Fired when the button is expanded. 

**Chapter 2. Contents** 

**306** 

**KivyMD, Release 2.0.1.dev0** 

###### `elevation_levels` 

Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps). 

Added in version 1.2.0. 

_`elevation_levels`_ is an `DictProperty` and defaults to _{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}_ . 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

**_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### `on_collapse(` _*args_ `)` 

Fired when the button is collapsed. 

###### `on_expand(` _*args_ `)` 

Fired when the button is expanded. 

`on_fab_state(` _instance_ , _state: str_ `)` _→_ None 

Fired when the `fab_state` value changes. 

`on__x(` _instance_ , _value_ `)` _→_ None 

**2.3. Components** 

**307** 



<!-- Start of picture text -->
07:00 *<br>rT<br>Ti e 2<br>ime pickers -,<br>Time pickers help users select and set a specific time<br>Q.:<br>«<br><!-- End of picture text -->



<!-- Start of picture text -->
07:00 AM«. ; VW 2 1 » —_[07iJ: 00 |AM<br>07:. 00 9 ; 3 _——<br>n 2, = = : 4 © Cancel 0K<br>10 2 6 5<br>93<br>a4 (i) Cancel OK<br>6 5<br>B Cancel OK<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **MDTimePickerDialVertical** 

Time pickers allow people to enter a specific time value. They’re displayed in dialogs and can be used to select hours, minutes, or periods of time. 

They can be used for a wide range of scenarios. Common use cases include: 

- Setting an alarm 

- Scheduling a meeting 

Time pickers are not ideal for nuanced or granular time selection, such as milliseconds for a stopwatch application. 

###### Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDTimePickerDialVertical
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_time_picker()
MDButtonText:
text:"Opentimepicker"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defshow_time_picker(self):
time_picker=MDTimePickerDialVertical()
time_picker.open()
Example().run()
```

###### Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDTimePickerDialVertical
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
```

(continues on next page) 

**2.3. Components** 

**309** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `def build(self): self.theme_cls.theme_style = "Dark" return ( MDScreen( MDButton( MDButtonText( text="Open time picker", ), pos_hint={'center_x': .5, 'center_y': .5}, on_release=self.show_time_picker, ), md_bg_color=self.theme_cls.backgroundColor, ) ) def show_time_picker(self, *args): time_picker = MDTimePickerDialVertical() time_picker.open() Example().run()` 

###### **MDTimePickerDialHorizontal** 

The clock dial interface adapts to a device’s orientation. In landscape mode, the stacked input and selection options are positioned side-by-side. 

```
defshow_time_picker(self):
MDTimePickerDialHorizontal().open()
```

**Note:** You must control the orientation of the time picker yourself. 

Declarative KV style 

```
fromtypingimportLiteral
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivy.propertiesimportObjectProperty
fromkivymd.appimportMDApp
fromkivymd.themingimportThemeManager
fromkivymd.uix.pickersimport(
MDTimePickerDialHorizontal,
MDTimePickerDialVertical,
)
KV='''
```

(continues on next page) 

**Chapter 2. Contents** 

**310** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`MDScreen: md_bg_color: self.theme_cls.backgroundColor MDButton: pos_hint: {'center_x': .5, 'center_y': .5} on_release: app.open_time_picker_horizontal("1", "10")` _˓→_ `theme_cls.device_orientation == "landscape" else` _˓→_ `picker_vertical("1", "10") MDButtonText: text: "Open time picker" ''' class Example(MDApp): ORIENTATION = Literal["portrait", "landscape"] time_picker_horizontal: MDTimePickerDialHorizontal = ObjectProperty( allownone=True ) time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty( allownone=True ) def build(self): self.theme_cls.theme_style = "Dark" self.theme_cls.bind(device_orientation=self.check_orientation) return Builder.load_string(KV) def check_orientation( self, instance: ThemeManager, orientation: ORIENTATION ): if orientation == "portrait" and self.time_picker_horizontal: self.time_picker_horizontal.dismiss() hour = str(self.time_picker_horizontal.time.hour) minute = str(self.time_picker_horizontal.time.minute) Clock.schedule_once( lambda x: self.open_time_picker_vertical(hour, minute), 0.1, ) elif orientation == "landscape" and self.time_picker_vertical: self.time_picker_vertical.dismiss() hour = str(self.time_picker_vertical.time.hour) minute = str(self.time_picker_vertical.time.minute) Clock.schedule_once( lambda x: self.open_time_picker_horizontal(hour, minute), 0.1, ) def open_time_picker_horizontal(self, hour, minute): self.time_picker_vertical = None self.time_picker_horizontal = MDTimePickerDialHorizontal(` 

```
ifself.
app.open_time_
```

(continues on next page) 

**2.3. Components** 

**311** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
hour=hour,minute=minute
)
self.time_picker_horizontal.open()
defopen_time_picker_vertical(self,hour,minute):
self.time_picker_horizontal=None
self.time_picker_vertical=MDTimePickerDialVertical(
hour=hour,minute=minute
)
self.time_picker_vertical.open()
```

```
Example().run()
```

Declarative Python style 

```
fromtypingimportLiteral
fromkivy.clockimportClock
fromkivy.propertiesimportObjectProperty
fromkivymd.appimportMDApp
fromkivymd.themingimportThemeManager
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimport(
MDTimePickerDialHorizontal,
MDTimePickerDialVertical,
)
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
ORIENTATION=Literal["portrait","landscape"]
time_picker_horizontal:MDTimePickerDialHorizontal=ObjectProperty(
allownone=True
)
time_picker_vertical:MDTimePickerDialHorizontal=ObjectProperty(
allownone=True
)
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.bind(device_orientation=self.check_orientation)
returnMDScreen(
MDButton(
MDButtonText(
text="Opentimepicker",
),
pos_hint={"center_x":0.5,"center_y":0.5},
on_release=self.show_time_picker,
),
md_bg_color=self.theme_cls.backgroundColor,
```

(continues on next page) 

**Chapter 2. Contents** 

**312** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
)
defshow_time_picker(self,*args):
(
self.open_time_picker_horizontal("1","10")
ifself.theme_cls.device_orientation=="landscape"
elseself.open_time_picker_vertical("1","10")
)
defcheck_orientation(
self,instance:ThemeManager,orientation:ORIENTATION
):
iforientation=="portrait"andself.time_picker_horizontal:
self.time_picker_horizontal.dismiss()
hour=str(self.time_picker_horizontal.time.hour)
minute=str(self.time_picker_horizontal.time.minute)
Clock.schedule_once(
lambdax:self.open_time_picker_vertical(hour,minute),
0.1,
)
eliforientation=="landscape"andself.time_picker_vertical:
self.time_picker_vertical.dismiss()
hour=str(self.time_picker_vertical.time.hour)
minute=str(self.time_picker_vertical.time.minute)
Clock.schedule_once(
lambdax:self.open_time_picker_horizontal(hour,minute),
0.1,
)
defopen_time_picker_horizontal(self,hour,minute):
self.time_picker_vertical=None
self.time_picker_horizontal=MDTimePickerDialHorizontal(
hour=hour,minute=minute
)
self.time_picker_horizontal.open()
defopen_time_picker_vertical(self,hour,minute):
self.time_picker_horizontal=None
self.time_picker_vertical=MDTimePickerDialVertical(
hour=hour,minute=minute
)
self.time_picker_vertical.open()
```

```
Example().run()
```

**2.3. Components** 

**313** 

**KivyMD, Release 2.0.1.dev0** 

###### **MDTimePickerInput** 

Time input pickers allow people to specify a time using keyboard numbers. This input option should be accessible from any other mobile time picker interface by tapping the keyboard icon. 

```
defshow_time_picker(self):
MDTimePickerInput().open()
```

###### **Events** 

###### **on_edit event** 

Declarative KV style 

```
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDTimePickerDialVertical,MDTimePickerInput
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_time_picker_vertical()
MDButtonText:
text:"Opentimepicker"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_edit_time_picker_input(self,time_picker_input):
time_picker_input.dismiss()
Clock.schedule_once(self.show_time_picker_vertical,0.2)
defshow_time_picker_input(self,*args):
time_picker_input=MDTimePickerInput()
time_picker_input.bind(on_edit=self.on_edit_time_picker_input)
time_picker_input.open()
defon_edit_time_picker_vertical(self,time_picker_vertical):
time_picker_vertical.dismiss()
Clock.schedule_once(self.show_time_picker_input,0.2)
```

(continues on next page) 

**Chapter 2. Contents** 

**314** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_edit=self.on_edit_time_picker_vertical)
time_picker_vertical.open()
```

```
Example().run()
```

Declarative Python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimport(
MDTimePickerDialVertical,MDTimePickerInput,
)
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnMDScreen(
MDButton(
MDButtonText(
text="Opentimepicker",
),
pos_hint={"center_x":0.5,"center_y":0.5},
on_release=self.show_time_picker_vertical,
),
md_bg_color=self.theme_cls.backgroundColor,
)
defon_edit_time_picker_input(self,time_picker_input):
time_picker_input.dismiss()
Clock.schedule_once(self.show_time_picker_vertical,0.2)
defshow_time_picker_input(self,*args):
time_picker_input=MDTimePickerInput()
time_picker_input.bind(on_edit=self.on_edit_time_picker_input)
time_picker_input.open()
defon_edit_time_picker_vertical(self,time_picker_vertical):
time_picker_vertical.dismiss()
Clock.schedule_once(self.show_time_picker_input,0.2)
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_edit=self.on_edit_time_picker_vertical)
time_picker_vertical.open()
```

(continues on next page) 

**2.3. Components** 

**315** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

###### **on_hour_select event** 

```
defon_hour_select(
self,time_picker_vertical:MDTimePickerDialVertical,mode:str
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"On'{mode}'select",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_hour_select=self.on_hour_select)
time_picker_vertical.open()
```

###### **on_minute_select event** 

```
defon_minute_select(
self,time_picker_vertical:MDTimePickerDialVertical,mode:str
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"On'{mode}'select",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_minute_select=self.on_minute_select)
time_picker_vertical.open()
```

**Chapter 2. Contents** 

**316** 

**KivyMD, Release 2.0.1.dev0** 

###### **on_am_pm event** 

```
defon_am_pm(
self,time_picker_vertical:MDTimePickerDialVertical,am_pm:str
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"'{am_pm.upper()}'select",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_am_pm=self.on_am_pm)
time_picker_vertical.open()
```

###### **on_selector_hour event** 

```
defon_selector_hour(
self,time_picker_vertical:MDTimePickerDialVertical,hour:str
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"Thevalueofthehouris�{hour}�select",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_selector_hour=self.on_selector_hour)
time_picker_vertical.open()
```

**2.3. Components** 

**317** 

**KivyMD, Release 2.0.1.dev0** 

###### **on_selector_minute event** 

```
defon_selector_minute(
self,time_picker_vertical:MDTimePickerDialVertical,minute:str
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"Thevalueofthehouris�{minute}�select",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_selector_minute=self.on_selector_minute)
time_picker_vertical.open()
```

###### **on_cancel event** 

```
defon_cancel(
self,time_picker_vertical:MDTimePickerDialVertical
):
time_picker_vertical.dismiss()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_cancel=self.on_cancel)
time_picker_vertical.open()
```

###### **on_ok event** 

```
defon_ok(
self,time_picker_vertical:MDTimePickerDialVertical
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"Timeis�{time_picker_vertical.time}�",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
```

(continues on next page) 

**Chapter 2. Contents** 

**318** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerDialVertical()
time_picker_vertical.bind(on_ok=self.on_ok)
time_picker_vertical.open()
```

###### **on_time_input event** 

```
defon_time_input(
self,
time_picker_vertical:MDTimePickerInput,
type_time:str,
value:str,
):
MDSnackbar(
MDSnackbarSupportingText(
text=f"The{type_time}valueissetto{value}",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
defshow_time_picker_vertical(self,*args):
time_picker_vertical=MDTimePickerInput()
time_picker_vertical.bind(on_time_input=self.on_time_input)
time_picker_vertical.open()
```

###### **API break** 

###### **1.2.0 version** 

```
time_picker_dialog=MDTimePicker()
time_picker_dialog.open()
```

**2.3. Components** 

**319** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
#time_picker_dialog=MDTimePickerDialVertical()
#time_picker_dialog=MDTimePickerDialHorizontal()
time_picker_dialog=MDTimePickerInput()
time_picker_dialog.open()
```

###### **API -** `kivymd.uix.pickers.timepicker.timepicker` 

`class kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker(` _**kwargs_ `)` 

Implements the base class of the time picker. 

Added in version 2.0.0. 

For more information, see in the _`ThemableBehavior`_ and _`MotionTimePickerBehavior`_ and `BoxLayout` and classes documentation. 

###### **Events** 

_`on_cancel`_ Fired when the ‘Cancel’ button is pressed. 

_`on_ok`_ Fired when the ‘Ok’ button is pressed. 

_`on_dismiss`_ Fired when a date picker closes. 

_`on_edit`_ Fired when you click on the date editing icon. 

```
on_hour_select
```

Fired when the hour input field container is clicked. 

```
on_minute_select
```

Fired when the minute input field container is clicked. 

```
on_am_pm
```

Fired when the AP/PM switching elements are pressed. 

```
on_selector_hour
```

Fired when switching the hour value in the clock face container. 

```
on_selector_minute
```

Fired when switching the minute value in the clock face container. 

###### `hour` 

Current hour. 

_`hour`_ is an `StringProperty` and defaults to _‘12’_ . 

###### `minute` 

Current minute. 

_`minute`_ is an `StringProperty` and defaults to _0_ . 

**Chapter 2. Contents** 

**320** 

**KivyMD, Release 2.0.1.dev0** 

###### `am_pm` 

Current AM/PM mode. 

_`am_pm`_ is an `OptionProperty` and defaults to _‘am’_ . 

###### `animation_duration` 

Duration of the animations. 

_`animation_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `animation_transition` 

Transition type of the animations. 

_`animation_transition`_ is an `StringProperty` and defaults to _‘out_quad’_ . 

###### `time` 

Returns the current time object. 

_`time`_ is an `ObjectProperty` and defaults to _None_ . 

###### `headline_text` 

Headline text. 

_`headline_text`_ is an `StringProperty` and defaults to _‘Select time’_ . 

###### `text_button_ok` 

The text of the confirmation button. 

_`text_button_ok`_ is a `StringProperty` and defaults to _‘Ok’_ . 

###### `text_button_cancel` 

The text of the cancel button. 

_`text_button_cancel`_ is a `StringProperty` and defaults to _‘Cancel’_ . 

###### `radius` 

Container radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(16), dp(16), dp(16), dp(16)]_ . 

###### `is_open` 

Is the date picker dialog open. 

_`is_open`_ is a `BooleanProperty` and defaults to _False_ . 

###### `scrim_color` 

Color for scrim in (r, g, b, a) or string format. 

_`scrim_color`_ is a `ColorProperty` and defaults to _[0, 0, 0, 0.5]_ . 

`set_time(` _time_obj: datetime.time_ `)` _→_ None 

Manually set time dialog with the specified time. 

`open()` _→_ None 

Show the dialog time picker. 

###### `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

**2.3. Components** 

**321** 

**KivyMD, Release 2.0.1.dev0** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

- `dismiss(` _*args_ `)` _→_ None 

Dismiss the dialog time picker. 

- `on_dismiss(` _*args_ `)` _→_ None 

Fired when a time picker closes. 

- `on_cancel(` _*args_ `)` _→_ None 

Fired when the ‘Cancel’ button is pressed. 

- `on_ok(` _*args_ `)` _→_ None 

Fired when the ‘Ok’ button is pressed. 

- `on_hour_select(` _*args_ `)` _→_ None 

Fired when the hour input field container is clicked. 

- `on_minute_select(` _*args_ `)` _→_ None 

Fired when the minute input field container is clicked. 

- `on_am_pm(` _*args_ `)` _→_ None 

Fired when the AP/PM switching elements are pressed. 

- `on_edit(` _*args_ `)` _→_ None 

Fired when you click on the time editing icon. 

- `on_selector_hour(` _*args_ `)` _→_ None 

Fired when switching the hour value in the clock face container. 

- `on_selector_minute(` _*args_ `)` _→_ None 

Fired when switching the minute value in the clock face container. 

- `on_time_input(` _*args_ `)` _→_ None 

Fired when switching the minute value in the clock face container. 

- `class kivymd.uix.pickers.timepicker.timepicker.MDTimePickerInput(` _**kwargs_ `)` 

Implements input time picker. 

- Added in version 2.0.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseTimePicker`_ classes documentation. 

- `class kivymd.uix.pickers.timepicker.timepicker.MDTimePickerDialVertical(` _**kwargs_ `)` 

   - Implements vertical time picker. 

Added in version 2.0.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseTimePicker`_ classes documentation. 

- `class kivymd.uix.pickers.timepicker.timepicker.MDTimePickerDialHorizontal(` _**kwargs_ `)` Implements horizontal time picker. 

   - Added in version 2.0.0. 

   - For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseTimePicker`_ classes documentation. 

**Chapter 2. Contents** 

**322** 



<!-- Start of picture text -->
‘ VAe<br>D t e k Aug 17 - Aug 23 a<br>Date pickers let people select a date, or a range of dates<br><!-- End of picture text -->



<!-- Start of picture text -->
@ Date08/17/2023 @) Select date @® Select date<br>MM/DD/YYYY Mon, Aug 17 Enter dates<br>< Aug ~ > < 202|<br>August 2023 ~ Baie<br>S M T Ww T mm/dd/yyyy Return<br>S M T Ww T<br>26 27 28 29 30<br>Canc<br>2 8) 4 5 6<br>9 10 11 12 13 2 8) 4 (s) 6<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **MDDockedDatePicker** 

Docked datepickers allow the selection of a specific date and year. The docked datepicker displays a date input field by default, and a dropdown calendar appears when the user taps on the input field. Either form of date entry can be interacted with. 

Docked date pickers are ideal for navigating dates in both the near future or past and the distant future or past, as they provide multiple ways to select dates. 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDDockedDatePicker
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDTextField:
id:field
mode:"outlined"
pos_hint:{'center_x':.5,'center_y':.85}
size_hint_x:.5
on_focus:app.show_date_picker(self.focus)
MDTextFieldHintText:
text:"Dockeddatepicker"
MDTextFieldHelperText:
text:"MM/DD/YYYY"
mode:"persistent"
MDTextFieldTrailingIcon:
icon:"calendar"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defshow_date_picker(self,focus):
ifnotfocus:
return
date_dialog=MDDockedDatePicker()
#Youhavetocontrolthepositionofthedatepickerdialogyourself.
date_dialog.pos=[
```

(continues on next page) 

**Chapter 2. Contents** 

**324** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.ids.field.center_x-date_dialog.width/2,
self.root.ids.field.y-(date_dialog.height+dp(32)),
]
date_dialog.open()
```

```
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDDockedDatePicker
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.textfieldimport(
MDTextFieldHintText,
MDTextField,
MDTextFieldHelperText,
MDTextFieldTrailingIcon,
)
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDTextField(
MDTextFieldHintText(
text="Dockeddatepicker"
),
MDTextFieldHelperText(
text="MM/DD/YYYY",
mode="persistent",
),
MDTextFieldTrailingIcon(
icon="calendar"
),
id="field",
mode="outlined",
pos_hint={'center_x':.5,'center_y':0.85},
size_hint_x=0.5,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_start(self):
self.root.get_ids().field.bind(focus=self.show_date_picker)
defshow_date_picker(self,field,focus):
```

(continues on next page) 

**2.3. Components** 

**325** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
iffocus:
date_dialog=MDDockedDatePicker()
#Youhavetocontrolthepositionofthedatepickerdialog
#yourself.
date_dialog.pos=[
field.center_x-date_dialog.width/2,
field.y-(date_dialog.height+dp(32)),
]
date_dialog.open()
Example().run()
```

###### **MDModalDatePicker** 

Modal date pickers navigate across dates in several ways: 

- To navigate across months, swipe horizontally (not implemented in KivyMD) 

- To navigate across years, scroll vertically (not implemented in KivyMD) 

- To access the year picker, tap the year 

Don’t use a modal date picker to prompt for dates in the distant past or future, such as a date of birth. In these cases, use a modal input picker or a docked datepicker instead. 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDModalDatePicker
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_date_picker()
MDButtonText:
text:"Openmodaldatepickerdialog"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defshow_date_picker(self):
```

(continues on next page) 

**Chapter 2. Contents** 

**326** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
date_dialog=MDModalDatePicker()
date_dialog.open()
```

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDModalDatePicker
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmodaldatepickerdialog"
),
id="button",
pos_hint={'center_x':.5,'center_y':0.5},
on_release=self.show_date_picker,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defshow_date_picker(self,args):
date_dialog=MDModalDatePicker()
date_dialog.open()
Example().run()
```

###### **MDModalInputDatePicker** 

Modal date inputs allow the manual entry of dates using the numbers on a keyboard. Users can input a date or a range of dates in a dialog. 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDModalInputDatePicker
```

(continues on next page) 

**2.3. Components** 

**327** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_date_picker()
MDButtonText:
text:"Openmodaldatepickerdialog"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defshow_date_picker(self):
date_dialog=MDModalInputDatePicker()
date_dialog.open()
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDModalInputDatePicker
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmodaldatepickerdialog"
),
id="button",
pos_hint={'center_x':.5,'center_y':0.5},
on_release=self.show_date_picker,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defshow_date_picker(self,args):
date_dialog=MDModalInputDatePicker()
```

(continues on next page) 

**Chapter 2. Contents** 

**328** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
date_dialog.open()
Example().run()
```

###### **The range of available dates** 

To display only the selected date range, use the _min_date_ and _max_date_ parameters: 

```
defshow_modal_date_picker(self,*args):
MDModalDatePicker(
mark_today=False,
min_date=datetime.date.today(),
max_date=datetime.date(
datetime.date.today().year,
datetime.date.today().month,
datetime.date.today().day+4,
),
).open()
```

Only dates in the specified range will be available for selection: 

###### **Select the date range** 

To select the date range, use the _mode_ parameter with the value “range”: 

```
defshow_modal_date_picker(self,*args):
MDModalDatePicker(mode="range").open()
```

###### **Setting the date range manually** 

```
defshow_modal_date_picker(self,*args):
MDModalInputDatePicker(mode="range").open()
```

###### **Events** 

###### **on_edit event** 

Declarative python style with KV 

**2.3. Components** 

**329** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDModalInputDatePicker,MDModalDatePicker
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_modal_date_picker()
MDButtonText:
text:"Openmodaldatepickerdialog"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defshow_modal_input_date_picker(self,*args):
defon_edit(*args):
date_dialog.dismiss()
Clock.schedule_once(self.show_modal_date_picker,0.2)
date_dialog=MDModalInputDatePicker()
date_dialog.bind(on_edit=on_edit)
date_dialog.open()
defon_edit(self,instance_date_picker):
instance_date_picker.dismiss()
Clock.schedule_once(self.show_modal_input_date_picker,0.2)
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker()
date_dialog.bind(on_edit=self.on_edit)
date_dialog.open()
```

```
Example().run()
```

Declarative python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDModalInputDatePicker,MDModalDatePicker
fromkivymd.uix.screenimportMDScreen
```

(continues on next page) 

**Chapter 2. Contents** 

**330** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmodaldatepickerdialog"
),
id="button",
pos_hint={'center_x':.5,'center_y':0.5},
on_release=self.show_modal_date_picker,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defshow_modal_input_date_picker(self,*args):
defon_edit(*args):
date_dialog.dismiss()
Clock.schedule_once(self.show_modal_date_picker,0.2)
date_dialog=MDModalInputDatePicker()
date_dialog.bind(on_edit=on_edit)
date_dialog.open()
defon_edit(self,instance_date_picker):
instance_date_picker.dismiss()
Clock.schedule_once(self.show_modal_input_date_picker,0.2)
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker()
date_dialog.bind(on_edit=self.on_edit)
date_dialog.open()
```

```
Example().run()
```

###### **on_select_day event** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDModalDatePicker
```

(continues on next page) 

**2.3. Components** 

**331** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarSupportingText
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_modal_date_picker()
MDButtonText:
text:"Openmodaldatepickerdialog"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defon_select_day(self,instance_date_picker,number_day):
instance_date_picker.dismiss()
MDSnackbar(
MDSnackbarSupportingText(
text=f"Theselecteddayis{number_day}",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
background_color="olive"
).open()
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker()
date_dialog.bind(on_select_day=self.on_select_day)
date_dialog.open()
```

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.material_resourcesimportdp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDModalDatePicker
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarSupportingText
classExample(MDApp):
```

(continues on next page) 

**Chapter 2. Contents** 

**332** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmodaldatepickerdialog"
),
id="button",
pos_hint={'center_x':.5,'center_y':0.5},
on_release=self.show_modal_date_picker,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_select_day(self,instance_date_picker,number_day):
instance_date_picker.dismiss()
MDSnackbar(
MDSnackbarSupportingText(
text=f"Theselecteddayis{number_day}",
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
background_color="olive"
).open()
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker()
date_dialog.bind(on_select_day=self.on_select_day)
date_dialog.open()
```

```
Example().run()
```

**on_select_month event** 

```
defon_select_month(self,instance_date_picker,number_month):
[...]
```

```
defshow_modal_date_picker(self,*args):
[...]
date_dialog.bind(on_select_month=self.on_select_month)
[...]
```

**2.3. Components** 

**333** 

**KivyMD, Release 2.0.1.dev0** 

###### **on_select_year event** 

```
defon_select_year(self,instance_date_picker,number_year):
[...]
```

```
defshow_modal_date_picker(self,*args):
[...]
date_dialog.bind(on_select_month=self.on_select_year)
[...]
```

###### **on_cancel event** 

```
defon_cancel(self,instance_date_picker):
[...]
defshow_modal_date_picker(self,*args):
[...]
date_dialog.bind(on_cancel=self.on_cancel)
[...]
```

###### **on_ok event** 

```
defon_ok(self,instance_date_picker):
print(instance_date_picker.get_date()[0])
```

```
defshow_modal_date_picker(self,*args):
[...]
date_dialog.bind(on_ok=self.on_ok)
[...]
```

###### **on_ok with range event** 

Declarative python style with KV 

```
importdatetime
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.pickersimportMDModalDatePicker
fromkivymd.uix.snackbarimport(
```

(continues on next page) 

**Chapter 2. Contents** 

**334** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDSnackbar,MDSnackbarSupportingText,MDSnackbarText
)
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_modal_date_picker()
MDButtonText:
text:"Openmodaldatepickerdialog"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defon_ok(self,instance_date_picker):
MDSnackbar(
MDSnackbarText(
text="Selecteddatesis:",
),
MDSnackbarSupportingText(
text="\n".join(str(date)fordateininstance_date_picker.get_date()),
padding=[0,0,0,dp(12)],
),
y=dp(124),
pos_hint={"center_x":0.5},
size_hint_x=0.5,
padding=[0,0,"8dp","8dp"],
).open()
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker(
mode="range",
min_date=datetime.date.today(),
max_date=datetime.date(
datetime.date.today().year,
datetime.date.today().month,
datetime.date.today().day+4,
),
)
date_dialog.bind(on_ok=self.on_ok)
date_dialog.open()
Example().run()
```

Declarative python style 

**2.3. Components** 

**335** 

**KivyMD, Release 2.0.1.dev0** 

```
importdatetime
fromkivymd.appimportMDApp
fromkivymd.material_resourcesimportdp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.pickersimportMDModalDatePicker
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.snackbarimport(
MDSnackbar,MDSnackbarSupportingText,MDSnackbarText
)
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDButton(
MDButtonText(
text="Openmodaldatepickerdialog"
),
id="button",
pos_hint={'center_x':.5,'center_y':0.5},
on_release=self.show_modal_date_picker,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_ok(self,instance_date_picker):
MDSnackbar(
MDSnackbarText(
text="Selecteddatesis:",
),
MDSnackbarSupportingText(
text="\n".join(
str(date)fordateininstance_date_picker.get_date()),
padding=[0,0,0,dp(12)],
),
y=dp(124),
pos_hint={"center_x":0.5},
size_hint_x=0.5,
padding=[0,0,"8dp","8dp"],
).open()
defshow_modal_date_picker(self,*args):
date_dialog=MDModalDatePicker(
mode="range",
min_date=datetime.date.today(),
max_date=datetime.date(
datetime.date.today().year,
datetime.date.today().month,
```

(continues on next page) 

**Chapter 2. Contents** 

**336** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
datetime.date.today().day+4,
),
)
date_dialog.bind(on_ok=self.on_ok)
date_dialog.open()
```

```
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

```
date_dialog=MDDatePicker()
date_dialog.open()
```

###### **2.0.0 version** 

```
#date_dialog=MDModalDatePicker()
#date_dialog=MDModalInputDatePicker()
date_dialog=MDDockedDatePicker()
date_dialog.open()
```

**API -** `kivymd.uix.pickers.datepicker.datepicker` 

`class kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker(` _year=None_ , _month=None_ , 

_day=None_ , _firstweekday=0_ , _**kwargs_ `)` 

Implements the base class of the date picker. 

Added in version 2.0.0. 

For more information, see in the _`ThemableBehavior`_ and _`MotionDatePickerBehavior`_ and `BoxLayout` and classes documentation. 

###### **Events** 

_`on_select_day`_ Fired when a day is selected. 

_`on_select_month`_ Fired when a month is selected. 

_`on_select_year`_ Fired when a year is selected. 

```
on_cancel
```

Fired when the ‘Cancel’ button is pressed. 

```
on_ok
```

Fired when the ‘Ok’ button is pressed. 

**2.3. Components** 

**337** 

**KivyMD, Release 2.0.1.dev0** 

```
on_edit
```

Fired when you click on the date editing icon. 

_`on_dismiss`_ Fired when a date picker closes. 

###### `day` 

The day of the month to be opened by default. If not specified, the current number will be used. 

_`day`_ is an `NumericProperty` and defaults to _0_ . 

###### `month` 

The number of month to be opened by default. If not specified, the current number will be used. _`month`_ is an `NumericProperty` and defaults to _0_ . 

###### `year` 

The year of month to be opened by default. If not specified, the current number will be used. 

_`year`_ is an `NumericProperty` and defaults to _0_ . 

###### `min_year` 

The year of month to be opened by default. If not specified, the current number will be used. 

_`min_year`_ is an `NumericProperty` and defaults to _1914_ . 

###### `max_year` 

The year of month to be opened by default. If not specified, the current number will be used. 

_`max_year`_ is an `NumericProperty` and defaults to _2121_ . 

###### `mode` 

Dialog type. Available options are: _‘picker’_ , _‘range’_ . 

_`mode`_ is an `OptionProperty` and defaults to _picker_ . 

###### `min_date` 

The minimum value of the date range for the _‘mode_ ’ parameter. Must be an object <class ‘datetime.date’>. 

_`min_date`_ is an `ObjectProperty` and defaults to _None_ . 

###### `max_date` 

The minimum value of the date range for the _‘mode_ ’ parameter. Must be an object <class ‘datetime.date’>. 

_`max_date`_ is an `ObjectProperty` and defaults to _None_ . 

###### `radius` 

Container radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(16), dp(16), dp(16), dp(16)]_ . 

###### `scrim_color` 

Color for scrim in (r, g, b, a) or string format. 

_`scrim_color`_ is a `ColorProperty` and defaults to _[0, 0, 0, 0.5]_ . 

###### `supporting_text` 

Supporting text. 

_`supporting_text`_ is a `StringProperty` and defaults to _‘Select date’_ . 

**Chapter 2. Contents** 

**338** 

**KivyMD, Release 2.0.1.dev0** 

###### `text_button_ok` 

The text of the confirmation button. 

_`text_button_ok`_ is a `StringProperty` and defaults to _‘Ok’_ . 

###### `text_button_cancel` 

The text of the cancel button. 

_`text_button_cancel`_ is a `StringProperty` and defaults to _‘Cancel’_ . 

###### `mark_today` 

Highlights the current day. 

_`mark_today`_ is a `BooleanProperty` and defaults to _True_ . 

###### `is_open` 

Is the date picker dialog open. 

_`is_open`_ is a `BooleanProperty` and defaults to _False_ . 

```
sel_year
```

```
sel_month
```

```
sel_day
```

###### `calendar_layout` 

`get_date(` _*args_ `)` _→_ list 

Returns a list of dates in the format [datetime.date(yyyy, mm, dd), ...]. The list has two dates if you use a date interval. 

`set_text_full_date()` _→_ str 

Returns a string like “Tue, Feb 2”. 

`compare_date_range()` _→_ None 

###### `change_month(` _operation: str_ `)` _→_ None 

Called when “chevron-left” and “chevron-right” buttons are pressed. Switches the calendar to the previous/next month. 

`generate_list_widgets_days()` _→_ None 

`update_calendar(` _year_ , _month_ `)` _→_ None 

`set_selected_widget(` _widget_ `)` _→_ None 

`restore_calendar_layout_properties()` _→_ None 

`set_calendar_layout_properties(` _method_ `)` _→_ None 

`dismiss(` _*args_ `)` _→_ None 

Dismiss the dialog date picker. 

`open()` _→_ None 

Show the dialog date picker. 

**2.3. Components** 

**339** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

- `on_select_day(` _*args_ `)` _→_ None 

Fired when a day is selected. 

- `on_select_month(` _*args_ `)` _→_ None 

Fired when a month is selected. 

- `on_select_year(` _*args_ `)` _→_ None 

Fired when a year is selected. 

`on_cancel(` _*args_ `)` _→_ None 

Fired when the ‘Cancel’ button is pressed. 

`on_ok(` _*args_ `)` _→_ None 

Fired when the ‘Ok’ button is pressed. 

- `on_edit(` _*args_ `)` _→_ None 

Fired when you click on the date editing icon. 

`on_dismiss(` _*args_ `)` _→_ None 

Fired when a date picker closes. 

`class kivymd.uix.pickers.datepicker.datepicker.MDDockedDatePicker(` _**kwargs_ `)` 

Implements docked date picker. 

Added in version 2.0.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseDatePicker`_ classes documentation. 

###### `generate_menu_month_year_selection(` _menu_type: str = 'month'_ `)` _→_ None 

Generates a list for the month or year selection menu. 

`open_close_menu_month_year_selection(` _state: bool = True_ , _menu_type: str = 'month'_ `)` _→_ None 

Hides the calendar layout and opens the list to select the month or year. 

`class kivymd.uix.pickers.datepicker.datepicker.MDModalDatePicker(` _**kwargs_ `)` 

Implements modal date picker. 

Added in version 2.0.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseDatePicker`_ classes documentation. 

`open()` _→_ None 

Show the dialog date picker. 

`generate_list_widgets_years()` _→_ None 

**Chapter 2. Contents** 

**340** 

**KivyMD, Release 2.0.1.dev0** 

`open_menu_year_selection(` _*args_ `)` _→_ None 

- `class kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker(` _*args_ , _**kwargs_ `)` 

Implements modal input date picker. 

Added in version 2.0.0. 

For more information, see in the _`CommonElevationBehavior`_ and _`MDBaseDatePicker`_ classes documentation. 

###### `date_format` 

Format of date strings that will be entered. Available options are: _‘dd/mm/yyyy’_ , _‘mm/dd/yyyy’_ , _‘yyyy/mm/dd’_ . 

_`date_format`_ is an `OptionProperty` and defaults to _None_ . 

###### `default_input_date` 

If true, the current date will be set in the input field. 

_`default_input_date`_ is a `BooleanProperty` and defaults to _True_ . 

###### `error_text` 

Error text when the date entered by the user is not valid. 

_`error_text`_ is a `StringProperty` and defaults to _‘Invalid date format’_ . 

###### `supporting_input_text` 

Auxiliary text when entering the date manually. 

_`supporting_input_text`_ is a `StringProperty` and defaults to _‘Enter date’_ . 

###### `generate_list_widgets_days()` _→_ None 

`update_calendar(` _*args_ `)` _→_ None 

`set_input_date(` _input_date: str_ `)` _→_ None 

###### `get_date(` _*args_ `)` _→_ list 

Returns a list of dates in the format [datetime.date(yyyy, mm, dd), ...]. The list has two dates if you use a date interval. 

###### `get_current_date_from_format()` _→_ str 

Returns the date according to the set format in _`date_format`_ . 

###### `open()` _→_ None 

Show the dialog date picker. 

###### **2.3.36 Chip** 

###### **See also:** 

Material Design 3 spec, Chips 

**2.3. Components** 

**341** 



<!-- Start of picture text -->
9:30 w4a<br>+ Amenities<br>Chips help people enter information, make BF Neighborhoods<br>selections, filter content, or trigger actions. V Eaglehead — ¥ Rabbit island {downtown<br>pitmas Y DykerHelghts | EastFlatbush | Gt<br><!-- End of picture text -->







<!-- Start of picture text -->
MDChip MDChipText MDChipTrailinglcon<br>MDChipLeadinglcon<br><!-- End of picture text -->







MDChip 



<!-- Start of picture text -->
(3 Assist | y Filter Suggestion<br><!-- End of picture text -->



<!-- Start of picture text -->
Se<br>Los Cantantes i<br>Oaxacan Restaurant<br>("| Add to my itinerary B® 12 mins from hotel<br>4.0 * *& & & xX 1,185 Reviews<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDChipLeadingIcon:
icon:root.icon
theme_text_color:"Custom"
text_color:"#68896c"
MDChipText:
text:root.text
theme_text_color:"Custom"
text_color:"#e6e9df"
MDScreen:
FitImage:
source:"bg.png"
MDBoxLayout:
orientation:"vertical"
adaptive_size:True
pos_hint:{"center_y":.6,"center_x":.5}
CommonLabel:
text:"in10mins"
bold:True
pos_hint:{"center_x":.5}
CommonLabel:
text:"TherapywithThea"
font_style:"Display"
role:"large"
padding_y:"12dp"
CommonLabel:
text:"Videocall"
font_style:"Display"
role:"small"
pos_hint:{"center_x":.5}
MDBoxLayout:
adaptive_size:True
pos_hint:{"center_x":.5}
spacing:"12dp"
padding:0,"24dp",0,0
CommonAssistChip:
text:"Homeoffice"
icon:"map-marker"
CommonAssistChip:
text:"Chat"
icon:"message"
```

(continues on next page) 

**Chapter 2. Contents** 

**346** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDWidget:
'''
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Teal"
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.propertiesimportStringProperty
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.chipimportMDChip,MDChipLeadingIcon,MDChipText
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.widgetimportMDWidget
classCommonAssistChip(MDChip):
text=StringProperty()
icon=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.type="assist"
self.theme_bg_color="Custom"
self.md_bg_color="#2a3127"
self.theme_line_color="Custom"
self.line_color="grey"
self.theme_elevation_level="Custom"
self.elevation_level=1
self.theme_shadow_softness="Custom"
self.shadow_softness=2
Clock.schedule_once(self._add_widget)
def_add_widget(self,*args):
self.add_widget(
MDChipLeadingIcon(
icon=self.icon,
theme_text_color="Custom",
text_color="#68896c",
)
```

(continues on next page) 

**2.3. Components** 

**347** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
)
self.add_widget(
MDChipText(
text=self.text,
theme_text_color="Custom",
text_color="#68896c",
)
)
classCommonLabel(MDLabel):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.adaptive_size=True
self.theme_text_color="Custom"
self.text_color="#e6e9df"
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Teal"
self.theme_cls.theme_style="Dark"
return(
MDScreen(
FitImage(
source="bg.png"
),
MDBoxLayout(
CommonLabel(
text="in10mins",
bold=True,
pos_hint={"center_x":0.5},
),
CommonLabel(
text="TherapywithThea",
font_style="Display",
role="large",
padding_y="12dp",
),
CommonLabel(
text="Videocall",
font_style="Display",
role="small",
pos_hint={"center_x":0.5},
),
MDBoxLayout(
CommonAssistChip(
text="Homeoffice",
icon="map-marker",
),
CommonAssistChip(
text="Chat",
```

(continues on next page) 

**Chapter 2. Contents** 

**348** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon="message",
),
adaptive_size=True,
pos_hint={"center_x":0.5},
spacing="12dp",
padding=(0,"24dp",0,0),
),
MDWidget(),
orientation="vertical",
adaptive_size=True,
pos_hint={"center_y":0.6,"center_x":0.5},
),
)
)
Example().run()
```



**2.3. Components** 

**349** 



<!-- Start of picture text -->
9:30 VA<br>+,+ Amenitieswy<br>Y Cats OK Dogs OK<br>LU Neighborhoods<br>Y Eaglehead Y Rabbit Island<br>er a<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
<CustomOneLineIconListItem>
MDListItemLeadingIcon:
icon:root.icon
MDListItemHeadlineText:
text:root.text
<PreviewIconsScreen>
MDBoxLayout:
orientation:"vertical"
spacing:"14dp"
padding:"20dp"
MDTextField:
id:search_field
mode:"outlined"
on_text:root.set_list_md_icons(self.text,True)
MDTextFieldLeadingIcon:
icon:"magnify"
MDTextFieldHintText:
text:"Searchicon"
MDBoxLayout:
id:chip_box
spacing:"12dp"
adaptive_height:True
RecycleView:
id:rv
viewclass:"CustomOneLineIconListItem"
key_size:"height"
RecycleBoxLayout:
padding:dp(10)
default_size:None,dp(48)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
orientation:"vertical"
'''
)
classCustomOneLineIconListItem(MDListItem):
icon=StringProperty()
text=StringProperty()
```

(continues on next page) 

**2.3. Components** 

**351** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classPreviewIconsScreen(MDScreen):
filter=ListProperty()#listoftagsforfilteringicons
defset_filter_chips(self):
'''Asynchronouslycreatesandaddschipstothecontainer.'''
asyncdefset_filter_chips():
fortagin["Outline","Off","On"]:
awaitasynckivy.sleep(0)
chip=MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
)
chip.bind(active=lambdax,y,z=tag:self.set_filter(y,z))
self.ids.chip_box.add_widget(chip)
```

```
asynckivy.start(set_filter_chips())
defset_filter(self,active:bool,tag:str)->None:
'''Setsalistoftagsforfilteringicons.'''
ifactive:
self.filter.append(tag)
else:
self.filter.remove(tag)
defset_list_md_icons(self,text="",search=False)->None:
'''Buildsalistoficons.'''
defadd_icon_item(name_icon):
self.ids.rv.data.append(
{
"icon":name_icon,
"text":name_icon,
}
)
self.ids.rv.data=[]
forname_iconinmd_icons.keys():
fortaginself.filter:
iftag.lower()inname_icon:
ifsearch:
iftextinname_icon:
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
```

(continues on next page) 

**Chapter 2. Contents** 

**352** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=PreviewIconsScreen()
defbuild(self)->PreviewIconsScreen:
self.theme_cls.theme_style="Dark"
returnself.screen
defon_start(self)->None:
self.screen.set_list_md_icons()
self.screen.set_filter_chips()
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty,ListProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.chipimportMDChip,MDChipText
fromkivymd.uix.listimportMDListItem
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.textfieldimport(
MDTextField,MDTextFieldLeadingIcon,MDTextFieldHintText
)
importasynckivy
Builder.load_string(
'''
<CustomOneLineIconListItem>
MDListItemLeadingIcon:
icon:root.icon
MDListItemHeadlineText:
text:root.text
'''
)
classCustomOneLineIconListItem(MDListItem):
```

(continues on next page) 

**2.3. Components** 

**353** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon=StringProperty()
text=StringProperty()
```

```
classPreviewIconsScreen(MDScreen):
filter=ListProperty()#listoftagsforfilteringicons
defset_filter_chips(self):
'''Asynchronouslycreatesandaddschipstothecontainer.'''
asyncdefset_filter_chips():
fortagin["Outline","Off","On"]:
awaitasynckivy.sleep(0)
chip=MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
)
chip.bind(active=lambdax,y,z=tag:self.set_filter(y,z))
self.get_ids().chip_box.add_widget(chip)
```

```
asynckivy.start(set_filter_chips())
```

```
defset_filter(self,active:bool,tag:str)->None:
'''Setsalistoftagsforfilteringicons.'''
ifactive:
self.filter.append(tag)
else:
self.filter.remove(tag)
defset_list_md_icons(self,text="",search=False)->None:
'''Buildsalistoficons.'''
defadd_icon_item(name_icon):
self.get_ids().rv.data.append(
{
"icon":name_icon,
"text":name_icon,
}
)
self.get_ids().rv.data=[]
forname_iconinmd_icons.keys():
fortaginself.filter:
iftag.lower()inname_icon:
ifsearch:
iftextinname_icon:
```

(continues on next page) 

**Chapter 2. Contents** 

**354** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
classExample(MDApp):
defbuild(self)->PreviewIconsScreen:
self.theme_cls.theme_style="Dark"
self.screen=PreviewIconsScreen(
MDBoxLayout(
MDTextField(
MDTextFieldLeadingIcon(
icon="magnify"
),
MDTextFieldHintText(
text="Searchicon"
),
id="search_field",
mode="outlined",
),
MDBoxLayout(
id="chip_box",
spacing="12dp",
adaptive_height=True,
),
MDRecycleView(
MDRecycleBoxLayout(
padding=dp(10),
default_size=(None,dp(48)),
default_size_hint=(1,None),
adaptive_height=True,
orientation="vertical",
),
id="rv",
),
orientation="vertical",
spacing="14dp",
padding="20dp",
)
)
search_field=self.screen.get_ids().search_field
search_field.bind(
text=lambda*x:self.screen.set_list_md_icons(search_field.text,True)
)
self.screen.get_ids().rv.key_size="height"
self.screen.get_ids().rv.viewclass="CustomOneLineIconListItem"
returnself.screen
defon_start(self)->None:
self.screen.set_list_md_icons()
self.screen.set_filter_chips()
```

(continues on next page) 

**2.3. Components** 

**355** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Tap a chip to select it. Multiple chips can be selected or unselected: 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.chipimportMDChip,MDChipText
fromkivymd.uix.screenimportMDScreen
importasynckivy
Builder.load_string(
'''
<ChipScreen>
MDBoxLayout:
orientation:"vertical"
spacing:"14dp"
padding:"20dp"
MDLabel:
adaptive_height:True
text:"SelectType"
MDStackLayout:
id:chip_box
spacing:"12dp"
adaptive_height:True
MDWidget:
MDButton:
pos:"20dp","20dp"
on_release:root.unchecks_chips()
MDButtonText:
text:"Uncheckchips"
'''
)
classChipScreen(MDScreen):
asyncdefcreate_chips(self):
'''Asynchronouslycreatesandaddschipstothecontainer.'''
fortagin["ExtraSoft","Soft","Medium","Hard"]:
awaitasynckivy.sleep(0)
```

(continues on next page) 

**Chapter 2. Contents** 

**356** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.ids.chip_box.add_widget(
MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
active=True,
)
)
defunchecks_chips(self)->None:
'''Removesmarksfromallchips.'''
forchipinself.ids.chip_box.children:
ifchip.active:
chip.active=False
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=ChipScreen()
defbuild(self)->ChipScreen:
self.theme_cls.theme_style="Dark"
returnself.screen
defon_start(self)->None:
asynckivy.start(self.screen.create_chips())
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.chipimportMDChip,MDChipText
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.stacklayoutimportMDStackLayout
fromkivymd.uix.widgetimportMDWidget
importasynckivy
classChipScreen(MDScreen):
asyncdefcreate_chips(self):
```

(continues on next page) 

**2.3. Components** 

**357** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
'''Asynchronouslycreatesandaddschipstothecontainer.'''
fortagin["ExtraSoft","Soft","Medium","Hard"]:
awaitasynckivy.sleep(0)
self.get_ids().chip_box.add_widget(
MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
active=True,
)
)
defunchecks_chips(self)->None:
'''Removesmarksfromallchips.'''
forchipinself.get_ids().chip_box.children:
ifchip.active:
chip.active=False
classExample(MDApp):
defbuild(self)->ChipScreen:
self.theme_cls.theme_style="Dark"
self.screen=ChipScreen(
MDBoxLayout(
MDLabel(
adaptive_height=True,
text="SelectType",
),
MDStackLayout(
id="chip_box",
spacing="12dp",
adaptive_height=True,
),
MDWidget(),
orientation="vertical",
spacing="14dp",
padding="20dp",
),
MDButton(
MDButtonText(
text="Uncheckchips"
),
id="button",
pos=("20dp","20dp"),
)
)
```

(continues on next page) 

**Chapter 2. Contents** 

**358** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.screen.get_ids().button.bind(
on_release=lambdax:self.screen.unchecks_chips()
)
returnself.screen
defon_start(self)->None:
asynckivy.start(self.screen.create_chips())
Example().run()
```

Alternatively, a single chip can be selected. This offers an alternative to toggle buttons, radio buttons, or single select menus: 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.chipimportMDChip,MDChipText
fromkivymd.uix.screenimportMDScreen
importasynckivy
Builder.load_string(
'''
<ChipScreen>
MDBoxLayout:
orientation:"vertical"
spacing:"14dp"
padding:"20dp"
MDLabel:
adaptive_height:True
text:"SelectType"
MDStackLayout:
id:chip_box
spacing:"12dp"
adaptive_height:True
MDWidget:
'''
)
classChipScreen(MDScreen):
asyncdefcreate_chips(self):
'''Asynchronouslycreatesandaddschipstothecontainer.'''
```

(continues on next page) 

**2.3. Components** 

**359** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fortagin["ExtraSoft","Soft","Medium","Hard"]:
awaitasynckivy.sleep(0)
chip=MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
)
chip.bind(active=self.uncheck_chip)
self.ids.chip_box.add_widget(chip)
defuncheck_chip(self,current_chip:MDChip,active:bool)->None:
'''Removesamarkfromanalreadymarkedchip.'''
ifactive:
forchipinself.ids.chip_box.children:
ifcurrent_chipisnotchip:
ifchip.active:
chip.active=False
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=ChipScreen()
defbuild(self)->ChipScreen:
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Lightgreen"
returnself.screen
defon_start(self)->None:
asynckivy.start(self.screen.create_chips())
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.chipimportMDChip,MDChipText
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.stacklayoutimportMDStackLayout
fromkivymd.uix.widgetimportMDWidget
importasynckivy
```

(continues on next page) 

**Chapter 2. Contents** 

**360** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classChipScreen(MDScreen):
asyncdefcreate_chips(self):
'''Asynchronouslycreatesandaddschipstothecontainer.'''
fortagin["ExtraSoft","Soft","Medium","Hard"]:
awaitasynckivy.sleep(0)
chip=MDChip(
MDChipText(
text=tag,
),
type="filter",
selected_color="green",
theme_bg_color="Custom",
md_bg_color="#303A29",
)
chip.bind(active=self.uncheck_chip)
self.get_ids().chip_box.add_widget(chip)
defuncheck_chip(self,current_chip:MDChip,active:bool)->None:
'''Removesamarkfromanalreadymarkedchip.'''
ifactive:
forchipinself.get_ids().chip_box.children:
ifcurrent_chipisnotchip:
ifchip.active:
chip.active=False
classExample(MDApp):
defbuild(self)->ChipScreen:
self.theme_cls.theme_style="Dark"
self.screen=ChipScreen(
MDBoxLayout(
MDLabel(
adaptive_height=True,
text="SelectType",
),
MDStackLayout(
id="chip_box",
spacing="12dp",
adaptive_height=True,
),
MDWidget(),
orientation="vertical",
spacing="14dp",
padding="20dp",
),
)
returnself.screen
```

(continues on next page) 

**2.3. Components** 

**361** 





<!-- Start of picture text -->
9:30 045<br>€ Edit event 0 & x<br>Z. Patient meet & greet<br>:<br>© Weds, November 3 v 10:30 AM v<br>© Sav Caffaa 12 Grattan Ctraat<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
pos_hint:{"center_x":.5,"center_y":.5}
type:"input"
theme_line_color:"Custom"
line_color:"grey"
ripple_effect:False
MDChipLeadingAvatar:
source:"data/logo/kivy-icon-128.png"
MDChipText:
text:"MDChip"
MDChipTrailingIcon:
icon:"close"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.chipimport(
MDChipLeadingAvatar,MDChipText,MDChipTrailingIcon,MDChip
)
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDChip(
MDChipLeadingAvatar(
source="data/logo/kivy-icon-128.png"
),
MDChipText(
text="MDChip"
),
MDChipTrailingIcon(
icon="close"
),
pos_hint={"center_x":0.5,"center_y":0.5},
type="input",
theme_line_color="Custom",
```

(continues on next page) 

**2.3. Components** 

**363** 



twy MDChip x 



<!-- Start of picture text -->
— - — “e.<br>Fashion Platform heels Colorful socks<br>(0. Le) a oN<br>Lens Library Crop Cut<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example of suggestion** 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
MDChip:
pos_hint:{"center_x":.5,"center_y":.5}
type:"suggestion"
theme_line_color:"Custom"
line_color:"grey"
MDChipText:
text:"MDChip"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.chipimportMDChipText,MDChip
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDChip(
MDChipText(
text="MDChip"
),
pos_hint={"center_x":0.5,"center_y":0.5},
type="suggestion",
theme_line_color="Custom",
line_color="grey",
),
md_bg_color=self.theme_cls.backgroundColor,
)
```

(continues on next page) 

**2.3. Components** 

**365** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
)
```

```
Example().run()
```



**API break** 

###### **1.2.0 version** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
MDChip:
text:"Portland"
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.on_release_chip(self)
'''
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_release_chip(self,instance_check):
print(instance_check)
Test().run()
```

**Chapter 2. Contents** 

**366** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
MDChip:
pos_hint:{"center_x":.5,"center_y":.5}
theme_line_color:"Custom"
line_color:"grey"
on_release:app.on_release_chip(self)
MDChipText:
text:"MDChip"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_release_chip(self,instance_check):
print(instance_check)
Example().run()
```

**API -** `kivymd.uix.chip.chip` 

`class kivymd.uix.chip.chip.MDChipLeadingAvatar(` _**kwargs_ `)` 

Implements the leading avatar for the chip. 

For more information, see in the _`CircularRippleBehavior`_ and _`ScaleBehavior`_ and `ButtonBehavior` and _`MDIcon`_ classes documentation. 

- `class kivymd.uix.chip.chip.MDChipLeadingIcon(` _**kwargs_ `)` 

Implements the leading icon for the chip. 

For more information, see in the _`CircularRippleBehavior`_ and _`ScaleBehavior`_ and `ButtonBehavior` and _`MDIcon`_ classes documentation. 

`class kivymd.uix.chip.chip.MDChipTrailingIcon(` _**kwargs_ `)` 

Implements the trailing icon for the chip. 

For more information, see in the _`CircularRippleBehavior`_ and _`ScaleBehavior`_ and `ButtonBehavior` and _`MDIcon`_ classes documentation. 

- `class kivymd.uix.chip.chip.MDChipText(` _*args_ , _**kwargs_ `)` 

Implements the label for the chip. 

For more information, see in the _`MDLabel`_ classes documentation. 

**2.3. Components** 

**367** 

**KivyMD, Release 2.0.1.dev0** 

###### `text_color_disabled` 

The text color in (r, g, b, a) or string format of the chip when the chip is disabled. 

Added in version 2.0.0. 

_`text_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

`class kivymd.uix.chip.chip.MDChip(` _*args_ , _**kwargs_ `)` 

Chip class. 

For more information, see in the _`MDBoxLayout`_ and _`RectangularRippleBehavior`_ and `ButtonBehavior` and _`CommonElevationBehavior`_ and _`TouchBehavior`_ classes documentation. 

###### `radius` 

Chip radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(8), dp(8), dp(8), dp(8)]_ . 

```
type
```

Type of chip. 

Added in version 2.0.0. 

Available options are: _‘assist’_ , _‘filter’_ , _‘input’_ , _‘suggestion’_ . 

_`type`_ is an `OptionProperty` and defaults to _‘suggestion’_ . 

###### `active` 

Whether the check is marked or not. 

Added in version 1.0.0. 

_`active`_ is an `BooleanProperty` and defaults to _False_ . 

###### `selected_color` 

The background color of the chip in the marked state in (r, g, b, a) or string format. 

Added in version 2.0.0. 

_`selected_color`_ is an `ColorProperty` and defaults to _None_ . 

```
line_color_disabled
```

The color of the outline in the disabled state 

Added in version 2.0.0. 

_`line_color_disabled`_ is an `ColorProperty` and defaults to _None_ . 

`on_long_touch(` _*args_ `)` _→_ None 

Fired when the widget is pressed for a long time. 

- `on_line_color(` _instance_ , _value_ `)` _→_ None 

Fired when the values of `line_color` change. 

- `on_type(` _instance_ , _value: str_ `)` _→_ None 

Fired when the values of _`type`_ change. 

- `on_active(` _instance_check_ , _active_value: bool_ `)` _→_ None 

Called when the values of _`active`_ change. 

`complete_anim_ripple(` _*args_ `)` _→_ None 

Called at the end of the ripple animation. 

**Chapter 2. Contents** 

**368** 

**KivyMD, Release 2.0.1.dev0** 

###### `remove_marked_icon_from_chip()` _→_ None 

###### `add_marked_icon_to_chip()` _→_ None 

Adds and animates a check icon to the chip. 

- `set_chip_bg_color(` _color: list | str_ `)` _→_ None 

Animates the background color of the chip. 

- `on_press(` _*args_ `)` _→_ None 

Fired when the button is pressed. 

- `on_release(` _*args_ `)` _→_ None 

Fired when the button is released (i.e. the touch/click that pressed the button goes away). 

###### `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### **2.3.37 ProgressIndicator** 

###### **See also:** 

Material Design spec, ProgressIndicator 

**2.3. Components** 

**369** 



<!-- Start of picture text -->
— O<br> ) 2)<br><!-- End of picture text -->







<!-- Start of picture text -->
a<br><!-- End of picture text -->

#### <u>a</u> 



~~oe~~ 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.progressindicatorimportMDCircularProgressIndicator
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDCircularProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
pos_hint={'center_x':.5,'center_y':.5},
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

Linear progress indicators can be determinate or indeterminate. 

###### **Determinate linear progress indicator** 

Determinate operations display the indicator increasing from 0 to 100% of the track, in sync with the process’s progress. 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLinearProgressIndicator:
id:progress
```

(continues on next page) 

**Chapter 2. Contents** 

**372** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
size_hint_x:.5
type:"determinate"
pos_hint:{'center_x':.5,'center_y':.4}
'''
classExample(MDApp):
defon_start(self):
self.root.ids.progress.start()
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.progressindicatorimportMDLinearProgressIndicator
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defon_start(self):
self.root.get_ids().progress.start()
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDLinearProgressIndicator(
id="progress",
type="determinate",
size_hint_x=.5,
value=50,
pos_hint={'center_x':.5,'center_y':.5},
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

Circular progress indicators can be determinate or indeterminate. 

**2.3. Components** 

**373** 

**KivyMD, Release 2.0.1.dev0** 

###### **Indeterminate circular progress indicator** 

Indeterminate operations display the indicator continually growing and shrinking along the track until the process is complete.. 

Declarative KV style 

```
MDCircularProgressIndicator:
size_hint:None,None
size:"48dp","48dp"
```

Declarative Python style 

```
MDCircularProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
)
```

###### **Determinate circular progress indicator** 

Declarative KV style 

```
MDCircularProgressIndicator:
size_hint:None,None
size:"48dp","48dp"
determinate:True
on_determinate_complete:print(args)
```

Declarative Python style 

```
MDCircularProgressIndicator(
determinate=True,
size_hint=(None,None),
size=("48dp","48dp"),
on_determinate_complete=lambda*args:print(args),
)
```

###### **API break** 

###### **1.1.1 version** 

```
MDProgressBar:
value:50
color:app.theme_cls.accent_color
```

```
MDSpinner:
size_hint:None,None
size:dp(48),dp(48)
```

**Chapter 2. Contents** 

**374** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

Declarative KV style 

```
MDLinearProgressIndicator:
value:50
indicator_color:app.theme_cls.errorColor
```

Declarative Python style 

```
MDLinearProgressIndicator(
value=50,
indicator_color=self.theme_cls.errorColor,
)
```

Declarative KV style 

```
MDCircularProgressIndicator:
size_hint:None,None
size:dp(48),dp(48)
```

Declarative Python style 

```
MDCircularProgressIndicator(
size_hint=(None,None),
size=("48dp","48dp"),
)
```

###### **API -** `kivymd.uix.progressindicator.progressindicator` 

`class kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator(` _**kwargs_ `)` 

Implementation of the linear progress indicator. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and `ProgressBar` classes documentation. 

###### `radius` 

Progress line radius. 

Added in version 1.2.0. 

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `reversed` 

Reverse the direction the progressbar moves. 

_`reversed`_ is an `BooleanProperty` and defaults to _False_ . 

###### `orientation` 

Orientation of progressbar. Available options are: _‘horizontal ‘_ , _‘vertical’_ . 

_`orientation`_ is an `OptionProperty` and defaults to _‘horizontal’_ . 

###### `indicator_color` 

Color of the active track. 

Changed in version 2.0.0: Rename from _color_ to _indicator_color_ attribute. 

**2.3. Components** 

**375** 

**KivyMD, Release 2.0.1.dev0** 

_`indicator_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `track_color` 

Progress bar back color in (r, g, b, a) or string format. 

Added in version 1.0.0. 

Changed in version 2.0.0: Rename from _back_color_ to _track_color_ attribute. 

_`track_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `running_determinate_transition` 

Running transition. 

Changed in version 2.0.0: Rename from _running_transition_ to _running_determinate_transition_ attribute. 

_`running_determinate_transition`_ is an `StringProperty` and defaults to _‘out_quart’_ . 

###### `catching_determinate_transition` 

Catching transition. 

Changed in version 2.0.0: Rename from _catching_transition_ to _catching_determinate_transition_ attribute. 

_`catching_determinate_transition`_ is an `StringProperty` and defaults to _‘out_quart’_ . 

###### `running_determinate_duration` 

Running duration. 

Changed in version 2.0.0: Rename from _running_duration_ to _running_determinate_duration_ attribute. 

_`running_determinate_duration`_ is an `NumericProperty` and defaults to _2.5_ . 

###### `catching_determinate_duration` 

Catching duration. 

`running_duration` is an `NumericProperty` and defaults to _0.8_ . 

###### `type` 

Type of progressbar. Available options are: _‘indeterminate ‘_ , _‘determinate’_ . 

_`type`_ is an `OptionProperty` and defaults to _None_ . 

###### `running_indeterminate_transition` 

Running transition. 

_`running_indeterminate_transition`_ is an `StringProperty` and defaults to _‘in_cubic’_ . 

###### `catching_indeterminate_transition` 

Catching transition. 

_`catching_indeterminate_transition`_ is an `StringProperty` and defaults to _‘out_quart’_ . 

###### `running_indeterminate_duration` 

Running duration. 

_`running_indeterminate_duration`_ is an `NumericProperty` and defaults to _0.5_ . 

###### `catching_indeterminate_duration` 

Catching duration. 

_`catching_indeterminate_duration`_ is an `NumericProperty` and defaults to _0.8_ . 

`check_size(` _*args_ `)` _→_ None 

**Chapter 2. Contents** 

**376** 

**KivyMD, Release 2.0.1.dev0** 

###### `start()` _→_ None 

Start animation. 

`stop()` _→_ None 

Stop animation. 

`running_away(` _*args_ `)` _→_ None 

`catching_up(` _*args_ `)` _→_ None 

`on_value(` _instance_ , _value_ `)` 

`class kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator(` _**kwargs_ `)` Implementation of the circular progress indicator. 

Changed in version 2.0.0: Rename _MDSpinner_ to _MDCircularProgressIndicator_ class. 

For more information, see in the _`ThemableBehavior`_ and `Widget` classes documentation. 

It can be used either as an indeterminate indicator that loops while the user waits for something to happen, or as a determinate indicator. 

Set _`determinate`_ to **True** to activate determinate mode, and _`determinate_time`_ to set the duration of the animation. 

###### **Events** 

###### **_on_determinate_complete_** 

The event is called at the end of the indicator loop in the _determinate = True_ mode. 

###### `determinate` 

Determinate value. 

_`determinate`_ is a `BooleanProperty` and defaults to _False_ . 

###### `determinate_time` 

Determinate time value. 

_`determinate_time`_ is a `NumericProperty` and defaults to _2_ . 

###### `line_width` 

Progress line width of indicator. 

_`line_width`_ is a `NumericProperty` and defaults to _dp(2.25)_ . 

###### `active` 

Use _`active`_ to start or stop the indicator. 

_`active`_ is a `BooleanProperty` and defaults to _True_ . 

###### `color` 

Indicator color in (r, g, b, a) or string format. 

_`color`_ is a `ColorProperty` and defaults to _None_ . 

###### `palette` 

A set of colors. Changes with each completed indicator cycle. 

_`palette`_ is a `ListProperty` and defaults to _[]_ . 

`on__rotation_angle(` _*args_ `)` 

**2.3. Components** 

**377** 



<!-- Start of picture text -->
VA<br>Revert<br>Menus<br>Menus display a list of choices on a temporary surface : 4 Help !<br>wr<br>ic<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`MDButton: id: button pos_hint: {"center_x": .5, "center_y": .5} on_release: app.menu_open() MDButtonText: text: "Press me" ''' class Example(MDApp): def menu_open(self): menu_items = [ { "text": f"Item {i}", "on_release": lambda x=f"Item {i}": self.menu_callback(x), } for i in range(5) ] MDDropdownMenu( caller=self.root.ids.button, items=menu_items ).open() def menu_callback(self, text_item): print(text_item) def build(self): self.theme_cls.primary_palette = "Orange" self.theme_cls.theme_style = "Dark" return Builder.load_string(KV) Example().run()` Declarative Python style `from kivymd.app import MDApp from kivymd.uix.button import MDButton, MDButtonText from kivymd.uix.menu import MDDropdownMenu from kivymd.uix.screen import MDScreen class Example(MDApp): def menu_open(self, button_press_me): menu_items = [ { "text": f"Item {i}", "on_release": lambda x=f"Item {i}": self.menu_callback(x), } for i in range(5) ] MDDropdownMenu(caller=button_press_me, items=menu_items).open()` 

(continues on next page) 

**2.3. Components** 

**379** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDButton(
MDButtonText(
text="Pressme"
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.menu_open,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

###### **Anatomy** 



###### **You can combine the following parameters:** 

- leading_icon 

- text 

- trailing_icon 

- trailing_text 

...to create the necessary types of menu items: 

```
menu_items=[
{
"text":"Strikethrough",
"leading_icon":"check",
"trailing_icon":"apple-keyboard-command",
"trailing_text":"+Shift+X",
}
]
```

**Chapter 2. Contents** 

**380** 





<!-- Start of picture text -->
OB<br><!-- End of picture text -->





<!-- Start of picture text -->
Be<br><!-- End of picture text -->





<!-- Start of picture text -->
OB<br><!-- End of picture text -->





<!-- Start of picture text -->
SO<br><!-- End of picture text -->

## ~~es a~~ Oo OO 



### <u>a</u> 





**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDIconButton:
icon:"gesture-tap-button"
pos_hint:{"center_y":.5}
MDLabel:
text:"Actions"
adaptive_size:True
pos_hint:{"center_y":.5}
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
id:button
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.menu.open()
MDButtonText:
text:"Pressme"
'''
classMenuHeader(MDBoxLayout):
'''Aninstanceoftheclassthatwillbeaddedtothemenuheader.'''
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=Builder.load_string(KV)
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(
header_cls=MenuHeader(),
caller=self.screen.ids.button,
items=menu_items,
)
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
returnself.screen
```

(continues on next page) 

**Chapter 2. Contents** 

**384** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButtonText,MDButton,MDIconButton
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.screenimportMDScreen
```

```
classMenuHeader(MDBoxLayout):
'''Aninstanceoftheclassthatwillbeaddedtothemenuheader.'''
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(
header_cls=MenuHeader(
MDIconButton(
icon="gesture-tap-button",
pos_hint={"center_y":.5},
),
MDLabel(
text="Actions",
adaptive_size=True,
pos_hint={"center_y":.5},
),
spacing="12dp",
padding="4dp",
adaptive_height=True,
),
items=menu_items,
)
self.screen=(
MDScreen(
MDButton(
MDButtonText(
text="Pressme"
),
id="button_press_me",
pos_hint={"center_x":.5,"center_y":.5},
on_release=lambdax:self.menu.open(),
```

(continues on next page) 

**2.3. Components** 

**385** 



=o C@ Actions Item 0 Item 1 

Item 2 



<!-- Start of picture text -->
Item 3<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDBoxLayout:
orientation:"vertical"
md_bg_color:self.theme_cls.backgroundColor
MDTopAppBar:
MDTopAppBarLeadingButtonContainer:
MDActionTopAppBarButton:
icon:"menu"
on_release:app.callback(self)
MDTopAppBarTitle:
text:"MDTopAppBar"
pos_hint:{"center_x":.5}
MDTopAppBarTrailingButtonContainer:
MDActionTopAppBarButton:
icon:"dots-vertical"
on_release:app.callback(self)
MDLabel:
text:"Content"
halign:"center"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(items=menu_items)
returnBuilder.load_string(KV)
defcallback(self,button):
self.menu.caller=button
self.menu.open()
defmenu_callback(self,text_item):
self.menu.dismiss()
MDSnackbar(
MDSnackbarText(
text=text_item,
),
y=dp(24),
```

(continues on next page) 

**2.3. Components** 

**387** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
```

```
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.appbarimport(
MDTopAppBar,
MDTopAppBarLeadingButtonContainer,
MDActionTopAppBarButton,
MDTopAppBarTitle,
MDTopAppBarTrailingButtonContainer,
)
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarText
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(items=menu_items)
return(
MDBoxLayout(
MDTopAppBar(
MDTopAppBarLeadingButtonContainer(
MDActionTopAppBarButton(
icon="menu",
on_release=self.callback,
)
),
MDTopAppBarTitle(
text="MDTopAppBar",
pos_hint={"center_x":.5},
),
MDTopAppBarTrailingButtonContainer(
MDActionTopAppBarButton(
icon="dots-vertical",
```

(continues on next page) 

**Chapter 2. Contents** 

**388** 



Item 0 Item 1 Item 2 Item 3 Item 4 

**KivyMD, Release 2.0.1.dev0** 

###### **Position** 

###### **Bottom position** 

###### **See also:** 

_`position`_ Declarative Python style with KV `from kivy.lang import Builder from kivy.metrics import dp from kivymd.app import MDApp from kivymd.uix.menu import MDDropdownMenu KV = ''' MDScreen: md_bg_color: self.theme_cls.backgroundColor MDTextField: id: field pos_hint: {'center_x': .5, 'center_y': .6} size_hint_x: None width: "200dp" on_focus: if self.focus: app.menu.open() MDTextFieldHintText: text: "Password" ''' class Example(MDApp): def __init__(self, **kwargs): super().__init__(**kwargs) self.screen = Builder.load_string(KV) menu_items = [ { "text": f"Item {i}", "on_release": lambda x=f"Item {i}": self.set_item(x), } for i in range(5)] self.menu = MDDropdownMenu( caller=self.screen.ids.field, items=menu_items, position="bottom", ) def set_item(self, text_item): self.screen.ids.field.text = text_item self.menu.dismiss() def build(self): self.theme_cls.primary_palette = "Orange" self.theme_cls.theme_style = "Dark"` 

(continues on next page) 

**Chapter 2. Contents** 

**390** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
returnself.screen
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.textfieldimportMDTextField,MDTextFieldHintText
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.set_item(x),
}
foriinrange(5)
]
self.menu=MDDropdownMenu(items=menu_items,position="bottom")
self.screen=MDScreen(
MDTextField(
MDTextFieldHintText(text="Password"),
id="field",
pos_hint={"center_x":0.5,"center_y":0.6},
size_hint_x=None,
width="200dp",
),
md_bg_color=self.theme_cls.backgroundColor,
)
field=self.screen.get_ids().field
self.menu.caller=field
field.bind(
focus=lambdainstance,value:self.menu.open()ifvalueelseNone
)
defset_item(self,text_item):
self.screen.get_ids().field.text=text_item
self.menu.dismiss()
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
returnself.screen
Example().run()
```

**2.3. Components** 

**391** 

Item 0 Item 1 

Item 2 Item 3 

Item 4 



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
]
ifnotself.drop_item_menu:
self.drop_item_menu=MDDropdownMenu(
caller=item,items=menu_items,position="center"
)
self.drop_item_menu.open()
defmenu_callback(self,text_item):
self.root.ids.drop_text.text=text_item
self.drop_item_menu.dismiss()
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.uix.dropdownitemimportMDDropDownItemText,MDDropDownItem
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
drop_item_menu:MDDropdownMenu=None
defopen_drop_item_menu(self,item):
menu_items=[
{
"text":f"{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
ifnotself.drop_item_menu:
self.drop_item_menu=MDDropdownMenu(
caller=item,items=menu_items,position="center"
)
self.drop_item_menu.open()
defmenu_callback(self,text_item):
self.root.get_ids().drop_text.text=text_item
self.drop_item_menu.dismiss()
defbuild(self):
return(
MDScreen(
MDDropDownItem(
MDDropDownItemText(
id="drop_text",
text="Item",
```

(continues on next page) 

**2.3. Components** 

**393** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.open_drop_item_menu,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

###### **API break** 

###### **1.1.1 version** 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.listimportIRightBodyTouch,OneLineAvatarIconListItem
fromkivymd.uix.menuimportMDDropdownMenu
KV='''
<RightContentCls>
disabled:True
adaptive_size:True
pos_hint:{"center_y":.5}
MDIconButton:
icon:root.icon
icon_size:"16sp"
md_bg_color_disabled:0,0,0,0
MDLabel:
text:root.text
font_style:"Caption"
adaptive_size:True
pos_hint:{"center_y":.5}
<Item>
IconLeftWidget:
icon:root.left_icon
RightContentCls:
id:container
```

(continues on next page) 

**Chapter 2. Contents** 

**394** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon:root.right_icon
text:root.right_text
MDScreen:
MDRaisedButton:
id:button
text:"PRESSME"
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.menu.open()
'''
classRightContentCls(IRightBodyTouch,MDBoxLayout):
icon=StringProperty()
text=StringProperty()
classItem(OneLineAvatarIconListItem):
left_icon=StringProperty()
right_icon=StringProperty()
right_text=StringProperty()
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=Builder.load_string(KV)
menu_items=[
{
"text":f"Item{i}",
"right_text":"+Shift+X",
"right_icon":"apple-keyboard-command",
"left_icon":"web",
"viewclass":"Item",
"height":dp(54),
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(
caller=self.screen.ids.button,
items=menu_items,
bg_color="#bdc6b0",
width_mult=4,
)
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
returnself.screen
```

(continues on next page) 

**2.3. Components** 

**395** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

###### **1.2.0 version** 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.menuimportMDDropdownMenu
KV='''
MDScreen:
MDRaisedButton:
id:button
text:"PRESSME"
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.menu.open()
'''
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.screen=Builder.load_string(KV)
menu_items=[
{
"text":f"Item{i}",
"leading_icon":"web",
"trailing_icon":"apple-keyboard-command",
"trailing_text":"+Shift+X",
"trailing_icon_color":"grey",
"trailing_text_color":"grey",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
self.menu=MDDropdownMenu(
md_bg_color="#bdc6b0",
caller=self.screen.ids.button,
items=menu_items,
)
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
returnself.screen
```

(continues on next page) 

**Chapter 2. Contents** 

**396** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

###### **2.0.0 version** 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.menuimportMDDropdownMenu
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
id:button
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.menu_open()
MDButtonText:
text:"Pressme"
'''
classExample(MDApp):
defmenu_open(self):
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
MDDropdownMenu(
caller=self.root.ids.button,items=menu_items
).open()
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

**2.3. Components** 

**397** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defmenu_open(self,button_press_me):
menu_items=[
{
"text":f"Item{i}",
"on_release":lambdax=f"Item{i}":self.menu_callback(x),
}foriinrange(5)
]
MDDropdownMenu(caller=button_press_me,items=menu_items).open()
defmenu_callback(self,text_item):
print(text_item)
defbuild(self):
self.theme_cls.primary_palette="Orange"
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDButton(
MDButtonText(
text="Pressme"
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.menu_open,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

**API -** `kivymd.uix.menu.menu` 

`class kivymd.uix.menu.menu.BaseDropdownItem(` _**kwargs_ `)` 

Base class for menu items. 

Added in version 1.2.0. 

For more information, see in the _`RectangularRippleBehavior`_ and _`MDBoxLayout`_ classes. 

```
text
```

The text of the menu item. 

_`text`_ is a `StringProperty` and defaults to _‘’_ . 

```
leading_icon
```

The leading icon of the menu item. 

**Chapter 2. Contents** 

**398** 

**KivyMD, Release 2.0.1.dev0** 

_`leading_icon`_ is a `StringProperty` and defaults to _‘’_ . 

###### `trailing_icon` 

The trailing icon of the menu item. 

_`trailing_icon`_ is a `StringProperty` and defaults to _‘’_ . 

###### `trailing_text` 

The trailing text of the menu item. 

_`trailing_text`_ is a `StringProperty` and defaults to _‘’_ . 

###### `text_color` 

The color of the text in (r, g, b, a) or string format for the text of the menu item. 

_`text_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `leading_icon_color` 

The color of the text in (r, g, b, a) or string format for the leading icon of the menu item. 

_`leading_icon_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `trailing_icon_color` 

The color of the text in (r, g, b, a) or string format for the trailing icon of the menu item. 

_`leading_icon_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `trailing_text_color` 

The color of the text in (r, g, b, a) or string format for the trailing text of the menu item. 

_`leading_icon_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `divider` 

Divider mode. Available options are: _‘Full’_ , _None_ and default to _‘Full’_ . 

_`divider`_ is a `OptionProperty` and defaults to _‘Full’_ . 

###### `divider_color` 

Divider color in (r, g, b, a) or string format. 

_`divider_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `class kivymd.uix.menu.menu.MDDropdownTextItem(` _**kwargs_ `)` 

Implements a menu item with text without leading and trailing icons. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

- `class kivymd.uix.menu.menu.MDDropdownLeadingIconItem(` _**kwargs_ `)` 

Implements a menu item with text, leading icon and without trailing icon. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

###### `class kivymd.uix.menu.menu.MDDropdownTrailingIconItem(` _**kwargs_ `)` 

Implements a menu item with text, without leading icon and with trailing icon. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

**2.3. Components** 

**399** 

**KivyMD, Release 2.0.1.dev0** 

###### `class kivymd.uix.menu.menu.MDDropdownTrailingIconTextItem(` _**kwargs_ `)` 

Implements a menu item with text, without leading icon, with trailing icon and with trailing text. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

- `class kivymd.uix.menu.menu.MDDropdownTrailingTextItem(` _**kwargs_ `)` 

Implements a menu item with text, without leading icon, without trailing icon and with trailing text. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

- `class kivymd.uix.menu.menu.MDDropdownLeadingIconTrailingTextItem(` _**kwargs_ `)` 

Implements a menu item with text, leading icon and with trailing text. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

- `class kivymd.uix.menu.menu.MDDropdownLeadingTrailingIconTextItem(` _**kwargs_ `)` 

Implements a menu item with text, with leading icon, with trailing icon and with trailing text. 

Added in version 1.2.0. 

For more information, see in the _`BaseDropdownItem`_ class. 

- `class kivymd.uix.menu.menu.MDDropdownMenu(` _**kwargs_ `)` 

Dropdown menu class. 

For more information, see in the _`MotionDropDownMenuBehavior`_ and _`StencilBehavior`_ and _`MDCard`_ classes documentation. 

###### **Events** 

###### **_on_release_** 

The method that will be called when you click menu items. 

###### `header_cls` 

An instance of the class ( _Kivy_ or _KivyMD_ widget) that will be added to the menu header. 

Added in version 0.104.2. 

See _Header_ for more information. 

_`header_cls`_ is a `ObjectProperty` and defaults to _None_ . 

###### `items` 

List of dictionaries with properties for menu items. 

_`items`_ is a `ListProperty` and defaults to _[]_ . 

###### `width_mult` 

This number multiplied by the standard increment (‘56dp’ on mobile, ‘64dp’ on desktop), determines the width of the menu items. 

If the resulting number were to be too big for the application Window, the multiplier will be adjusted for the biggest possible one. 

Deprecated since version 1.2.0: Use _width_ instead. 

**Chapter 2. Contents** 

**400** 





ltem 04 Item 0 Item 1 Item 2 Item 3 Item 4 Item 5 





<!-- Start of picture text -->
Item 0<br>Item 1<br>Item 2<br>Item 3<br>Item 4<br>Item b=<br><!-- End of picture text -->





<!-- Start of picture text -->
Item? 4<br>Item 0<br>item 1<br>Item 2<br>Item 3<br>Item 4<br><!-- End of picture text -->



liam 

Item 0 

Item 1 

Item 2 

Item 3 

Item 4 





<!-- Start of picture text -->
Item? 4<br>Item 0<br>item 1<br>Item 2<br>Item 3<br>Item 4<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `position` 

Menu window position relative to parent element. Available options are: _‘auto’_ , _‘top’_ , _‘center’_ , _‘bottom’_ . 

See _Position_ for more information. 

_`position`_ is a `OptionProperty` and defaults to _‘auto’_ . 

###### `radius` 

Menu radius. 

_`radius`_ is a `VariableListProperty` and defaults to _‘[dp(7)]’_ . 

###### `adjust_width()` _→_ None 

Adjust the width of the menu if the width of the menu goes beyond the boundaries of the parent window from starting point. 

###### `check_ver_growth()` _→_ None 

Checks whether the height of the lower/upper borders of the menu exceeds the limits borders of the parent window. 

- `check_hor_growth()` _→_ None 

Checks whether the width of the left/right menu borders exceeds the boundaries of the parent window. 

`get_target_pos()` _→_ [float, float] 

- `set_target_height()` _→_ None 

Set the target height of the menu depending on the size of each item. 

- `set_menu_properties(` _*args_ `)` _→_ None 

Sets the size and position for the menu window. 

`set_menu_pos(` _*args_ `)` _→_ None 

###### `adjust_position()` _→_ str 

Return value ‘auto’ for the menu position if the menu position is out of screen. 

`open()` _→_ None 

Animate the opening of a menu window. 

- `on_items(` _instance_ , _value: list_ `)` _→_ None 

The method sets the class that will be used to create the menu item. 

`on_header_cls(` _instance_dropdown_menu_ , _instance_user_menu_header_ `)` _→_ None 

Called when a value is set to the _`header_cls`_ parameter. 

###### `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

**Chapter 2. Contents** 

**404** 



<!-- Start of picture text -->
C VAe<br>= Recipes Q H<br>Lists =<br>Lists are continuous, vertical indexes of text and images Te<br><!-- End of picture text -->









<!-- Start of picture text -->
MDListltemLeadinglcon MDListitemTrailingCheckbox<br>| Headline ———————> _ MDListltemHeadlineText |<br>@  supportngtet —————> MDListitemSupportingText<br>Tertiary tect —————>  MDListltemTertiaryText<br>MDListitem<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example:** 

###### **One line list item** 

Declarative KV styles 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDListItem:
pos_hint:{"center_x":.5,"center_y":.5}
size_hint_x:.8
MDListItemHeadlineText:
text:"Headline"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python styles 

```
fromkivymd.uix.listimportMDListItem,MDListItemHeadlineText
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
classExample(MDApp):
defbuild(self):
return(
MDScreen(
MDListItem(
MDListItemHeadlineText(
text="Headline",
),
pos_hint={"center_x":.5,"center_y":.5},
size_hint_x=0.8,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
```

(continues on next page) 

**2.3. Components** 

**407** 





Headline Supporting text 







Headline Supporting text Tertiary text 







3 Headline Supporting text Tertiary text 







2 Headline Supporting text Tertiary text 



<!-- Start of picture text -->
Wi<br><!-- End of picture text -->







2 Headline Supporting text Tertiary text 



<!-- Start of picture text -->
OC<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

`class kivymd.uix.list.list.BaseListItemText(` _*args_ , _**kwargs_ `)` 

Base class for text labels of a list item. 

For more information, see in the _`MDLabel`_ class documentation. 

- `class kivymd.uix.list.list.BaseListItemIcon(` _*args_ , _**kwargs_ `)` 

Base class for leading/trailing icon of list item. 

For more information, see in the _`MDIcon`_ class documentation. 

###### `icon_color` 

Icon color in (r, g, b, a) or string format. 

_`icon_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `icon_color_disabled` 

The icon color in (r, g, b, a) or string format of the list item when the list item is disabled. 

_`icon_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

- `class kivymd.uix.list.list.MDListItemHeadlineText(` _*args_ , _**kwargs_ `)` 

Implements a class for headline text of list item. 

For more information, see in the _`BaseListItemText`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemSupportingText(` _*args_ , _**kwargs_ `)` 

Implements a class for secondary text of list item. 

For more information, see in the _`BaseListItemText`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemTertiaryText(` _*args_ , _**kwargs_ `)` 

Implements a class for tertiary text of list item. 

For more information, see in the _`BaseListItemText`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemTrailingSupportingText(` _*args_ , _**kwargs_ `)` 

Implements a class for trailing text of list item. 

For more information, see in the _`BaseListItemText`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemLeadingIcon(` _*args_ , _**kwargs_ `)` 

Implements a class for leading icon class. 

For more information, see in the _`BaseListItemIcon`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemLeadingAvatar(` _**kwargs_ `)` 

Implements a class for leading avatar class. 

For more information, see in the _`ThemableBehavior`_ and _`CircularRippleBehavior`_ and `ButtonBehavior` and _`FitImage`_ classes documentation. 

- `class kivymd.uix.list.list.MDListItemTrailingIcon(` _*args_ , _**kwargs_ `)` 

Implements a class for trailing icon class. 

For more information, see in the _`BaseListItemIcon`_ class documentation. 

- `class kivymd.uix.list.list.MDListItemTrailingCheckbox(` _**kwargs_ `)` 

Implements a class for trailing checkbox class. 

For more information, see in the _`MDCheckbox`_ class documentation. 

**2.3. Components** 

**413** 

**KivyMD, Release 2.0.1.dev0** 

###### `class kivymd.uix.list.list.MDListItem(` _*args_ , _**kwargs_ `)` 

Implements a list item. 

For more information, see in the _`BaseListItem`_ and `BoxLayout` classes documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### **2.3.40 SegmentedButton** 

Added in version 1.2.0. 

###### **See also:** 

Material Design spec, Segmented buttons 

Segmented control 

**Chapter 2. Contents** 

**414** 



<!-- Start of picture text -->
30 v4i<br>eg Mm eC nted Your downloads<br>le ( I ttoNn S Balom> 21st Century Strangers ©<br>Segmentedviews, or sortbuttons helpelements.  people select options, switch BY Ta ©<br>FE%= ) nore ®<br>* Mutter fo)<br><!-- End of picture text -->



<!-- Start of picture text -->
ye E Week Month)<br><!-- End of picture text -->



<!-- Start of picture text -->
MDSegmentedButtonlitem<br>MDSegmentButtonicon MDSegmentButtonLabel<br>MDSegmentedButton<br><!-- End of picture text -->





**KivyMD, Release 2.0.1.dev0** 

Declarative python style 

```
MDSegmentedButton(
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-python"
),
MDSegmentButtonLabel(
text="Python"
),
),
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-javascript"
),
MDSegmentButtonLabel(
text="Java-Script"
),
),
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-swift"
),
MDSegmentButtonLabel(
text="Swift"
)
)
)
```

###### **Use without text with an icon** 

Declarative KV style 

```
MDSegmentedButton:
MDSegmentedButtonItem:
MDSegmentButtonIcon:
icon:"language-python"
MDSegmentedButtonItem:
MDSegmentButtonIcon:
icon:"language-javascript"
MDSegmentedButtonItem:
MDSegmentButtonIcon:
icon:"language-swift"
```

Declarative python style 

**2.3. Components** 

**417** 

**KivyMD, Release 2.0.1.dev0** 

```
MDSegmentedButton(
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-python"
),
),
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-javascript"
),
),
MDSegmentedButtonItem(
MDSegmentButtonIcon(
icon="language-swift"
),
)
)
```

###### **Use only text** 

Declarative KV style 

```
MDSegmentedButton:
MDSegmentedButtonItem:
MDSegmentButtonLabel:
text:"Python"
MDSegmentedButtonItem:
MDSegmentButtonLabel:
text:"Java-Script"
MDSegmentedButtonItem:
MDSegmentButtonLabel:
text:"Swift"
```

Declarative python style 

```
MDSegmentedButton(
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Python"
),
),
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Java-Script"
```

(continues on next page) 

**Chapter 2. Contents** 

**418** 







<!-- Start of picture text -->
Type ‘large’<br>Type ‘normal<br>Type 'mediun’<br>a ee ee<br>Type ‘small<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.segmentedbuttonimport(
MDSegmentedButton,
MDSegmentedButtonItem,
MDSegmentButtonLabel,
)
fromkivymd.appimportMDApp
classMyBox(MDBoxLayout):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
widgets=[]
forsegment_typein["large","normal","medium","small"]:
widgets.append(
MDBoxLayout(
MDLabel(
text=f"Type'{segment_type}'",
adaptive_height=True,
bold=True,
pos_hint={"center_y":0.5},
halign="center",
),
MDSegmentedButton(
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Songs",
),
),
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Albums",
),
),
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Podcasts",
),
),
type=segment_type,
),
orientation="vertical",
spacing="12dp",
adaptive_height=True,
)
)
self.widgets=widgets
```

```
classExample(MDApp):
defbuild(self):
return(
```

(continues on next page) 

**Chapter 2. Contents** 

**420** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDScreen(
MyBox(
orientation="vertical",
size_hint_x=.7,
adaptive_height=True,
spacing="24dp",
pos_hint={"center_x":.5,"center_y":.5},
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

###### **A practical example** 

Declarative Python style with KV 

```
importos
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
importasynckivy
fromfakerimportFaker
KV='''
<UserCard>
adaptive_height:True
radius:dp(16)
MDListItem:
radius:dp(16)
theme_bg_color:"Custom"
md_bg_color:self.theme_cls.secondaryContainerColor
MDListItemLeadingAvatar:
source:root.album
MDListItemHeadlineText:
text:root.name
MDListItemSupportingText:
text:root.path_to_file
```

(continues on next page) 

**2.3. Components** 

**421** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
orientation:"vertical"
padding:"12dp"
spacing:"12dp"
MDLabel:
adaptive_height:True
text:"Yourdownloads"
font_style:"Display"
role:"small"
MDSegmentedButton:
size_hint_x:1
MDSegmentedButtonItem:
active:True
on_active:app.generate_card()
MDSegmentButtonLabel:
text:"Songs"
MDSegmentedButtonItem:
on_active:app.generate_card()
MDSegmentButtonLabel:
text:"Albums"
MDSegmentedButtonItem:
on_active:app.generate_card()
MDSegmentButtonLabel:
text:"Podcasts"
RecycleView:
id:card_list
viewclass:"UserCard"
bar_width:0
RecycleBoxLayout:
orientation:'vertical'
spacing:"16dp"
padding:"16dp"
default_size:None,dp(72)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
'''
```

(continues on next page) 

**Chapter 2. Contents** 

**422** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classUserCard(MDBoxLayout):
name=StringProperty()
path_to_file=StringProperty()
album=StringProperty()
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defgenerate_card(self):
asyncdefgenerate_card():
foriinrange(10):
awaitasynckivy.sleep(0)
self.root.ids.card_list.data.append(
{
"name":fake.name(),
"path_to_file":f"{os.path.splitext(fake.file_path())[0]}.mp3",
"album":fake.image_url(),
}
)
fake=Faker()
self.root.ids.card_list.data=[]
Clock.schedule_once(lambdax:asynckivy.start(generate_card()))
```

```
Example().run()
```

Declarative python style 

```
importos
fromkivy.clockimportClock
fromkivy.propertiesimportStringProperty
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.listimport(
MDListItem,
MDListItemLeadingAvatar,
MDListItemHeadlineText,
MDListItemSupportingText,
)
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.segmentedbuttonimport(
```

(continues on next page) 

**2.3. Components** 

**423** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDSegmentedButton,MDSegmentedButtonItem,MDSegmentButtonLabel
)
importasynckivy
fromfakerimportFaker
classUserCard(MDBoxLayout):
name=StringProperty()
path_to_file=StringProperty()
album=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.adaptive_height=True
self.radius=dp(16)
Clock.schedule_once(self.post_init)
defpost_init(self,*args):
self.widgets=[
MDListItem(
MDListItemLeadingAvatar(
source=self.album
),
MDListItemHeadlineText(
text=self.name
),
MDListItemSupportingText(
text=self.path_to_file
),
)
]
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"
return(
MDScreen(
MDBoxLayout(
MDLabel(
adaptive_height=True,
text="Yourdownloads",
font_style="Display",
role="small",
),
MDSegmentedButton(
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Songs"
),
```

(continues on next page) 

**Chapter 2. Contents** 

**424** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
id="first_segment",
on_active=Clock.schedule_once(
lambdax:self.generate_card()
),
on_release=Clock.schedule_once(
lambdax:self.generate_card()
)
),
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Albums"
),
on_release=Clock.schedule_once(
lambdax:self.generate_card()
)
),
MDSegmentedButtonItem(
MDSegmentButtonLabel(
text="Podcasts"
),
on_release=Clock.schedule_once(
lambdax:self.generate_card()
)
),
size_hint_x=1
),
MDRecycleView(
MDRecycleBoxLayout(
orientation='vertical',
spacing="16dp",
padding="16dp",
default_size=(None,dp(72)),
default_size_hint=(1,None),
adaptive_height=True,
),
id="card_list",
bar_width=0,
),
orientation="vertical",
padding="12dp",
spacing="12dp",
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_start(self):
self.root.get_ids().card_list.viewclass="UserCard"
self.root.get_ids().first_segment.dispatch("on_release")
defgenerate_card(self):
asyncdefgenerate_card():
```

(continues on next page) 

**2.3. Components** 

**425** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
foriinrange(10):
awaitasynckivy.sleep(0)
self.root.get_ids().card_list.data.append(
{
"name":fake.name(),
"path_to_file":f"{os.path.splitext(fake.file_path())[0]}.mp3",
"album":fake.image_url(),
}
)
fake=Faker()
self.root.get_ids().card_list.data=[]
Clock.schedule_once(lambdax:asynckivy.start(generate_card()))
```

```
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

```
MDSegmentedButton:
on_marked:func(*args)
MDSegmentedButtonItem:
icon:...
text:...
```

###### **2.0.0 version** 

Declarative KV style 

```
MDSegmentedButton:
MDSegmentedButtonItem:
on_active:func(*args)
MDSegmentButtonIcon:
icon:...
MDSegmentButtonLabel:
text:...
```

Declarative python style 

```
MDSegmentedButton(
MDSegmentedButtonItem(
```

(continues on next page) 

**Chapter 2. Contents** 

**426** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDSegmentButtonIcon(
...
),
MDSegmentButtonLabel(
...
),
),
on_active=lambdax:func(*args)
)
```

###### **API -** `kivymd.uix.segmentedbutton.segmentedbutton` 

`class kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItem(` _*args_ , _**kwargs_ `)` Segment button item. 

For more information see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and _`RectangularRippleBehavior`_ and `ButtonBehavior` and _`StateLayerBehavior`_ and `RelativeLayout` and class documentation. 

###### `selected_color` 

Color of the marked segment. 

Added in version 2.0.0. 

_`selected_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the list item when the list item is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

###### `active` 

Background color of an disabled segment. 

_`active`_ is an `BooleanProperty` and defaults to _False_ . 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**2.3. Components** 

**427** 

**KivyMD, Release 2.0.1.dev0** 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

- `on_line_color(` _instance_ , _value_ `)` _→_ None 

Fired when the values of `line_color` change. 

- `on_active(` _instance_ , _value_ `)` _→_ None 

Fired when the _`active`_ value changes. Animates the marker icon for the element. 

- `on_disabled(` _instance_ , _value_ `)` _→_ None 

Fired when the `disabled` value changes. 

###### `class kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton(` _*args_ , _**kwargs_ `)` 

Segment button panel. 

For more information, see in the _`MDBoxLayout`_ class documentation. 

###### `multiselect` 

Do I allow multiple segment selection. 

_`multiselect`_ is an `BooleanProperty` and defaults to _False_ . 

###### `hiding_icon_transition` 

Name of the transition hiding the current icon. 

_`hiding_icon_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `hiding_icon_duration` 

Duration of hiding the current icon. 

_`hiding_icon_duration`_ is a `NumericProperty` and defaults to _1_ . 

###### `opening_icon_transition` 

The name of the transition that opens a new icon of the “marked” type. 

_`opening_icon_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `opening_icon_duration` 

The duration of opening a new icon of the “marked” type. 

_`opening_icon_duration`_ is a `NumericProperty` and defaults to _0.1_ . 

###### `selected_segments` 

The list of _`MDSegmentedButtonItem`_ objects that are currently marked. 

_`selected_segments`_ is a `ListProperty` and defaults to _[]_ . 

###### `type` 

Density can be used in denser UIs where space is limited. Density is only applied to the height. Each step down in density removes ‘4dp’ from the height. 

Added in version 2.0.0. 

Available options are: ‘large’, ‘normal’, ‘medium’, ‘small’. 

_`type`_ is an `OptionProperty` and defaults to _‘large’_ . 

**Chapter 2. Contents** 

**428** 

**KivyMD, Release 2.0.1.dev0** 

###### `selected_icon_color` 

Color in (r, g, b, a) or string format of the icon of the marked segment. 

Added in version 2.0.0. 

_`selected_icon_color`_ is a `ColorProperty` and defaults to _None_ . 

- `get_marked_items()` _→_ list 

Returns a list of active item objects. 

- `get_items()` _→_ list 

Returns a list of item objects. 

- `adjust_segment_radius(` _*args_ `)` _→_ None 

Rounds off the first and last elements. 

- `mark_item(` _segment_item:_ MDSegmentedButtonItem `)` _→_ None 

Fired when a segment element is clicked ( _on_release_ event). 

###### `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`remove_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Remove a widget from the children of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to remove from our children list. 

```
>>>fromkivy.uix.buttonimportButton
>>>root=Widget()
>>>button=Button()
```

(continues on next page) 

**2.3. Components** 

**429** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
>>>root.add_widget(button)
>>>root.remove_widget(button)
```

- `class kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentButtonIcon(` _*args_ , _**kwargs_ `)` 

   - Implements a icon for _`MDSegmentedButtonItem`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDIcon`_ class documentation. 

- `class kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentButtonLabel(` _*args_ , _**kwargs_ `)` 

Implements a label for _`MDSegmentedButtonItem`_ class. 

Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ class documentation. 

###### **2.3.41 Transition** 

###### **A set of classes for implementing transitions between application screens.** 

Added in version 1.0.0. 

###### **Changing transitions** 

You have multiple transitions available by default, such as: 

- _`MDFadeSlideTransition`_ 

state one: the new screen closes the previous screen by lifting from the bottom of the screen and changing from transparent to non-transparent; 

state two: the current screen goes down to the bottom of the screen, passing from a non-transparent state to a transparent one, thus opening the previous screen; 

###### **Note:** You cannot control the direction of a slide using the direction attribute. 

###### **API -** `kivymd.uix.transition.transition` 

- `class kivymd.uix.transition.transition.MDTransitionBase` 

TransitionBase is used to animate 2 screens within the _`MDScreenManager`_ . 

For more information, see in the `TransitionBase` class documentation. 

`start(` _instance_screen_manager:_ kivymd.uix.screenmanager.MDScreenManager `)` _→_ None 

- (internal) Starts the transition. This is automatically called by the `ScreenManager` . 

###### `animated_hero_in()` _→_ None 

Animates the flight of heroes from screen **A** to screen **B** . 

**Chapter 2. Contents** 

**430** 

**KivyMD, Release 2.0.1.dev0** 

###### `animated_hero_out()` _→_ None 

Animates the flight of heroes from screen **B** to screen **A** . 

###### `on_complete()` _→_ None 

Override method. See :attr: **`** kivy.uix.screenmanager.TransitionBase.on_complete’. 

###### `class kivymd.uix.transition.transition.MDSwapTransition(` _**kwargs_ `)` 

Swap transition that looks like iOS transition when a new window appears on the screen. 

###### `class kivymd.uix.transition.transition.MDSlideTransition` 

- Slide Transition, can be used to show a new screen from any direction: left, right, up or down. 

###### `class kivymd.uix.transition.transition.MDFadeSlideTransition` 

Slide Transition, can be used to show a new screen from any direction: left, right, up or down. 

- `start(` _instance_screen_manager:_ kivymd.uix.screenmanager.MDScreenManager `)` _→_ None 

   - (internal) Starts the transition. This is automatically called by the `ScreenManager` . 

###### `on_progress(` _progression: float_ `)` _→_ None 

###### `class kivymd.uix.transition.transition.MDSharedAxisTransition` 

Android default screen transition. 

Added in version 2.0.0. 

###### `transition_axis` 

Axis of the transition. Available values “x”, “y”, and “z”. 

_`transition_axis`_ is an `OptionProperty` and defaults to _“x”_ . 

###### `duration` 

Duration in seconds of the transition. Android recommends these intervals: 

Table 1: Android transition values (in seconds) 

|Name|value|
|---|---|
|small_1|0.075|
|small_2|0.15|
|medium_1|0.2|
|medium_2|0.25|
|large_1|0.3|
|large_2|0.35|



_`duration`_ is a `NumericProperty` and defaults to 0.2 (= 200ms). 

###### `switch_animation` 

Custom material design animation transition. 

_`switch_animation`_ is a `OptionProperty` and defaults to _“easing_emphasized”_ . 

###### `slide_distance` 

Distance to which it slides left, right, bottom or up depending on axis. 

_`slide_distance`_ is a `NumericProperty` and defaults to _dp(15)_ . 

**2.3. Components** 

**431** 



<!-- Start of picture text -->
sheets mmm one<br>Bottom sheets are surfaces containing Send<br>supplementarythe screen. content, anchored to the bottom of a‘ & t& e Qiad<br>Add to album View all<br><!-- End of picture text -->





<!-- Start of picture text -->
uri @ee Villanueva Saachi<br>ning Daniel Maa<br>CF Priority<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.bottomsheetimport(
MDBottomSheet,
MDBottomSheetDragHandle,
MDBottomSheetDragHandleTitle,
MDBottomSheetDragHandleButton,
```

```
)
```

```
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDBottomSheet(
MDBottomSheetDragHandle(
MDBottomSheetDragHandleTitle(
text="MDBottomSheet",
adaptive_height=True,
pos_hint={"center_y":0.5},
),
MDBottomSheetDragHandleButton(
icon="close",
),
),
size_hint_y=None,
height="84dp",
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
```

```
Example().run()
```

**Chapter 2. Contents** 

**434** 



<!-- Start of picture text -->
MDBottomSheet 4<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDLabel:
text:root.title
pos_hint:{"center_x":.5}
halign:"center"
adaptive_height:True
MDScreen:
MDNavigationLayout:
MDScreenManager:
MDScreen:
CustomMapView:
bottom_sheet:bottom_sheet
map_source:MapSource(url=app.map_sources[app.current_map])
lat:46.5124
lon:47.9812
zoom:12
MDBottomSheet:
id:bottom_sheet
sheet_type:"standard"
size_hint_y:None
height:"150dp"
on_open:asynckivy.start(app.generate_content())
MDBottomSheetDragHandle:
drag_handle_color:"grey"
MDBottomSheetDragHandleTitle:
text:"Selecttypemap"
pos_hint:{"center_y":.5}
MDBottomSheetDragHandleButton:
icon:"close"
ripple_effect:False
on_release:bottom_sheet.set_state("toggle")
BoxLayout:
id:content_container
padding:0,0,0,"16dp"
'''
classTypeMapElement(MDBoxLayout):
selected=BooleanProperty(False)
icon=StringProperty()
title=StringProperty()
```

(continues on next page) 

**Chapter 2. Contents** 

**436** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classCustomMapView(MapView,TouchBehavior):
bottom_sheet=ObjectProperty()
defon_double_tap(self,touch,*args):
ifself.bottom_sheet:
self.bottom_sheet.set_state("toggle")
classExample(MDApp):
map_sources={
"street":"https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
"sputnik":"https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
"hybrid":"https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
}
current_map=StringProperty("street")
asyncdefgenerate_content(self):
icons={
"street":"google-street-view",
"sputnik":"space-station",
"hybrid":"map-legend",
}
ifnotself.root.ids.content_container.children:
fori,titleinenumerate(self.map_sources.keys()):
awaitasynckivy.sleep(0)
self.root.ids.content_container.add_widget(
TypeMapElement(
title=title.capitalize(),
icon=icons[title],
selected=noti,
)
)
defset_active_element(self,instance,type_map):
forelementinself.root.ids.content_container.children:
ifinstance==element:
element.selected=True
self.current_map=type_map
else:
element.selected=False
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.propertiesimportStringProperty,ObjectProperty,BooleanProperty
```

(continues on next page) 

**2.3. Components** 

**437** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivy_garden.mapviewimportMapView
importasynckivy
fromkivy_garden.mapviewimportMapSource
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportTouchBehavior,DeclarativeBehavior
fromkivymd.uix.bottomsheetimport(
MDBottomSheet,
MDBottomSheetDragHandle,
MDBottomSheetDragHandleTitle,
MDBottomSheetDragHandleButton,
)
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.navigationdrawerimportMDNavigationLayout
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classTypeMapElement(MDBoxLayout):
selected=BooleanProperty(False)
icon=StringProperty()
title=StringProperty()
classCustomMapView(DeclarativeBehavior,MapView,TouchBehavior):
bottom_sheet=ObjectProperty()
defon_double_tap(self,touch,*args):
ifself.bottom_sheet:
self.bottom_sheet.set_state("toggle")
classExample(MDApp):
map_sources={
"street":"https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
"sputnik":"https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
"hybrid":"https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
}
current_map=StringProperty("street")
asyncdefgenerate_content(self):
icons={
"street":"google-street-view",
"sputnik":"space-station",
"hybrid":"map-legend",
}
ifnotself.screen.get_ids().content_container.children:
fori,titleinenumerate(self.map_sources.keys()):
awaitasynckivy.sleep(0)
```

(continues on next page) 

**Chapter 2. Contents** 

**438** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`type_map_element = TypeMapElement( MDIconButton( id=f"icon_{icons[title]}", icon=icons[title], theme_bg_color="Custom", md_bg_color="#EDF1F9", pos_hint={"center_x": 0.5}, theme_icon_color="Custom", icon_color="black" ), MDLabel( text=title, pos_hint={"center_x": 0.5}, halign="center", adaptive_height=True, ), orientation="vertical", adaptive_height=True, spacing="8dp", title=title.capitalize(), icon=icons[title], selected=not i, ) icon = type_map_element.get_ids()[f"icon_{icons[title]}"] icon.bind( on_release=lambda x=icon, z=type_map_element, y=title.lower(): self.` _˓→_ `set_active_element( x, z, y ) ) self.screen.get_ids().content_container.add_widget( type_map_element )` 

```
defset_active_element(self,button,instance,type_map):
forelementinself.screen.get_ids().content_container.children:
ifinstanceiselement:
element.selected=True
button.md_bg_color=self.theme_cls.primaryColor
button.icon_color="white"
self.current_map=type_map
self.screen.get_ids().custom_mapview.map_source=MapSource(
url=self.map_sources[self.current_map]
)
else:
forwidgetinelement.children:
ifisinstance(widget,MDIconButton)andnotwidgetisbutton:
element.selected=False
widget.md_bg_color="#EDF1F9"
widget.icon_color="black"
defbuild(self):
```

(continues on next page) 

**2.3. Components** 

**439** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.screen=MDScreen(
MDNavigationLayout(
MDScreenManager(
MDScreen(
CustomMapView(
id="custom_mapview",
map_source=MapSource(
url=self.map_sources[self.current_map]
),
lat=46.5124,
lon=47.9812,
zoom=12,
)
)
),
MDBottomSheet(
MDBottomSheetDragHandle(
MDBottomSheetDragHandleTitle(
text="Selecttypemap",
pos_hint={"center_y":0.5},
),
MDBottomSheetDragHandleButton(
id="handle_button",
icon="close",
ripple_effect=False,
),
drag_handle_color="grey",
),
MDBoxLayout(
id="content_container",
padding=(0,0,0,"16dp"),
),
id="bottom_sheet",
sheet_type="standard",
size_hint_y=None,
height="150dp",
on_open=lambdax:asynckivy.start(self.generate_content()),
),
)
)
bottom_sheet=self.screen.get_ids().bottom_sheet
self.screen.get_ids().custom_mapview.bottom_sheet=bottom_sheet
self.screen.get_ids().handle_button.bind(
on_release=lambdax:bottom_sheet.set_state("toggle")
)
returnself.screen
Example().run()
```

**Chapter 2. Contents** 

**440** 

**KivyMD, Release 2.0.1.dev0** 

###### **API break** 

###### **1.2.0 version** 

```
Root:
MDBottomSheet:
#Optional.
MDBottomSheetDragHandle:
#Optional.
MDBottomSheetDragHandleTitle:
#Optional.
MDBottomSheetDragHandleButton:
MDBottomSheetContent:
[...]
```

###### **2.0.0 version** 

```
Root:
MDNavigationLayout:
MDScreenManager:
#Yourscreen.
MDScreen:
MDBottomSheet:
#Optional.
MDBottomSheetDragHandle:
#Optional.
MDBottomSheetDragHandleTitle:
#Optional.
MDBottomSheetDragHandleButton:
icon:"close"
#Yourcontent.
BoxLayout:
```

**2.3. Components** 

**441** 





**KivyMD, Release 2.0.1.dev0** 

other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet(` _*args_ , _**kwargs_ `)` 

Bottom sheet class. 

For more information, see in the _`MDNavigationDrawer`_ class documentation. 

###### `sheet_type` 

Type of sheet. 

Standard bottom sheets co-exist with the screen’s main UI region and allow for simultaneously viewing and interacting with both regions, especially when the main UI region is frequently scrolled or panned. Use a standard bottom sheet to display content that complements the screen’s primary content, such as an audio player in a music app. 

Like dialogs, modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. 

Changed in version 2.0.0: Rename from _type_ to _sheet_type_ . 

_`sheet_type`_ is a `OptionProperty` and defaults to _‘modal’_ . 

- `on_sheet_type(` _instance_ , _value_ `)` _→_ None 

Fired when the _`sheet_type`_ value changes. 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

**_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**2.3. Components** 

**443** 

**KivyMD, Release 2.0.1.dev0** 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`on_touch_move(` _touch_ `)` 

Receive a touch move event. The touch is in parent coordinates. 

See `on_touch_down()` for more information. 

###### **2.3.43 Label** 

**Chapter 2. Contents** 

**444** 

t 

Display Display » Display Headline Headline @ Headline © 

Welcome to Welcome to the Welcome to the sho Welcome to the show Welcome to the show Welcome to the show 

Title 

**KivyMD, Release 2.0.1.dev0** 

###### **MDLabel** 

###### **Example** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLabel:
text:"MDLabel"
halign:"center"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.labelimportMDLabel
classTest(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDLabel(
text="MDLabel",
halign="center",
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Test().run()
```

**Chapter 2. Contents** 

**446** 

MDLabel 











###### Display, role - large 







**KivyMD, Release 2.0.1.dev0** 

###### **All styles** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.font_definitionsimporttheme_font_styles
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDRecycleView:
id:rv
key_viewclass:'viewclass'
key_size:'height'
RecycleBoxLayout:
padding:dp(10)
spacing:dp(10)
default_size:None,dp(48)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
orientation:"vertical"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_start(self):
forstyleintheme_font_styles:
ifstyle!="Icon":
forroleintheme_font_styles[style]:
font_size=int(theme_font_styles[style][role]["font-size"])
self.root.ids.rv.data.append(
{
"viewclass":"MDLabel",
"text":f"{style}{role}{font_size}sp",
"adaptive_height":"True",
"font_style":style,
"role":role,
}
)
Example().run()
```

Declarative python style 

**2.3. Components** 

**449** 

**KivyMD, Release 2.0.1.dev0** 

```
fromkivy.metricsimportdp
fromkivymd.font_definitionsimporttheme_font_styles
fromkivymd.appimportMDApp
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDRecycleView(
MDRecycleBoxLayout(
padding=dp(10),
spacing=dp(10),
default_size=(None,dp(48)),
default_size_hint=(1,None),
adaptive_height=True,
orientation="vertical",
),
id="rv",
),
md_bg_color=self.theme_cls.backgroundColor
)
)
defon_start(self):
self.root.get_ids().rv.key_viewclass='viewclass'
self.root.get_ids().rv.key_size='height'
forstyleintheme_font_styles:
ifstyle!="Icon":
forroleintheme_font_styles[style]:
font_size=int(
theme_font_styles[style][role]["font-size"])
self.root.get_ids().rv.data.append(
{
"viewclass":"MDLabel",
"text":f"{style}{role}{font_size}sp",
"adaptive_height":"True",
"font_style":style,
"role":role,
}
)
Example().run()
```

**Chapter 2. Contents** 

**450** 

Display large 57 sp Display medium 45 sp Display small 36 sp Headline large 32 sp 

Headline medium 28 sp Headline small 24 sp 

Title large 22 sp Title medium 16 sp Title small 14 sp Body large 16 sp Body medium 14 sp 

**KivyMD, Release 2.0.1.dev0** 

###### **Highlighting and copying labels** 

**You can highlight labels by double tap on the label:** 

Declarative KV style 

```
fromkivy.lang.builderimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDLabel:
adaptive_size:True
pos_hint:{"center_x":.5,"center_y":.5}
text:"Doadoubleclickonme"
allow_selection:True
padding:"4dp","4dp"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.clockimportClock
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defon_start(self):
defon_start(dt):
self.root.md_bg_color=self.theme_cls.backgroundColor
Clock.schedule_once(on_start)
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDLabel(
adaptive_size=True,
```

(continues on next page) 

**Chapter 2. Contents** 

**452** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
pos_hint={"center_x":0.5,"center_y":0.5},
text="Doadoubleclickonme",
allow_selection=True,
padding=("4dp","4dp"),
),
)
)
Example().run()
```

**You can copy the label text by double clicking on it:** 

Declarative KV style 

```
fromkivy.lang.builderimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
MDLabel:
adaptive_size:True
pos_hint:{"center_x":.5,"center_y":.5}
text:"MDLabel"
padding:"4dp","4dp"
allow_selection:True
allow_copy:True
on_copy:print("Thetextiscopiedtotheclipboard")
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.lang.builderimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
```

(continues on next page) 

**2.3. Components** 

**453** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
return(
MDScreen(
MDLabel(
id="label",
adaptive_size=True,
pos_hint={"center_x":.5,"center_y":.5},
text="MDLabel",
allow_selection=True,
allow_copy=True,
padding=("4dp","4dp"),
)
)
)
defon_start(self):
self.root.ids.label.bind(on_copy=self.on_copy)
defon_copy(self,instance_label:MDLabel):
print("Thetextiscopiedtotheclipboard")
Example().run()
```

###### **Example of copying/cutting labels using the context menu** 

Declarative KV style 

```
fromkivy.core.clipboardimportClipboard
fromkivy.lang.builderimportBuilder
fromkivy.metricsimportdp
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarText
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.menuimportMDDropdownMenu
KV='''
MDBoxLayout:
orientation:"vertical"
spacing:"12dp"
padding:"24dp"
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
id:box
```

(continues on next page) 

**Chapter 2. Contents** 

**454** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
orientation:"vertical"
padding:"24dp"
spacing:"12dp"
adaptive_height:True
MDTextField:
max_height:"200dp"
mode:"filled"
multiline:True
Widget:
'''
data=[
"Loremipsumdolorsitamet,consecteturadipiscingelit.",
"Sedblanditliberovolutpatsedcrasornarearcu.Nislvelpretium"
"lectusquamidleoin.Tinciduntarcunonsodalesnequesodalesutetiam.",
"Elitscelerisquemaurispellentesquepulvinarpellentesquehabitant."
"Nislrhoncusmattisrhoncusurnaneque.Orcinullapellentesque"
"dignissimenim.Acauctorauguemaurisauguenequegravidainfermentum."
"Lacussuspendissefaucibusinterdumposuere."
]
deftoast(text):
MDSnackbar(
MDSnackbarText(
text=text,
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.3,
).open()
classCopyLabel(MDLabel):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.allow_selection=True
self.adaptive_height=True
classExample(MDApp):
context_menu=None
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
fortextindata:
copy_label=CopyLabel(text=text)
copy_label.bind(on_selection=self.open_context_menu)
```

(continues on next page) 

**2.3. Components** 

**455** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.ids.box.add_widget(copy_label)
defclick_item_context_menu(
self,type_click:str,instance_label:CopyLabel
)->None:
Clipboard.copy(instance_label.text)
iftype_click=="copy":
toast("Copied")
eliftype_click=="cut":
self.root.ids.box.remove_widget(instance_label)
toast("Cut")
ifself.context_menu:
self.context_menu.dismiss()
defopen_context_menu(self,instance_label:CopyLabel)->None:
instance_label.text_color="black"
menu_items=[
{
"text":"Copytext",
"on_release":lambda:self.click_item_context_menu(
"copy",instance_label
),
},
{
"text":"Cuttext",
"on_release":lambda:self.click_item_context_menu(
"cut",instance_label
),
},
]
self.context_menu=MDDropdownMenu(
caller=instance_label,items=menu_items,width_mult=3
)
self.context_menu.open()
Example().run()
```

Declarative Python style 

```
fromkivy.core.clipboardimportClipboard
fromkivy.metricsimportdp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.snackbarimportMDSnackbar,MDSnackbarText
fromkivymd.appimportMDApp
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.menuimportMDDropdownMenu
fromkivymd.uix.textfieldimportMDTextField
fromkivymd.uix.widgetimportMDWidget
```

(continues on next page) 

**Chapter 2. Contents** 

**456** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
data=[
"Loremipsumdolorsitamet,consecteturadipiscingelit.",
"Sedblanditliberovolutpatsedcrasornarearcu.Nislvelpretium"
"lectusquamidleoin.Tinciduntarcunonsodalesnequesodalesutetiam.",
"Elitscelerisquemaurispellentesquepulvinarpellentesquehabitant."
"Nislrhoncusmattisrhoncusurnaneque.Orcinullapellentesque"
"dignissimenim.Acauctorauguemaurisauguenequegravidainfermentum."
"Lacussuspendissefaucibusinterdumposuere."
]
deftoast(text):
MDSnackbar(
MDSnackbarText(
text=text,
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.3,
).open()
classCopyLabel(MDLabel):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.allow_selection=True
self.adaptive_height=True
classExample(MDApp):
context_menu=None
defbuild(self):
return(
MDBoxLayout(
MDBoxLayout(
id="box",
orientation="vertical",
padding="24dp",
spacing="12dp",
adaptive_height=True,
),
MDTextField(
max_height="200dp",
mode="filled",
multiline=True,
),
MDWidget(),
orientation="vertical",
spacing="12dp",
padding="24dp",
md_bg_color=self.theme_cls.backgroundColor,
```

(continues on next page) 

**2.3. Components** 

**457** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
)
)
defon_start(self):
fortextindata:
copy_label=CopyLabel(text=text)
copy_label.bind(on_selection=self.open_context_menu)
self.root.get_ids().box.add_widget(copy_label)
defclick_item_context_menu(
self,type_click:str,instance_label:CopyLabel
)->None:
Clipboard.copy(instance_label.text)
iftype_click=="copy":
toast("Copied")
eliftype_click=="cut":
self.root.get_ids().box.remove_widget(instance_label)
toast("Cut")
ifself.context_menu:
self.context_menu.dismiss()
defopen_context_menu(self,instance_label:CopyLabel)->None:
instance_label.text_color="black"
menu_items=[
{
"text":"Copytext",
"on_release":lambda:self.click_item_context_menu(
"copy",instance_label
),
},
{
"text":"Cuttext",
"on_release":lambda:self.click_item_context_menu(
"cut",instance_label
),
},
]
self.context_menu=MDDropdownMenu(
caller=instance_label,items=menu_items,width_mult=3
)
self.context_menu.open()
Example().run()
```

**Chapter 2. Contents** 

**458** 

~~Ce~~ co 













**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
LabelBase.register(
name="MaterialSymbols",
fn_regular="Material_Symbols_Outlined-20-200-1_200.ttf",
)
self.theme_cls.font_styles["MaterialSymbols"]={
"large":{
"line-height":1.64,
"font-name":"MaterialSymbols",
"font-size":sp(57),
},
"medium":{
"line-height":1.52,
"font-name":"MaterialSymbols",
"font-size":sp(45),
},
"small":{
"line-height":1.44,
"font-name":"MaterialSymbols",
"font-size":sp(36),
},
}
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.core.textimportLabelBase
fromkivy.metricsimportsp
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonIcon,MDButtonText
fromkivymd.uix.labelimportMDIcon
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
LabelBase.register(
name="MaterialSymbols",
fn_regular="Material_Symbols_Outlined-20-200-1_200.ttf",
)
```

(continues on next page) 

**2.3. Components** 

**461** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.theme_cls.font_styles["MaterialSymbols"]={
"large":{
"line-height":1.64,
"font-name":"MaterialSymbols",
"font-size":sp(57),
},
"medium":{
"line-height":1.52,
"font-name":"MaterialSymbols",
"font-size":sp(45),
},
"small":{
"line-height":1.44,
"font-name":"MaterialSymbols",
"font-size":sp(36),
},
}
return(
MDScreen(
MDIcon(
icon="music_video",
theme_font_name="Custom",
font_name="MaterialSymbols",
pos_hint={"center_x":.5,"center_y":.58},
),
MDButton(
MDButtonIcon(
icon="music_video",
theme_font_name="Custom",
font_name="MaterialSymbols",
),
MDButtonText(
text="Elevated"
),
pos_hint={"center_x":.5,"center_y":.47}
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

**Chapter 2. Contents** 

**462** 



**KivyMD, Release 2.0.1.dev0** 

###### `text` 

Text of the label. 

_`text`_ is an `StringProperty` and defaults to _‘’_ . 

###### `text_color` 

Label text color in (r, g, b, a) or string format. 

_`text_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `allow_copy` 

Allows you to copy text to the clipboard by double-clicking on the label. 

Added in version 1.2.0. 

_`allow_copy`_ is an `BooleanProperty` and defaults to _False_ . 

###### `allow_selection` 

Allows to highlight text by double-clicking on the label. 

Added in version 1.2.0. 

_`allow_selection`_ is an `BooleanProperty` and defaults to _False_ . 

###### `color_selection` 

The color in (r, g, b, a) or string format of the text selection when the value of the _`allow_selection`_ attribute is True. 

Added in version 1.2.0. 

_`color_selection`_ is an `ColorProperty` and defaults to _None_ . 

###### `color_deselection` 

The color in (r, g, b, a) or string format of the text deselection when the value of the _`allow_selection`_ attribute is True. 

Added in version 1.2.0. 

_`color_deselection`_ is an `ColorProperty` and defaults to _None_ . 

###### `is_selected` 

Is the label text highlighted. 

Added in version 1.2.0. 

_`is_selected`_ is an `BooleanProperty` and defaults to _False_ . 

###### `radius` 

Label radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

`do_selection()` _→_ None 

`cancel_selection()` _→_ None 

`on_double_tap(` _touch_ , _*args_ `)` _→_ None 

Fired by double-clicking on the widget. 

`on_window_touch(` _*args_ `)` _→_ None 

Fired at the on_touch_down event. 

**Chapter 2. Contents** 

**464** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_copy(` _*args_ `)` _→_ None 

Fired when double-tapping on the label. 

Added in version 1.2.0. 

- `on_selection(` _*args_ `)` _→_ None 

Fired when double-tapping on the label. 

Added in version 1.2.0. 

- `on_cancel_selection(` _*args_ `)` _→_ None 

Fired when the highlighting is removed from the label text. 

Added in version 1.2.0. 

- `on_allow_selection(` _instance_label_ , _selection: bool_ `)` _→_ None 

Fired when the _`allow_selection`_ value changes. 

- `on_text_color(` _instance_label_ , _color: list | str_ `)` _→_ None Fired when the _`text_color`_ value changes. 

- `on_md_bg_color(` _instance_label_ , _color: list | str_ `)` _→_ None 

Fired when the `md_bg_color` value changes. 

- `on_size(` _instance_label_ , _size: list_ `)` _→_ None 

Fired when the parent window of the application is resized. 

`update_canvas_bg_pos(` _instance_label_ , _pos: list_ `)` _→_ None 

- `class kivymd.uix.label.label.MDIcon(` _*args_ , _**kwargs_ `)` 

Icon class. 

For more information, see in the _`MDLabel`_ class documentation. `icon` 

Label icon name. 

_`icon`_ is an `StringProperty` and defaults to _‘blank’_ . 

###### `source` 

Path to icon. 

_`source`_ is an `StringProperty` and defaults to _None_ . 

###### `icon_color` 

Icon color in (r, g, b, a) or string format. 

Added in version 2.0.0. 

_`icon_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `icon_color_disabled` 

The icon color in (r, g, b, a) or string format of the button when the button is disabled. 

Added in version 2.0.0. 

_`icon_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

**Parameters** 

**2.3. Components** 

**465** 





<!-- Start of picture text -->
9:30 VAn<br>Search « Pre *<br>Search lets people enter a keyword or phrase to get 2 Ping,ingHaneulu e-22fen<br>relevant 9information9 4 Q3 performancea.  summary<br>We will discuss our sales performance...<br>Resources a % € +2 Ping Yesterday<br>3 DN! Lao Qiang! (RRWT/EAH?<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

```
MDSearchBar:
id:search_bar
supporting_text:"Searchintext"
view_root:root
#SearchBar.
MDSearchBarLeadingContainer:
MDSearchLeadingIcon:
icon:"menu"
on_release:app.open_menu(self)
MDSearchBarTrailingContainer:
MDSearchTrailingIcon:
icon:"microphone"
MDSearchTrailingAvatar:
source:f"{images_path}/logo/kivymd-icon-128.png"
#SearchView.
MDSearchViewLeadingContainer:
MDSearchLeadingIcon:
icon:"arrow-left"
on_release:search_bar.close_view()
MDSearchViewTrailingContainer:
MDSearchTrailingIcon:
icon:"window-close"
MDSearchViewContainer:
...
```

**2.3. Components** 

**467** 



<!-- Start of picture text -->
=| Search<br>in text 1} we<br><!-- End of picture text -->

€ |Search in text yy, ab-testing |] abacus € _ abjad-arabic ™ abjad-hebrew c abugida-devanagari VY) _ abugida-thai (9) | access-point (tes access-point-check (1 access-point-minus 2) access-point-network i) access-point-network-off 



<!-- Start of picture text -->
xX<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text=StringProperty()
KV='''
#:importimages_pathkivymd.images_path
<IconItem>
theme_bg_color:"Custom"
md_bg_color:[0,0,0,0]
MDListItemLeadingIcon:
icon:root.icon
MDListItemSupportingText:
text:root.text
MDScreen:
md_bg_color:app.theme_cls.backgroundColor
BoxLayout:
padding:[dp(10),dp(30),dp(10),dp(10)]
orientation:"vertical"
MDSearchBar:
id:search_bar
supporting_text:"Searchintext"
view_root:root
on_text:app.set_list_md_icons(text=args[-1],search=True)
#SearchBaritems.
MDSearchBarLeadingContainer:
MDSearchLeadingIcon:
icon:"menu"
on_release:print("Menupressed")
MDSearchBarTrailingContainer:
MDSearchTrailingIcon:
icon:"microphone"
on_press:print("Microphonepressed")
MDSearchTrailingAvatar:
source:f"{images_path}/logo/kivymd-icon-128.png"
on_press:print("Avatarpressed")
#SearchView.
MDSearchViewLeadingContainer:
MDSearchLeadingIcon:
icon:"arrow-left"
```

(continues on next page) 

**Chapter 2. Contents** 

**470** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
on_release:search_bar.close_view()
MDSearchViewTrailingContainer:
MDSearchTrailingIcon:
icon:"window-close"
on_release:search_bar.text=""
MDSearchViewContainer:
RecycleView:
id:rv
key_viewclass:'viewclass'
key_size:'height'
RecycleBoxLayout:
default_size:None,dp(48)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
orientation:'vertical'
Widget:
BoxLayout:
size_hint_y:None
height:dp(30)
spacing:dp(10)
MDLabel:
text:"Bardock"
halign:"right"
MDSwitch:
on_active:search_bar.docked=args[-1]
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"
returnBuilder.load_string(KV)
defon_select_text(self,text):
self.root.ids.search_bar.text=text
defon_start(self):
self.set_list_md_icons()
defset_list_md_icons(self,text="",search=False):
defadd_icon_item(name_icon):
```

(continues on next page) 

**2.3. Components** 

**471** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.ids.rv.data.append(
{
"viewclass":"IconItem",
"icon":name_icon,
"text":name_icon,
"on_release":lambday=name_icon:self.on_select_text(y),
}
)
self.root.ids.rv.data=[]
forname_iconinmd_icons.keys():
ifsearch:
iftextinname_icon:
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty
fromkivymdimportimages_path
fromkivymd.icon_definitionsimportmd_icons
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.recycleboxlayoutimportMDRecycleBoxLayout
fromkivymd.uix.listimport(
MDListItem,
MDListItemLeadingIcon,
MDListItemSupportingText,
)
fromkivymd.uix.recycleviewimportMDRecycleView
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.searchimport(
MDSearchBar,
MDSearchBarLeadingContainer,
MDSearchLeadingIcon,
MDSearchBarTrailingContainer,
MDSearchTrailingIcon,
MDSearchTrailingAvatar,
MDSearchViewLeadingContainer,
MDSearchViewTrailingContainer,
MDSearchViewContainer,
)
fromkivymd.uix.selectioncontrolimportMDSwitch
fromkivymd.uix.widgetimportMDWidget
```

(continues on next page) 

**Chapter 2. Contents** 

**472** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classIconItem(MDListItem):
icon=StringProperty()
text=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.theme_bg_color="Custom"
self.md_bg_color=[0,0,0,0]
self.leading_icon=MDListItemLeadingIcon()
self.supporting_text=MDListItemSupportingText()
self.widgets=[
self.leading_icon,
self.supporting_text,
]
defon_icon(self,instance,value):
self.leading_icon.icon=value
defon_text(self,instance,value):
self.supporting_text.text=value
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Olive"
returnMDScreen(
MDBoxLayout(
MDSearchBar(
MDSearchBarLeadingContainer(
MDSearchLeadingIcon(
icon="menu",
on_release=lambdax:print("Menupressed"),
),
),
MDSearchBarTrailingContainer(
MDSearchTrailingIcon(
icon="microphone",
on_press=lambdax:print("Microphonepressed"),
),
MDSearchTrailingAvatar(
source=f"{images_path}/logo/kivymd-icon-128.png",
on_press=lambdax:print("Avatarpressed"),
),
),
MDSearchViewLeadingContainer(
MDSearchLeadingIcon(
```

(continues on next page) 

**2.3. Components** 

**473** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon="arrow-left",
on_release=lambdax:self.search_bar_close_view(),
),
),
MDSearchViewTrailingContainer(
MDSearchTrailingIcon(
icon="window-close",
on_release=lambdax:self.set_search_bar_text(),
),
),
MDSearchViewContainer(
MDRecycleView(
MDRecycleBoxLayout(
id="rv_box",
default_size=[None,dp(48)],
default_size_hint=[1,None],
size_hint_y=None,
orientation="vertical",
),
id="rv",
),
),
id="search_bar",
supporting_text="Searchintext",
),
MDWidget(),
MDBoxLayout(
MDLabel(
text="Bardock",
halign="right",
),
MDSwitch(
on_active=lambdax,y:self.set_docked(y),
),
size_hint_y=None,
height=dp(30),
spacing=dp(10),
),
padding=[dp(10),dp(30),dp(10),dp(10)],
orientation="vertical",
),
md_bg_color=self.theme_cls.backgroundColor,
)
defset_docked(self,value):
self.root.get_ids().search_bar.docked=value
defsearch_bar_close_view(self):
self.root.get_ids().search_bar.close_view()
defset_search_bar_text(self):
self.root.get_ids().search_bar.text=""
```

(continues on next page) 

**Chapter 2. Contents** 

**474** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defon_select_text(self,text):
self.root.get_ids().search_bar.text=text
defon_start(self):
search_bar=self.root.get_ids().search_bar
rv=self.root.get_ids().rv
rv_box=self.root.get_ids().rv_box
rv.key_size="height"
rv.key_viewclass="viewclass"
search_bar.view_root=self.root
rv_box.bind(minimum_height=rv_box.setter("height"))
search_bar.bind(
text=lambdainstance,text:self.set_list_md_icons(text,True)
)
self.set_list_md_icons()
defset_list_md_icons(self,text="",search=False):
defadd_icon_item(name_icon):
self.root.get_ids().rv.data.append(
{
"viewclass":"IconItem",
"icon":name_icon,
"text":name_icon,
"on_release":lambday=name_icon:self.on_select_text(y),
}
)
self.root.get_ids().rv.data=[]
forname_iconinmd_icons.keys():
ifsearch:
iftextinname_icon:
add_icon_item(name_icon)
else:
add_icon_item(name_icon)
Example().run()
```

**2.3. Components** 

**475** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.search.search` 

- `class kivymd.uix.search.search.MDSearchTrailingAvatar(` _**kwargs_ `)` 

Trailing avatar class. 

For more information, see in the `ButtonBehavior` and `Image` classes documentation. 

- `class kivymd.uix.search.search.MDSearchLeadingIcon(` _**kwargs_ `)` 

Leading icon class. 

For more information, see in the `ButtonBehavior` and `MDIcon` classes documentation. 

- `class kivymd.uix.search.search.MDSearchTrailingIcon(` _**kwargs_ `)` 

Trailing icon class. 

For more information, see in the `ButtonBehavior` and `MDIcon` classes documentation. 

- `class kivymd.uix.search.search.MDSearchBarTrailingContainer(` _*args_ , _**kwargs_ `)` Trailing container class for search bar. 

For more information, see in the `BoxLayout` class documentation. 

- `class kivymd.uix.search.search.MDSearchBarLeadingContainer(` _*args_ , _**kwargs_ `)` Leading container class for search bar. 

For more information, see in the `BoxLayout` class documentation. 

- `class kivymd.uix.search.search.MDSearchViewTrailingContainer(` _*args_ , _**kwargs_ `)` Trailing container class for search view. 

For more information, see in the `BoxLayout` class documentation. 

- `class kivymd.uix.search.search.MDSearchViewLeadingContainer(` _*args_ , _**kwargs_ `)` 

Leading container class for search view. 

For more information, see in the `BoxLayout` class documentation. 

- `class kivymd.uix.search.search.MDSearchViewContainer(` _*args_ , _**kwargs_ `)` 

A container for widgets that are displayed when the search bar is in focus. 

For more information, see in the `BoxLayout` class documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**Chapter 2. Contents** 

**476** 

**KivyMD, Release 2.0.1.dev0** 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`show_child(` _anim_time: float_ `)` _→_ None 

Displays the stored child widget with a fade-in animation. 

###### **Parameters** 

`anim_time` – Delay before showing the widget. 

###### `hide_child()` _→_ None 

Removes the stored child widget from the layout. 

###### `remove_widget(` _widget_ `)` 

Remove a widget from the children of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to remove from our children list. 

```
>>>fromkivy.uix.buttonimportButton
>>>root=Widget()
>>>button=Button()
>>>root.add_widget(button)
>>>root.remove_widget(button)
```

###### `class kivymd.uix.search.search.MDSearchBar(` _*args_ , _**kwargs_ `)` 

Search bar class. 

For more information, see in the `Widget` class documentation. 

###### `leading_icon` 

Leading icon name. 

_`leading_icon`_ is an `StringProperty` and defaults to _‘magnify’_ . 

###### `supporting_text` 

Supporting text. 

_`supporting_text`_ is an `StringProperty` and defaults to _‘Hinted search text’_ . 

###### `view_root` 

Root widget for search view. 

_`view_root`_ is an `ObjectProperty` and defaults to _None_ . 

###### `docked_width` 

Docked width. 

_`docked_width`_ is an `NumericProperty` and defaults to _dp(360)_ . 

###### `docked_height` 

Docked height. 

_`docked_height`_ is an `NumericProperty` and defaults to _dp(240)_ . 

**2.3. Components** 

**477** 

**KivyMD, Release 2.0.1.dev0** 

###### `docked` 

If _True_ , the search bar will be docked. 

_`docked`_ is an `BooleanProperty` and defaults to _False_ . 

```
text
```

Search query text. 

_`text`_ is an `StringProperty` and defaults to _‘’_ . 

`on_docked(` _instance_ , _docked_ `)` _→_ None 

Called when the _`docked`_ property changes. 

###### **Parameters** 

- `instance` – The MDSearchBar instance. 

- `docked` – The new docked value (True/False). 

Updates the size_hint_x and width accordingly. When docked, sets a fixed width using docked_width property. 

`on_supporting_text(` _instance_ , _text: str_ `)` _→_ None 

Called when the _`supporting_text`_ property changes. 

###### **Parameters** 

- `instance` – The MDSearchBar instance. 

- `text` – The new supporting text. 

Updates the hint text of the text input field to display the provided supporting text. 

- `on_view_root(` _*args_ `)` _→_ None 

Called when the view_root property changes. 

###### **Parameters** 

`args` – Arguments passed to the method. 

Removes the search widget from its current parent (if any), adds it to the new view_root, and initializes the search widget state and position. 

`add_widget(` _widget_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**Chapter 2. Contents** 

**478** 





<!-- Start of picture text -->
7" Good heathy lunch idea 9:20 AM<br>#P. Alejandro Ortega<br>>! Pre-sale concert tickets 2mins ago<br>~ Sofia Sacchi<br><> Carmen Villanueva<br>EE do Ine. esterday<br>Email archived Undo<br>Snackbars provide brief messages about app<br>processes at the bottom of the screen. _<br>8 @ Oe<br><!-- End of picture text -->





<!-- Start of picture text -->
‘Single-line snackbar with action, Action. : x. aa)<br><!-- End of picture text -->



<!-- Start of picture text -->
—<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Configurations** 

###### **1. Single line** 



```
MDSnackbar(
MDSnackbarText(
text="Single-linesnackbar",
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
```

**2. Single-line snackbar with action** 



```
MDSnackbar(
MDSnackbarSupportingText(
text="Single-linesnackbarwithaction",
),
MDSnackbarButtonContainer(
MDSnackbarActionButton(
MDSnackbarActionButtonText(
text="Actionbutton"
),
),
pos_hint={"center_y":0.5}
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
```

**2.3. Components** 

**481** 



<!-- Start of picture text -->
Single-line snackbar with action and close buttons Action button x<br><!-- End of picture text -->





<!-- Start of picture text -->
. . Action buttor x<br>with action and close butions<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDSnackbarActionButton(
MDSnackbarActionButtonText(
text="Actionbutton"
),
),
MDSnackbarCloseButton(
icon="close",
),
pos_hint={"center_y":0.5}
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
).open()
```

###### **5. Two-line snackbar with action and close buttons at the bottom** 



```
MDSnackbar(
MDSnackbarText(
text="Single-linesnackbarwithaction",
),
MDSnackbarSupportingText(
text="andclosebuttonsatthebottom",
padding=[0,0,0,dp(56)],
),
MDSnackbarButtonContainer(
Widget(),
MDSnackbarActionButton(
MDSnackbarActionButtonText(
text="Actionbutton"
),
),
MDSnackbarCloseButton(
icon="close",
),
),
y=dp(124),
```

(continues on next page) 

**2.3. Components** 

**483** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
pos_hint={"center_x":0.5},
size_hint_x=0.5,
padding=[0,0,"8dp","8dp"],
).open()
```

###### **API break** 

###### **1.1.1 version** 

```
snackbar=Snackbar(
text="Firststring",
snackbar_x="10dp",
snackbar_y="24dp",
)
snackbar.size_hint_x=(
Window.width-(snackbar.snackbar_x*2)
)/Window.width
snackbar.buttons=[
MDFlatButton(
text="Done",
theme_text_color="Custom",
text_color="#8E353C",
on_release=snackbar.dismiss,
),
]
snackbar.open()
```

###### **1.2.0 version** 

```
MDSnackbar(
MDLabel(
text="Firststring",
),
MDSnackbarActionButton(
text="Done",
theme_text_color="Custom",
text_color="#8E353C",
),
y=dp(24),
pos_hint={"center_x":0.5},
size_hint_x=0.5,
md_bg_color="#E8D8D7",
).open()
```

**Chapter 2. Contents** 

**484** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
MDSnackbar(
MDSnackbarSupportingText(
text="Single-linesnackbarwithaction",
),
MDSnackbarButtonContainer(
MDSnackbarActionButton(
MDSnackbarActionButtonText(
text="Actionbutton"
),
),
pos_hint={"center_y":0.5}
),
y=dp(24),
orientation="horizontal",
pos_hint={"center_x":0.5},
size_hint_x=0.5,
background_color=self.theme_cls.onPrimaryContainerColor,
).open()
```

###### **API -** `kivymd.uix.snackbar.snackbar` 

`class kivymd.uix.snackbar.snackbar.MDSnackbarButtonContainer(` _*args_ , _**kwargs_ `)` 

The class implements a container for placing snackbar buttons. 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

**2.3. Components** 

**485** 

**KivyMD, Release 2.0.1.dev0** 

###### `class kivymd.uix.snackbar.snackbar.MDSnackbarCloseButton(` _**kwargs_ `)` 

Snackbar closed button class. 

For more information, see in the _`MDIconButton`_ class documentation. 

- `class kivymd.uix.snackbar.snackbar.MDSnackbarActionButtonText(` _*args_ , _**kwargs_ `)` 

The class implements the text for the _`MDSnackbarActionButton`_ class. 

Changed in version 2.2.0. 

For more information, see in the _`MDButtonText`_ class documentation. 

- `class kivymd.uix.snackbar.snackbar.MDSnackbarActionButton(` _*args_ , _**kwargs_ `)` 

Snackbar action button class. 

For more information, see in the _`MDButton`_ class documentation. 

- `class kivymd.uix.snackbar.snackbar.MDSnackbar(` _*args_ , _**kwargs_ `)` 

Snackbar class. 

Changed in version 1.2.0: Rename _BaseSnackbar_ to _MDSnackbar_ class. 

For more information, see in the _`MotionShackBehavior`_ and _`MDCard`_ and class documentation. 

###### **Events** 

_`on_open`_ Fired when a snackbar opened. 

_`on_dismiss`_ Fired when a snackbar closes. 

###### `duration` 

The amount of time that the snackbar will stay on screen for. 

_`duration`_ is a `NumericProperty` and defaults to _3_ . 

###### `auto_dismiss` 

Whether to use automatic closing of the snackbar or not. 

_`auto_dismiss`_ is a `BooleanProperty` and defaults to _True_ . 

###### `radius` 

Snackbar radius. 

_`radius`_ is a `ListProperty` and defaults to _[dp(4), dp(4), dp(4), dp(4)]_ 

###### `background_color` 

The background color in (r, g, b, a) or string format of the snackbar. 

_`background_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `dismiss(` _*args_ `)` _→_ None 

Dismiss the snackbar. 

###### `open()` _→_ None 

Show the snackbar. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

**Chapter 2. Contents** 

**486** 

**KivyMD, Release 2.0.1.dev0** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`on_open(` _*args_ `)` _→_ None 

Fired when a snackbar opened. 

`on_dismiss(` _*args_ `)` _→_ None 

Fired when a snackbar closed. 

`class kivymd.uix.snackbar.snackbar.MDSnackbarText(` _*args_ , _**kwargs_ `)` 

The class implements the text. 

For more information, see in the _`MDLabel`_ class documentation. 

- `class kivymd.uix.snackbar.snackbar.MDSnackbarSupportingText(` _*args_ , _**kwargs_ `)` 

The class implements the supporting text. 

For more information, see in the _`MDLabel`_ class documentation. 

###### **2.3.46 SliverAppbar** 

Added in version 1.0.0. 

**MDSliverAppbar is a Material Design widget in KivyMD which gives scrollable or collapsible MDTopAppBar** 

**Note:** This widget is a modification of the silverappbar.py module. 

**2.3. Components** 

**487** 







<!-- Start of picture text -->
< ) Vi fo:<br>Sliiver&apphaksMia MDSliverAppbarContent<br>BEES<br>Js al >_> ne MDSliverAppbarHeader<br>«Ibanez“«" GRG121DX-BKF a<br>$445,99<br>«Ibanez“«" GRG121DX-BKF a<br>$445,99<br>«Ibanez“«" GRG121DX-BKF a MDSliverAppbarContent<br>$445,99<br>«Ibanez“«" GRG121DX-BKF a<br>$445,99<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative KV style 

```
fromkivy.lang.builderimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.listimportMDListItem
KV='''
<GuitarItem>
theme_bg_color:"Custom"
md_bg_color:"2d4a50"
MDListItemLeadingAvatar
source:"avatar.png"
MDListItemHeadlineText:
text:"Ibanez"
MDListItemSupportingText:
text:"GRG121DX-BKF"
MDListItemTertiaryText:
text:"$445,99"
MDListItemTrailingIcon:
icon:"guitar-electric"
MDScreen:
MDSliverAppbar:
background_color:"2d4a50"
hide_appbar:True
MDTopAppBar:
type:"medium"
MDTopAppBarLeadingButtonContainer:
MDActionTopAppBarButton:
icon:"arrow-left"
MDTopAppBarTitle:
text:"Slivertoolbar"
MDTopAppBarTrailingButtonContainer:
MDActionTopAppBarButton:
icon:"attachment"
MDActionTopAppBarButton:
```

(continues on next page) 

**2.3. Components** 

**489** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon:"calendar"
MDActionTopAppBarButton:
icon:"dots-vertical"
MDSliverAppbarHeader:
FitImage:
source:"bg.jpg"
MDSliverAppbarContent:
id:content
orientation:"vertical"
padding:"12dp"
theme_bg_color:"Custom"
md_bg_color:"2d4a50"
'''
classGuitarItem(MDListItem):
...
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
defon_start(self):
forxinrange(10):
self.root.ids.content.add_widget(GuitarItem())
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.appbarimport(
MDTopAppBar,
MDTopAppBarLeadingButtonContainer,
MDActionTopAppBarButton,
MDTopAppBarTitle,
MDTopAppBarTrailingButtonContainer,
```

```
)
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.listimport(
MDListItem,
MDListItemLeadingAvatar,
MDListItemHeadlineText,
MDListItemSupportingText,
MDListItemTertiaryText,
```

(continues on next page) 

**Chapter 2. Contents** 

**490** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDListItemTrailingIcon,
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.sliverappbarimport(
MDSliverAppbar,
MDSliverAppbarHeader,
MDSliverAppbarContent,
)
classGuitarItem(MDListItem):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.theme_bg_color="Custom"
self.md_bg_color="2d4a50"
self.widgets=[
MDListItemLeadingAvatar(source="avatar.png"),
MDListItemHeadlineText(text="Ibanez"),
MDListItemSupportingText(text="GRG121DX-BKF"),
MDListItemTertiaryText(text="$445,99"),
MDListItemTrailingIcon(icon="guitar-electric"),
]
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnMDScreen(
MDSliverAppbar(
MDTopAppBar(
MDTopAppBarLeadingButtonContainer(
MDActionTopAppBarButton(
icon="arrow-left",
),
),
MDTopAppBarTitle(
text="Slivertoolbar",
),
MDTopAppBarTrailingButtonContainer(
MDActionTopAppBarButton(
icon="attachment",
),
MDActionTopAppBarButton(
icon="calendar",
),
MDActionTopAppBarButton(
icon="dots-vertical",
),
),
type="medium",
),
MDSliverAppbarHeader(
```

(continues on next page) 

**2.3. Components** 

**491** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
FitImage(
source="bg.jpg",
),
),
MDSliverAppbarContent(
id="content",
orientation="vertical",
padding="12dp",
theme_bg_color="Custom",
md_bg_color="2d4a50",
),
background_color="2d4a50",
hide_appbar=True,
)
)
defon_start(self):
forxinrange(10):
self.root.get_ids().content.add_widget(GuitarItem())
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

```
#:importSliverToolbar__main__.SliverToolbar
```

```
Root:
```

```
MDSliverAppbar:
[...]
MDSliverAppbarHeader:
[...]
MDSliverAppbarContent:
[...]
```

```
classSliverToolbar(MDTopAppBar):
[...]
```

**Chapter 2. Contents** 

**492** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
Root:
MDSliverAppbar:
[...]
MDTopAppBar:
[...]
MDSliverAppbarHeader:
[...]
MDSliverAppbarContent:
[...]
```

###### **API -** `kivymd.uix.sliverappbar.sliverappbar` 

###### `class kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbarContent(` _*args_ , _**kwargs_ `)` 

Implements a box for a scrollable list of custom items. 

For more information, see in the _`MDBoxLayout`_ class documentation. 

###### `class kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbarHeader(` _*args_ , _**kwargs_ `)` 

Sliver app bar header class. 

For more information, see in the `BoxLayout` class documentation. 

###### `class kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar(` _*args_ , _**kwargs_ `)` 

Sliver appbar class. 

For more information, see in the _`ThemableBehavior`_ and `BoxLayout` classes documentation. 

###### **Events** 

```
on_scroll_content
```

Fired when the list of custom content is being scrolled. 

###### `background_color` 

Background color of appbar in (r, g, b, a) or string format. 

_`background_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `max_height` 

Distance from top of screen to start of custom list content. 

```
MDSliverAppbar:
max_height:"200dp"
```

**2.3. Components** 

**493** 



<!-- Start of picture text -->
Sliver appbar RKO<br> ._\banez ¥<br>@ .  \banez ¥<br>@.._ \banez ¥<br><!-- End of picture text -->







**KivyMD, Release 2.0.1.dev0** 



_`radius`_ is an `VariableListProperty` and defaults to _[20]_ . 

###### `max_opacity` 

Maximum background transparency value for the _`MDSliverAppbarHeader`_ class. 

```
MDSliverAppbar:
max_opacity:.5
```

_`max_opacity`_ is an `NumericProperty` and defaults to _1_ . 

- `on_hide_appbar(` _instance_ , _value_ `)` _→_ None 

Fired when the _hide_appbar_ value changes. 

`on_scroll_content(` _instance: object = None_ , _value: float = 1.0_ , _direction: str = 'up'_ `)` 

Fired when the list of custom content is being scrolled. 

###### **Parameters** 

- `instance` – _`MDSliverAppbar`_ 

- `value` – see `scroll_y` 

- `direction` – scroll direction: ‘up/down’ 

`on_background_color(` _instance_ , _color_ `)` _→_ None 

Fired when the _background_color_ value changes. 

`on_vbar()` _→_ None 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

**2.3. Components** 

**495** 





<!-- Start of picture text -->
—<br>30 v.45<br>T. e mo:<br>Saved podcasts<br>bars lo-<br>Top app bars display information and actions at the “fh <li ee]<br>top of a screen ea A —<br>Wizards & Wynona At Peace<br><!-- End of picture text -->



<!-- Start of picture text -->
@ = Title Large ©<br>@ € Title Large 0 & :<br>@ Headline€ Small 0 8 :<br>€ 0A :<br>Headline Medium<br><!-- End of picture text -->









<!-- Start of picture text -->
MDActionTopAppBarButton<br>| MDTopAppBarrTitle MDActionTopAppBarButton<br>¢  AppBar small © f :<br>MDTopAppBarLeadingButtonContainer<br><!-- End of picture text -->

MDTopAppBarTrailingButtonContainer 

**KivyMD, Release 2.0.1.dev0** 

###### **Configurations** 

###### **1. Center-aligned** 

Imperative python style with KV 

```
MDScreen:
md_bg_color:self.theme_cls.secondaryContainerColor
MDTopAppBar:
type:"small"
size_hint_x:.8
pos_hint:{"center_x":.5,"center_y":.5}
MDTopAppBarLeadingButtonContainer:
MDActionTopAppBarButton:
icon:"menu"
MDTopAppBarTitle:
text:"AppBarsmall"
halign:"center"
MDTopAppBarTrailingButtonContainer:
MDActionTopAppBarButton:
icon:"account-circle-outline"
```

Declarative python style 

```
MDScreen(
MDTopAppBar(
MDTopAppBarLeadingButtonContainer(
MDActionTopAppBarButton(
icon="menu",
),
),
MDTopAppBarTitle(
text="AppBarsmall",
halign="center",
),
MDTopAppBarTrailingButtonContainer(
MDActionTopAppBarButton(
icon="account-circle-outline",
),
),
type="small",
size_hint_x=.8,
pos_hint={"center_x":0.5,"center_y":0.5},
),
md_bg_color=self.theme_cls.secondaryContainerColor,
)
```

**2.3. Components** 

**499** 



<!-- Start of picture text -->
= AppBar Center-aligned a)<br><!-- End of picture text -->









<!-- Start of picture text -->
<  AppBar small e f :<br>€ e ff :<br>AppBar medium<br><!-- End of picture text -->



<!-- Start of picture text -->
€ e @ :<br>AppBar large<br>Bottom =3<br>app bar i A<br>A bottom app bar displays navigation and key | jal a = :<br>actions at the bottom of mobile screens. > — ic<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.appbarimportMDBottomAppBar,MDFabBottomAppBarButton
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDBottomAppBar(
MDFabBottomAppBarButton(
icon="plus",
),
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```



###### **Add action items** 

```
#:importMDActionBottomAppBarButtonkivymd.uix.appbar.MDActionBottomAppBarButton
```

```
MDScreen:
```

```
MDBottomAppBar:
action_items:
[
```

(continues on next page) 

**2.3. Components** 

**503** 







**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`MDActionBottomAppBarButton(icon="download-box-outline"), ] def build(self): self.theme_cls.theme_style = "Dark" return Builder.load_string(KV) Example().run()` Declarative python style `from kivymd.app import MDApp from kivymd.uix.appbar import ( MDBottomAppBar, MDFabBottomAppBarButton, MDActionBottomAppBarButton ) from kivymd.uix.screen import MDScreen class Example(MDApp): def change_actions_items(self, *args): self.screen.get_ids().bottom_appbar.action_items = [ MDActionBottomAppBarButton(icon="magnify"), MDActionBottomAppBarButton(icon="trash-can-outline"), MDActionBottomAppBarButton(icon="download-box-outline"), ] def build(self): self.theme_cls.theme_style = "Dark" self.screen = ( MDScreen( MDBottomAppBar( MDFabBottomAppBarButton( icon="plus", on_release=self.change_actions_items, ), id="bottom_appbar", ), md_bg_color=self.theme_cls.backgroundColor, ) ) self.screen.get_ids().bottom_appbar.action_items = [ MDActionBottomAppBarButton(icon="gmail"), MDActionBottomAppBarButton(icon="bookmark"), ] return self.screen Example().run()` 

**2.3. Components** 

**505** 

**KivyMD, Release 2.0.1.dev0** 

###### **A practical example** 

```
importasynckivy
fromkivy.clockimportClock
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty,BooleanProperty,ObjectProperty
fromkivy.uix.behaviorsimportStateFocusBehavior
fromkivy.uix.recycleboxlayoutimportRecycleBoxLayout
fromkivy.uix.recycleview.layoutimportLayoutSelectionBehavior
fromkivy.uix.recycleview.viewsimportRecycleDataViewBehavior
fromkivymd.uix.appbarimportMDActionBottomAppBarButton
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.appimportMDApp
fromfakerimportFaker#pipinstallFaker
KV='''
#:importMDFabBottomAppBarButtonkivymd.uix.appbar.MDFabBottomAppBarButton
<UserCard>
orientation:"vertical"
adaptive_height:True
md_bg_color:"#373A22"ifself.selectedelse"#1F1E15"
radius:16
padding:0,0,0,"16dp"
MDListItem:
theme_bg_color:"Custom"
md_bg_color:root.md_bg_color
radius:root.radius
ripple_effect:False
MDListItemLeadingAvatar:
source:root.avatar
#radius:self.height/2
MDListItemHeadlineText:
text:root.name
theme_text_color:"Custom"
text_color:"#8A8D79"
MDListItemSupportingText:
text:root.time
theme_text_color:"Custom"
text_color:"#8A8D79"
MDLabel:
text:root.text
adaptive_height:True
```

(continues on next page) 

**Chapter 2. Contents** 

**506** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
theme_text_color:"Custom"
text_color:"#8A8D79"
padding_x:"16dp"
shorten:True
shorten_from:"right"
Widget:
MDFloatLayout:
md_bg_color:"#151511"
RecycleView:
id:card_list
viewclass:"UserCard"
SelectableRecycleGridLayout:
orientation:'vertical'
spacing:"16dp"
padding:"16dp"
default_size:None,dp(120)
default_size_hint:1,None
size_hint_y:None
height:self.minimum_height
multiselect:True
touch_multiselect:True
MDBottomAppBar:
id:bottom_appbar
scroll_cls:card_list
allow_hidden:True
theme_bg_color:"Custom"
md_bg_color:"#232217"
MDFabBottomAppBarButton:
id:fab_button
icon:"plus"
theme_bg_color:"Custom"
md_bg_color:"#373A22"
theme_icon_color:"Custom"
icon_color:"#ffffff"
'''
classUserCard(RecycleDataViewBehavior,MDBoxLayout):
name=StringProperty()
time=StringProperty()
text=StringProperty()
avatar=StringProperty()
callback=ObjectProperty(lambdax:x)
index=None
```

(continues on next page) 

**2.3. Components** 

**507** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
selected=BooleanProperty(False)
selectable=BooleanProperty(True)
defrefresh_view_attrs(self,rv,index,data):
self.index=index
returnsuper().refresh_view_attrs(rv,index,data)
defon_touch_down(self,touch):
ifsuper().on_touch_down(touch):
returnTrue
ifself.collide_point(*touch.pos)andself.selectable:
Clock.schedule_once(self.callback)
returnself.parent.select_with_touch(self.index,touch)
```

```
defapply_selection(self,rv,index,is_selected):
self.selected=is_selected
rv.data[index]["selected"]=is_selected
```

```
classSelectableRecycleGridLayout(
StateFocusBehavior,LayoutSelectionBehavior,RecycleBoxLayout
):
pass
```

```
classBottomAppBarButton(MDActionBottomAppBarButton):
theme_icon_color="Custom"
icon_color="#8A8D79"
classExample(MDApp):
selected_cards=False
defbuild(self):
returnBuilder.load_string(KV)
defon_tap_card(self,*args):
datas=[data["selected"]fordatainself.root.ids.card_list.data]
ifTrueindatasandnotself.selected_cards:
self.root.ids.bottom_appbar.action_items=[
BottomAppBarButton(icon="gmail"),
BottomAppBarButton(icon="label-outline"),
BottomAppBarButton(icon="bookmark"),
]
self.root.ids.fab_button.icon="pencil"
self.selected_cards=True
else:
iflen(list(set(datas)))==1andnotlist(set(datas))[0]:
self.selected_cards=False
ifnotself.selected_cards:
self.root.ids.bottom_appbar.action_items=[
BottomAppBarButton(icon="magnify"),
```

(continues on next page) 

**Chapter 2. Contents** 

**508** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
BottomAppBarButton(icon="trash-can-outline"),
BottomAppBarButton(icon="download-box-outline"),
]
self.root.ids.fab_button.icon="plus"
defon_start(self):
asyncdefgenerate_card():
foriinrange(10):
awaitasynckivy.sleep(0)
self.root.ids.card_list.data.append(
{
"name":fake.name(),
"time":fake.date(),
"avatar":fake.image_url(),
"text":fake.text(),
"selected":False,
"callback":self.on_tap_card,
}
)
self.on_tap_card()
fake=Faker()
Clock.schedule_once(lambdax:asynckivy.start(generate_card()))
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

`MDTopAppBar: type_height: "large" headline_text: "Headline" left_action_items: [["arrow-left", lambda x: x]] right_action_items: [ ["attachment", lambda x: x], ["calendar", lambda x: x],` _˓→_ `["dots-vertical", lambda x: x], ] anchor_title: "left"` 

**2.3. Components** 

**509** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
MDTopAppBar:
type:"large"
MDTopAppBarLeadingButtonContainer:
MDActionTopAppBarButton:
icon:"arrow-left"
MDTopAppBarTitle:
text:"AppBarsmall"
MDTopAppBarTrailingButtonContainer:
MDActionTopAppBarButton:
icon:"attachment"
MDActionTopAppBarButton:
icon:"calendar"
MDActionTopAppBarButton:
icon:"dots-vertical"
```

###### **API -** `kivymd.uix.appbar.appbar` 

###### `class kivymd.uix.appbar.appbar.MDFabBottomAppBarButton(` _**kwargs_ `)` 

Implements a floating action button (FAB) for a bar with type ‘bottom’. 

For more information, see in the _`MDFabButton`_ and _`RotateBehavior`_ and _`ScaleBehavior`_ and classes documentation. 

- `class kivymd.uix.appbar.appbar.MDActionTopAppBarButton(` _**kwargs_ `)` 

Implements action buttons on the bar. 

For more information, see in the _`MDIconButton`_ class documentation. 

###### `md_bg_color_disabled` 

The background color in (r, g, b, a) or string format of the button when the button is disabled. 

_`md_bg_color_disabled`_ is a `ColorProperty` and defaults to _None_ . 

###### `class kivymd.uix.appbar.appbar.MDActionBottomAppBarButton(` _**kwargs_ `)` 

Implements action buttons for a :class:’~kivymd.uix.appbar.appbar.MDBottomAppBar’ class. 

Added in version 1.2.0. 

For more information, see in the _`MDActionTopAppBarButton`_ class documentation. 

- `class kivymd.uix.appbar.appbar.MDTopAppBarTitle(` _*args_ , _**kwargs_ `)` 

Implements the panel title. 

Added in version 2.0.0. 

For more information, see in the _`MDLabel`_ class documentation. 

**Chapter 2. Contents** 

**510** 

**KivyMD, Release 2.0.1.dev0** 

- `class kivymd.uix.appbar.appbar.MDTopAppBarLeadingButtonContainer(` _*args_ , _**kwargs_ `)` 

Implements a container for the leading action buttons. 

Added in version 2.0.0. 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

- `class kivymd.uix.appbar.appbar.MDTopAppBarTrailingButtonContainer(` _*args_ , _**kwargs_ `)` 

Implements a container for the trailing action buttons. 

Added in version 2.0.0. 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

- `class kivymd.uix.appbar.appbar.MDTopAppBar(` _*args_ , _**kwargs_ `)` 

Top app bar class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`CommonElevationBehavior`_ and _`BackgroundColorBehavior`_ and `BoxLayout` and _`WindowController`_ classes documentation. 

###### **Events** 

###### **_on_action_button_** 

Method for the button used for the _`MDBottomAppBar`_ class. 

###### `set_bars_color` 

If _True_ the background color of the bar status will be set automatically according to the current color of the bar. 

Added in version 1.0.0. 

See set_bars_colors for more information. 

_`set_bars_color`_ is an `BooleanProperty` and defaults to _False_ . 

```
type
```

Bar height type. 

Added in version 1.0.0. 

Available options are: ‘medium’, ‘large’, ‘small’. 

`type_height` is an `OptionProperty` and defaults to _‘small’_ . 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

**2.3. Components** 

**511** 

**KivyMD, Release 2.0.1.dev0** 

###### Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.appbar.appbar.MDBottomAppBar(` _*args_ , _**kwargs_ `)` 

Bottom app bar class. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and _`CommonElevationBehavior`_ and `FloatLayout` classes documentation. 

###### **Events** 

###### **_on_show_bar_** 

The method is fired when the _`MDBottomAppBar`_ panel is shown. 

###### **_on_hide_bar_** 

The method is fired when the _`MDBottomAppBar`_ panel is hidden. 

###### `action_items` 

The icons on the left bar. 

Added in version 1.2.0. 

_`action_items`_ is an `ListProperty` and defaults to _[]_ . 

###### `animation` 

# TODO: add description. # FIXME: changing the value does not affect anything. 

Added in version 1.2.0. 

_`animation`_ is an `BooleanProperty` and defaults to _True_ . 

###### `show_transition` 

Type of button display transition. 

Added in version 1.2.0. 

_`show_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `hide_transition` 

Type of button hidden transition. 

Added in version 1.2.0. 

_`hide_transition`_ is a `StringProperty` and defaults to _‘in_back’_ . 

###### `hide_duration` 

Duration of button hidden transition. 

Added in version 1.2.0. 

_`hide_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

**Chapter 2. Contents** 

**512** 

**KivyMD, Release 2.0.1.dev0** 

###### `show_duration` 

Duration of button display transition. 

Added in version 1.2.0. 

_`show_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `scroll_cls` 

Widget inherited from the `ScrollView` class. The value must be set if the _`allow_hidden`_ parameter is _True_ . 

Added in version 1.2.0. 

_`scroll_cls`_ is a `ObjectProperty` and defaults to _None_ . 

###### `allow_hidden` 

Allows or disables hiding the panel when scrolling content. If the value is _True_ , the _`scroll_cls`_ parameter must be specified. 

Added in version 1.2.0. 

_`allow_hidden`_ is a `BooleanProperty` and defaults to _False_ . 

###### `bar_is_hidden` 

Is the panel currently hidden. 

Added in version 1.2.0. 

_`bar_is_hidden`_ is a `BooleanProperty` and defaults to _False_ . 

`button_centering_animation(` _button:_ MDActionBottomAppBarButton _|_ MDFabBottomAppBarButton `)` _→_ None 

Animation of centering buttons for `MDActionOverFlowButton` , _`MDActionBottomAppBarButton`_ and _`MDFabBottomAppBarButton`_ classes. 

`check_scroll_direction(` _scroll_cls_ , _y: float_ `)` _→_ None 

Checks the scrolling direction. Depending on the scrolling direction, hides or shows the _`MDBottomAppBar`_ panel. 

`show_bar()` _→_ None 

Show _`MDBottomAppBar`_ panel. 

`hide_bar()` _→_ None 

Hide _`MDBottomAppBar`_ panel. 

- `on_show_bar(` _*args_ `)` _→_ None 

The method is fired when the _`MDBottomAppBar`_ panel is shown. 

- `on_hide_bar(` _*args_ `)` _→_ None 

The method is fired when the _`MDBottomAppBar`_ panel is hidden. 

`on_scroll_cls(` _instance_ , _scroll_cls_ `)` _→_ None 

Fired when the value of the _`scroll_cls`_ attribute changes. 

- `on_size(` _*args_ `)` _→_ None 

Fired when the root screen is resized. 

- `on_action_items(` _instance_ , _value: list_ `)` _→_ None 

Fired when the value of the _`action_items`_ attribute changes. 

**2.3. Components** 

**513** 

**KivyMD, Release 2.0.1.dev0** 

###### `set_fab_opacity(` _*ars_ `)` _→_ None 

Sets the transparency value of the:class: _~MDFabBottomAppBarButton_ button. 

- `set_fab_icon(` _instance_ , _value_ `)` _→_ None 

Animates the size of the _`MDFabBottomAppBarButton`_ button. 

- `add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### **2.3.48 Divider** 

Added in version 2.0.0. 

###### **See also:** 

Material Design 3 spec, Divider 

**Chapter 2. Contents** 

**514** 



<!-- Start of picture text -->
9:30 VA<br>= Inbox Q i<br>Divider ne glee<br>Dividers are thin lines that group content in lists or other Fone ae ns sna ;<br>containers<br><!-- End of picture text -->

###### Today 

###### Cumpleanhos de mama 

Hola, en mi casa if you all help with the food. Should we ... 

###### Graduacion de Inés 

Hola hija mia, aqui tienes unas fotos preciosas de Inés en... 

###### Pre-sale concert tickets 

| just saw there are a couple good shows lined up next m... 

###### Console ideas 

Do you remember that cafe we went to a few months ago 



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDDivider:
size_hint_x:.5
theme_divider_color:"Custom"
color:self.theme_cls.onBackgroundColor
pos_hint:{'center_x':.5,'center_y':.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
MDDivider(
size_hint_x=0.5,
pos_hint={'center_x':0.5,'center_y':0.5},
theme_divider_color="Custom",
color=self.theme_cls.onBackgroundColor,
),
md_bg_color=self.theme_cls.backgroundColor
)
)
Example().run()
```

**Chapter 2. Contents** 

**516** 





<!-- Start of picture text -->
«=—_ @ : i & by Selen Zeynep<br>»<br>% J 1 i What Buttons are Artists Pushing When<br>- é 53 Lj They Perform Live<br>¢<br>y y meen! The general consensus is that artists using digital<br>\ perce ae turntables are just pushing random buttons when they<br>| a ! Rs | _ perform live. But is that true? In the DMC<br>: 2G BE Championships it's obvious that some artists are<br>. . “ES : putting their various honed skills on display.<br>= : “a a‘ : 2 EN > j<br>pil ms “= Most of the scorn for solo performers comes from<br>= ee the many who headline huge festivals.<br>& 7 —_—<br>oS ame Q) Favourite =, Add to playlist<br><!-- End of picture text -->









~~S~~ S 



<!-- Start of picture text -->
—_,<br>Navigatione e _ ;<br>drawer 7 ;<br>Navigation drawers let people switch between UI views on larger i “Recs rs<br>devices Oo7 os -<br>ov<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
#Thiscustomruleshouldimplementwhatwillbedisplayedin
#yourMDNavigationDrawer.
ContentNavigationDrawer:
```

Declarative python style 

```
Root(
MDNavigationLayout(
MDScreenManager(
Screen_1(
...
),
Screen_2(
...
),
),
MDNavigationDrawer(
#Thiscustomruleshouldimplementwhatwillbedisplayedin
#yourMDNavigationDrawer.
ContentNavigationDrawer(
...
)
)
)
)
```

###### **A simple example** 

Declarative KV styles 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDNavigationLayout:
MDScreenManager:
MDScreen:
MDButton:
pos_hint:{"center_x":.5,"center_y":.5}
on_release:nav_drawer.set_state("toggle")
MDButtonText:
text:"OpenDrawer"
```

(continues on next page) 

**Chapter 2. Contents** 

**520** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationDrawer:
id:nav_drawer
radius:0,dp(16),dp(16),0
MDNavigationDrawerMenu:
MDNavigationDrawerLabel:
text:"Mail"
MDNavigationDrawerItem:
MDNavigationDrawerItemLeadingIcon:
icon:"account"
MDNavigationDrawerItemText:
text:"Inbox"
MDNavigationDrawerItemTrailingText:
text:"24"
MDNavigationDrawerDivider:
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python styles 

```
fromkivy.metricsimportdp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.screenmanagerimportMDScreenManager
fromkivymd.uix.navigationdrawerimport(
MDNavigationLayout,
MDNavigationDrawer,
MDNavigationDrawerMenu,
MDNavigationDrawerLabel,
MDNavigationDrawerItem,
MDNavigationDrawerItemLeadingIcon,
MDNavigationDrawerItemText,
MDNavigationDrawerItemTrailingText,
MDNavigationDrawerDivider,
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.appimportMDApp
```

(continues on next page) 

**2.3. Components** 

**521** 

**KivyMD, Release 2.0.1.dev0** 



<!-- Start of picture text -->
(continued from previous page)<br>class Example(MDApp):<br>def build(self):<br>return MDScreen(<br>MDNavigationLayout(<br>MDScreenManager(<br>MDScreen(<br>MDButton(<br>MDButtonText(<br>text="Open Drawer",<br>),<br>on_release=lambda x: self.root.get_ids().nav_drawer.set_<br>˓→ state(<br>"toggle"<br>),<br>pos_hint={"center_x": 0.5, "center_y": 0.5},<br>),<br>),<br>),<br>MDNavigationDrawer(<br>MDNavigationDrawerMenu(<br>MDNavigationDrawerLabel(<br>text="Mail",<br>),<br>MDNavigationDrawerItem(<br>MDNavigationDrawerItemLeadingIcon(<br>icon="account",<br>),<br>MDNavigationDrawerItemText(<br>text="Inbox",<br>),<br>MDNavigationDrawerItemTrailingText(<br>text="24",<br>),<br>),<br>MDNavigationDrawerDivider(<br>),<br>),<br>id="nav_drawer",<br>radius=(0, dp(16), dp(16), 0),<br>),<br>),<br>md_bg_color=self.theme_cls.backgroundColor,<br>)<br>Example().run()<br><!-- End of picture text -->

**Chapter 2. Contents** 

**522** 



<!-- Start of picture text -->
Mail<br>3B sinbox 9A<br>MDNavigationDrawerDivider<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

```
MDNavigationDrawerItem(
MDNavigationDrawerItemLeadingIcon(
icon="account"
),
MDNavigationDrawerItemText(
text="Inbox"
),
MDNavigationDrawerItemTrailingText(
text="24"
),
)
```



###### **Type drawer** 

###### **Standard** 

```
MDNavigationDrawer:
drawer_type:"standard"
```

###### **Modal** 

```
MDNavigationDrawer:
drawer_type:"modal"
```

###### **Anchoring screen edge for drawer** 

###### **Left** 

```
MDNavigationDrawer:
anchor:"left"
```

**Chapter 2. Contents** 

**524** 



<!-- Start of picture text -->
Mail<br>2 Inbox 24<br>Close Drawer<br><!-- End of picture text -->







**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
selected_color:"#4a4939"
_no_ripple_effect:True
MDScreen:
MDNavigationLayout:
MDScreenManager:
MDScreen:
MDRaisedButton:
text:"OpenDrawer"
pos_hint:{"center_x":.5,"center_y":.5}
on_release:nav_drawer.set_state("toggle")
MDNavigationDrawer:
id:nav_drawer
radius:(0,dp(16),dp(16),0)
MDNavigationDrawerMenu:
MDNavigationDrawerHeader:
title:"Headertitle"
title_color:"#4a4939"
text:"Headertext"
spacing:"4dp"
padding:"12dp",0,0,"56dp"
MDNavigationDrawerLabel:
text:"Mail"
DrawerClickableItem:
icon:"gmail"
right_text:"+99"
text_right_color:"#4a4939"
text:"Inbox"
DrawerClickableItem:
icon:"send"
text:"Outbox"
MDNavigationDrawerDivider:
MDNavigationDrawerLabel:
text:"Labels"
DrawerLabelItem:
icon:"information-outline"
text:"Label"
```

(continues on next page) 

**2.3. Components** 

**527** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
DrawerLabelItem:
icon:"information-outline"
text:"Label"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

###### **2.2.0 version** 

Declarative Python style with KV 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty,ColorProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.navigationdrawerimport(
MDNavigationDrawerItem,MDNavigationDrawerItemTrailingText
)
KV='''
<DrawerItem>
active_indicator_color:"#e7e4c0"
MDNavigationDrawerItemLeadingIcon:
icon:root.icon
theme_icon_color:"Custom"
icon_color:"#4a4939"
MDNavigationDrawerItemText:
text:root.text
theme_text_color:"Custom"
text_color:"#4a4939"
<DrawerLabel>
adaptive_height:True
padding:"18dp",0,0,"12dp"
MDNavigationDrawerItemLeadingIcon:
icon:root.icon
theme_icon_color:"Custom"
icon_color:"#4a4939"
pos_hint:{"center_y":.5}
```

(continues on next page) 

**Chapter 2. Contents** 

**528** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationDrawerLabel:
text:root.text
theme_text_color:"Custom"
text_color:"#4a4939"
pos_hint:{"center_y":.5}
padding:"6dp",0,"16dp",0
theme_line_height:"Custom"
line_height:0
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDNavigationLayout:
MDScreenManager:
MDScreen:
MDButton:
pos_hint:{"center_x":.5,"center_y":.5}
on_release:nav_drawer.set_state("toggle")
MDButtonText:
text:"OpenDrawer"
MDNavigationDrawer:
id:nav_drawer
radius:0,dp(16),dp(16),0
MDNavigationDrawerMenu:
MDNavigationDrawerHeader:
orientation:"vertical"
padding:0,0,0,"12dp"
adaptive_height:True
MDLabel:
text:"Headertitle"
theme_text_color:"Custom"
theme_line_height:"Custom"
line_height:0
text_color:"#4a4939"
adaptive_height:True
padding_x:"16dp"
font_style:"Display"
role:"small"
MDLabel:
text:"Headertext"
padding_x:"18dp"
adaptive_height:True
```

(continues on next page) 

**2.3. Components** 

**529** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
font_style:"Title"
role:"large"
MDNavigationDrawerDivider:
DrawerItem:
icon:"gmail"
text:"Inbox"
trailing_text:"+99"
trailing_text_color:"#4a4939"
DrawerItem:
icon:"send"
text:"Outbox"
MDNavigationDrawerDivider:
MDNavigationDrawerLabel:
text:"Labels"
padding_y:"12dp"
DrawerLabel:
icon:"information-outline"
text:"Label"
DrawerLabel:
icon:"information-outline"
text:"Label"
'''
classDrawerLabel(MDBoxLayout):
icon=StringProperty()
text=StringProperty()
classDrawerItem(MDNavigationDrawerItem):
icon=StringProperty()
text=StringProperty()
trailing_text=StringProperty()
trailing_text_color=ColorProperty()
_trailing_text_obj=None
defon_trailing_text(self,instance,value):
self._trailing_text_obj=MDNavigationDrawerItemTrailingText(
text=value,
theme_text_color="Custom",
text_color=self.trailing_text_color,
)
self.add_widget(self._trailing_text_obj)
```

(continues on next page) 

**Chapter 2. Contents** 

**530** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defon_trailing_text_color(self,instance,value):
self._trailing_text_obj.text_color=value
```

```
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivy.propertiesimportStringProperty,ColorProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.navigationdrawerimport(
MDNavigationDrawerItem,
MDNavigationDrawerItemTrailingText,
MDNavigationLayout,
MDNavigationDrawer,
MDNavigationDrawerMenu,
MDNavigationDrawerHeader,
MDNavigationDrawerDivider,
MDNavigationDrawerLabel,
MDNavigationDrawerItemLeadingIcon,
MDNavigationDrawerItemText,
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.screenmanagerimportMDScreenManager
classDrawerLabel(MDBoxLayout):
icon=StringProperty()
text=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDNavigationDrawerItemLeadingIcon(
icon=self.icon,
theme_icon_color="Custom",
icon_color="#4a4939",
pos_hint={"center_y":.5},
),
MDNavigationDrawerLabel(
text=self.text,
theme_text_color="Custom",
```

(continues on next page) 

**2.3. Components** 

**531** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text_color="#4a4939",
pos_hint={"center_y":.5},
padding=("6dp",0,"16dp",0),
theme_line_height="Custom",
line_height=0,
)
]
classDrawerItem(MDNavigationDrawerItem):
icon=StringProperty()
text=StringProperty()
trailing_text=StringProperty()
trailing_text_color=ColorProperty()
_trailing_text_obj=None
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDNavigationDrawerItemLeadingIcon(
icon=self.icon,
theme_icon_color="Custom",
icon_color="#4a4939",
),
MDNavigationDrawerItemText(
text=self.text,
theme_text_color="Custom",
text_color="#4a4939",
id="DDD"
)
]
defon_trailing_text(self,instance,value):
self._trailing_text_obj=MDNavigationDrawerItemTrailingText(
text=value,
theme_text_color="Custom",
text_color=self.trailing_text_color,
)
self.add_widget(self._trailing_text_obj)
defon_trailing_text_color(self,instance,value):
self._trailing_text_obj.text_color=value
classExample(MDApp):
defopen_drawer(self,*args):
self.root.get_ids().nav_drawer.set_state("toggle")
defbuild(self):
return(
MDScreen(
```

(continues on next page) 

**Chapter 2. Contents** 

**532** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationLayout(
MDScreenManager(
MDScreen(
MDButton(
MDButtonText(
text="OpenDrawer"
),
pos_hint={"center_x":.5,"center_y":.5},
on_release=self.open_drawer,
)
)
),
MDNavigationDrawer(
MDNavigationDrawerMenu(
MDNavigationDrawerHeader(
MDLabel(
text="Headertitle",
theme_text_color="Custom",
theme_line_height="Custom",
line_height=0,
text_color="#4a4939",
adaptive_height=True,
padding_x="16dp",
font_style="Display",
role="small",
),
MDLabel(
text="Headertext",
padding_x="18dp",
adaptive_height=True,
font_style="Title",
role="large",
),
orientation="vertical",
padding=(0,0,0,"12dp"),
adaptive_height=True,
),
MDNavigationDrawerDivider(),
DrawerItem(
icon="gmail",
text="Inbox",
trailing_text="+99",
trailing_text_color="#4a4939",
),
DrawerItem(
icon="send",
text="Outbox",
),
MDNavigationDrawerDivider(),
MDNavigationDrawerLabel(
text="Labels",
padding_y="12dp",
```

(continues on next page) 

**2.3. Components** 

**533** 

**KivyMD, Release 2.0.1.dev0** 



<!-- Start of picture text -->
(continued from previous page)<br>),<br>DrawerLabel(<br>icon="information-outline",<br>text="Label",<br>),<br>DrawerLabel(<br>icon="information-outline",<br>text="Label",<br>),<br>),<br>id="nav_drawer",<br>radius=(0, dp(16), dp(16), 0),<br>)<br>),<br>md_bg_color=self.theme_cls.backgroundColor<br>)<br>)<br>Example().run()<br><!-- End of picture text -->

**API -** `kivymd.uix.navigationdrawer.navigationdrawer` 

- `class kivymd.uix.navigationdrawer.navigationdrawer.BaseNavigationDrawerItem` 

   - Implement the base class for the menu list item. 

   - Added in version 2.0.0. 

```
selected
```

Is the item selected. 

_`selected`_ is a `BooleanProperty` and defaults to _False_ . 

- `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationLayout(` _*args_ , _**kwargs_ `)` For more information, see in the _`DeclarativeBehavior`_ and `FloatLayout` classes documentation. 

   - `update_pos(` _instance_navigation_drawer_ , _pos_x: float_ `)` _→_ None 

`add_scrim(` _instance_manager: kivy.uix.screenmanager.ScreenManager_ `)` _→_ None 

`update_scrim_rectangle(` _instance_manager: kivy.uix.screenmanager.ScreenManager_ , _size: list_ `)` _→_ None 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Only two layouts are allowed: `ScreenManager` and _`MDNavigationDrawer`_ . 

- `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerLabel(` _*args_ , _**kwargs_ `)` Implements a label class. 

For more information, see in the _`MDLabel`_ class documentation. 

Added in version 1.0.0. 

- `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerDivider(` _**kwargs_ `)` Implements a divider class. 

   - For more information, see in the `BoxLayout` class documentation. 

**Chapter 2. Contents** 

**534** 

**KivyMD, Release 2.0.1.dev0** 

Added in version 1.0.0. 

`class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerHeader(` _*args_ , 

_**kwargs_ `)` 

Implements a header class. 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

Added in version 1.0.0. 

- `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItem(` _*args_ , _**kwargs_ `)` 

Implements an item for the _`MDNavigationDrawer`_ menu list. 

For more information, see in the _`MDListItem`_ and _`StateFocusBehavior`_ and _`BaseNavigationDrawerItem`_ classes documentation. 

Added in version 1.0.0. 

###### `active_indicator_color` 

The active indicator color in (r, g, b, a) or string format. 

Added in version 2.0.0. 

_`active_indicator_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `inactive_indicator_color` 

The inactive indicator color in (r, g, b, a) or string format. 

Added in version 2.0.0. 

_`inactive_indicator_color`_ is a `ColorProperty` and defaults to _None_ . 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
```

```
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

**2.3. Components** 

**535** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_release(` _*args_ `)` _→_ None 

Fired when the item is released (i.e. the touch/click that pressed the item goes away). 

###### `on_selected(` _instance_ , _value_ `)` 

Fired when the `selected` value changes 

###### `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItemLeadingIcon(` _*args_ , 

_**kwargs_ `)` 

Implements the leading icon for the menu list item. 

For more information, see in the _`MDListItemLeadingIcon`_ and _`BaseNavigationDrawerItem`_ classes documentation. 

Added in version 2.0.0. 

###### `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItemText(` _*args_ , 

_**kwargs_ `)` 

Implements the text for the menu list item. 

For more information, see in the _`MDListItemSupportingText`_ and _`BaseNavigationDrawerItem`_ classes documentation. 

Added in version 2.0.0. 

###### `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItemTrailingText(` _*args_ , 

_**kwargs_ `)` 

Implements the supporting text for the menu list item. 

For more information, see in the _`MDListItemTrailingSupportingText`_ and _`BaseNavigationDrawerItem`_ classes documentation. 

Added in version 2.0.0. 

- `class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerMenu(` _*args_ , _**kwargs_ `)` 

Implements a scrollable list for menu items of the _`MDNavigationDrawer`_ class. 

For more information, see in the _`MDScrollView`_ class documentation. 

Added in version 1.0.0. 

```
MDNavigationDrawer:
```

```
MDNavigationDrawerMenu:
```

```
#Yourmenuitems.
...
```

###### `spacing` 

Spacing between children, in pixels. 

_`spacing`_ is a `NumericProperty` and defaults to _0_ . 

- `add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

**Chapter 2. Contents** 

**536** 

**KivyMD, Release 2.0.1.dev0** 

**_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`update_items_color(` _item:_ MDNavigationDrawerItem `)` _→_ None 

`class kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer(` _*args_ , _**kwargs_ `)` Navigation drawer class. 

For more information, see in the _`MDCard`_ class documentation. 

###### **Events** 

Added in version 2.0.0. 

**_on_open_ :** Fired when the navigation drawer is opened. 

**_on_close_ :** 

Fired when the navigation drawer is closed. 

###### `drawer_type` 

Type of drawer. Modal type will be on top of screen. Standard type will be at left or right of screen. Also it automatically disables _`close_on_click`_ and _`enable_swiping`_ to prevent closing drawer for standard type. 

Changed in version 2.0.0: Rename from _type_ to _drawer_type_ . 

_`drawer_type`_ is a `OptionProperty` and defaults to _‘modal’_ . 

###### `anchor` 

Anchoring screen edge for drawer. Set it to _‘right’_ for right-to-left languages. Available options are: _‘left’_ , _‘right’_ . 

_`anchor`_ is a `OptionProperty` and defaults to _‘left’_ . 

###### `scrim_color` 

Color for scrim in (r, g, b, a) or string format. Alpha channel will be multiplied with `_scrim_alpha` . Set fourth channel to 0 if you want to disable scrim. 

_`scrim_color`_ is a `ColorProperty` and defaults to _[0, 0, 0, 0.5]_ . 

**2.3. Components** 

**537** 



<!-- Start of picture text -->
Mail<br>2 siInbox 24<br>Close Drawer<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### `open_progress` 

Percent of visible part of side panel. The percent is specified as a floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if panel is opened. 

_`open_progress`_ is a `NumericProperty` and defaults to _0.0_ . 

###### `enable_swiping` 

Allow to open or close navigation drawer with swipe. It automatically sets to False for “standard” type. 

_`enable_swiping`_ is a `BooleanProperty` and defaults to _True_ . 

###### `swipe_distance` 

The distance of the swipe with which the movement of navigation drawer begins. 

_`swipe_distance`_ is a `NumericProperty` and defaults to _10_ . 

###### `swipe_edge_width` 

The size of the area in px inside which should start swipe to drag navigation drawer. 

_`swipe_edge_width`_ is a `NumericProperty` and defaults to _20_ . 

###### `scrim_alpha_transition` 

The name of the animation transition type to use for changing `scrim_alpha` . 

_`scrim_alpha_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `opening_transition` 

The name of the animation transition type to use when animating to the _`state` ‘open’_ . 

_`opening_transition`_ is a `StringProperty` and defaults to _‘out_cubic’_ . 

###### `opening_time` 

The time taken for the panel to slide to the _`state` ‘open’_ . 

_`opening_time`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `closing_transition` 

The name of the animation transition type to use when animating to the _`state`_ ‘close’. 

_`closing_transition`_ is a `StringProperty` and defaults to _‘out_sine’_ . 

###### `closing_time` 

The time taken for the panel to slide to the _`state` ‘close’_ . 

_`closing_time`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `background_color` 

The drawer background color in (r, g, b, a) or string format. 

Added in version 2.0.0. 

_`background_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `theme_elevation_level = 'Custom'` 

Drawer elevation level scheme name. 

Added in version 2.0.0. 

Available options are: _‘Primary’_ , _‘Custom’_ . 

_`theme_elevation_level`_ is an `OptionProperty` and defaults to _‘Custom’_ . 

**2.3. Components** 

**539** 

**KivyMD, Release 2.0.1.dev0** 

###### `elevation_level = 1` 

Drawer elevation level (values from 0 to 5) 

Added in version 2.2.0. 

_`elevation_level`_ is an `BoundedNumericProperty` and defaults to _2_ . 

###### `set_properties_widget()` _→_ None 

Fired _on_release/on_press/on_enter/on_leave_ events. 

`set_state(` _new_state='toggle'_ , _animation=True_ `)` _→_ None 

Change state of the side panel. New_state can be one of _“toggle”_ , _“open”_ or _“close”_ . 

`update_status(` _*args_ `)` _→_ None 

`get_dist_from_side(` _x: float_ `)` _→_ float 

###### `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

###### `on_touch_move(` _touch_ `)` 

Receive a touch move event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

###### `on_touch_up(` _touch_ `)` 

Receive a touch up event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

`on_radius(` _instance_navigation_drawer_ , _radius_value: list_ `)` _→_ None 

Fired when the `radius` value changes. 

`on_drawer_type(` _instance_navigation_drawer_ , _drawer_type: str_ `)` _→_ None 

Fired when the _`drawer_type`_ value changes. 

###### `on_open(` _*args_ `)` _→_ None 

Fired when the navigation drawer is opened. 

- `on_close(` _*args_ `)` _→_ None 

Fired when the navigation drawer is closed. 

**Chapter 2. Contents** 

**540** 



<!-- Start of picture text -->
9:30 e@ 45<br>e<br>Sliders let users make selections from a range of values Media—___w volume<br>Call volume<br>—|<br>aRing volume<br>———-e<br>-~ Alarm volume<br><!-- End of picture text -->









###### MDSliderValueLabel 

###### MDSliderHandle 

**KivyMD, Release 2.0.1.dev0** 

_`track_inactive_width`_ is an `NumericProperty` and defaults to _dp(4)_ . 

###### `step_point_size` 

Step point size. 

Added in version 2.0.0. 

_`step_point_size`_ is an `NumericProperty` and defaults to _dp(1)_ . 

###### `track_active_color` 

Color of the active track. 

Added in version 2.0.0. 

Changed in version 2.0.0: Rename from _track_color_active_ to _track_active_color_ 

_`track_active_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `track_active_step_point_color` 

Color of step points on active track. 

Added in version 2.0.0. 

_`track_active_step_point_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `track_inactive_step_point_color` 

Color of step points on inactive track. 

Added in version 2.0.0. 

_`track_inactive_step_point_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `track_inactive_color` 

Color of the inactive track. 

Added in version 2.0.0. 

Changed in version 2.0.0: Rename from _track_color_inactive_ to _track_inactive_color_ 

_`track_active_color`_ is an `ColorProperty` and defaults to _None_ . 

###### `value_container_show_anim_duration` 

Duration of the animation opening of the label value. 

Added in version 2.0.0. 

_`value_container_show_anim_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `value_container_hide_anim_duration` 

Duration of closing the animation of the label value. 

Added in version 2.0.0. 

_`value_container_hide_anim_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `value_container_show_anim_transition` 

The type of the opening animation of the label value. 

Added in version 2.0.0. 

_`value_container_show_anim_transition`_ is an `StringProperty` and defaults to _‘out_circ’_ . 

**2.3. Components** 

**543** 

**KivyMD, Release 2.0.1.dev0** 

###### `value_container_hide_anim_transition` 

The type of the closing animation of the label value. 

Added in version 2.0.0. 

_`value_container_hide_anim_transition`_ is an `StringProperty` and defaults to _‘out_circ’_ . 

###### `handle_anim_transition` 

Handle animation type. 

Added in version 2.0.0. 

_`handle_anim_transition`_ is an `StringProperty` and defaults to _‘out_circ’_ . 

###### `handle_anim_duration` 

Handle animation duration. 

Added in version 2.0.0. 

_`handle_anim_duration`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`update_points(` _instance_ , _step_ `)` _→_ None 

Draws the step points on the slider. 

`on_size(` _*args_ `)` _→_ None 

Fired when the widget is resized. 

`on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

**Chapter 2. Contents** 

**544** 

**KivyMD, Release 2.0.1.dev0** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

- `on_value_pos(` _*args_ `)` _→_ None 

Fired when the _value_pos_ value changes. Sets a new value for the value label texture. 

- `on_touch_up(` _touch_ `)` 

Receive a touch up event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

- `on_touch_move(` _touch_ `)` 

Receive a touch move event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

- `on_handle_enter()` _→_ None 

Scales the container of the label value. 

- `on_handle_leave()` _→_ None 

Scales the container of the label value. 

- `class kivymd.uix.slider.slider.MDSliderHandle(` _**kwargs_ `)` 

Handle class. 

Added in version 2.0.0. 

For more information, see in the _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and _`StateFocusBehavior`_ and `Widget` classes documentation. 

###### `radius` 

Handle radius. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(10), dp(10), dp(10), dp(10)]_ . 

```
size
```

Handle size. 

_`size`_ is an `ListProperty` and defaults to _[dp(20), dp(20)]_ . 

###### `state_layer_size` 

Handle state layer size. 

_`state_layer_size`_ is an `ListProperty` and defaults to _[dp(40), dp(40)]_ . 

###### `state_layer_color` 

Handle state layer color. 

_`state_layer_color`_ is an `ColorProperty` and defaults to _None_ . 

- `on_enter()` _→_ None 

Fired when mouse enter the bbox of the widget. Animates the display of the slider handle layer. 

###### `on_leave()` _→_ None 

Fired when the mouse goes outside the widget border. Animates the hiding of the slider handle layer. 

**2.3. Components** 

**545** 

**KivyMD, Release 2.0.1.dev0** 

`class kivymd.uix.slider.slider.MDSliderValueLabel(` _*args_ , _**kwargs_ `)` 

Implements the value label. 

For more information, see in the _`MDLabel`_ class documentation. 

Added in version 2.0.0. 

```
size
```

Container size for the label value. 

`handle_anim_transition` is an `ListProperty` and defaults to _[dp(36), dp(36)]_ . 

###### **2.3.51 ExpansionPanel** 

**Expansion panels contain creation flows and allow lightweight editing of an element.** 



###### **Usage** 

```
MDExpansionPanel:
MDExpansionPanelHeader:
#Contentofheader.
[...]
MDExpansionPanelContent:
#Contentofpanel.
[...]
```

**Chapter 2. Contents** 

**546** 



<!-- Start of picture text -->
Supporting text v<br>Channel information<br>Email<br>kivydevelopment@gmail.com<br>Instagram<br>www instagram.com/KivyMD<br>MDExpansionPanel!Content MDExpansionPanelHeader<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text:"Channelinformation"
adaptive_height:True
padding_x:"16dp"
padding_y:"12dp"
MDListItem:
MDListItemLeadingIcon:
icon:"email"
MDListItemHeadlineText:
text:"Email"
MDListItemSupportingText:
text:"kivydevelopment@gmail.com"
MDListItem:
MDListItemLeadingIcon:
icon:"instagram"
MDListItemHeadlineText:
text:"Instagram"
MDListItemSupportingText:
text:"Account"
MDListItemTertiaryText:
text:"www.instagram.com/KivyMD"
'''
classTrailingPressedIconButton(
ButtonBehavior,RotateBehavior,MDListItemTrailingIcon
):
...
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
deftap_expansion_chevron(
self,panel:MDExpansionPanel,chevron:TrailingPressedIconButton
):
panel.open()ifnotpanel.is_openelsepanel.close()
panel.set_chevron_down(
chevron
)ifnotpanel.is_openelsepanel.set_chevron_up(chevron)
```

(continues on next page) 

**Chapter 2. Contents** 

**548** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

###### **Use with ScrollView** 

```
importasynckivy
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportRotateBehavior
fromkivymd.uix.expansionpanelimportMDExpansionPanel
fromkivymd.uix.listimportMDListItemTrailingIcon
KV='''
<ExpansionPanelItem>
MDExpansionPanelHeader:
MDListItem:
theme_bg_color:"Custom"
md_bg_color:self.theme_cls.surfaceContainerLowColor
ripple_effect:False
MDListItemSupportingText:
text:"Supportingtext"
TrailingPressedIconButton:
id:chevron
icon:"chevron-right"
on_release:app.tap_expansion_chevron(root,chevron)
MDExpansionPanelContent:
orientation:"vertical"
padding:"12dp",0,"12dp","12dp"
md_bg_color:self.theme_cls.surfaceContainerLowestColor
MDLabel:
text:"Channelinformation"
adaptive_height:True
padding_x:"16dp"
padding_y:"12dp"
MDListItem:
theme_bg_color:"Custom"
md_bg_color:self.theme_cls.surfaceContainerLowestColor
MDListItemLeadingIcon:
```

(continues on next page) 

**2.3. Components** 

**549** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon:"email"
MDListItemHeadlineText:
text:"Email"
MDListItemSupportingText:
text:"kivydevelopment@gmail.com"
MDListItem:
theme_bg_color:"Custom"
md_bg_color:self.theme_cls.surfaceContainerLowestColor
MDListItemLeadingIcon:
icon:"instagram"
MDListItemHeadlineText:
text:"Instagram"
MDListItemSupportingText:
text:"Account"
MDListItemTertiaryText:
text:"www.instagram.com/KivyMD"
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
ScrollView:
size_hint_x:.5
pos_hint:{"center_x":.5,"center_y":.5}
MDList:
id:container
'''
classExpansionPanelItem(MDExpansionPanel):
...
classTrailingPressedIconButton(
ButtonBehavior,RotateBehavior,MDListItemTrailingIcon
):
...
classExample(MDApp):
defon_start(self):
asyncdefset_panel_list():
foriinrange(12):
awaitasynckivy.sleep(0)
```

(continues on next page) 

**Chapter 2. Contents** 

**550** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.root.ids.container.add_widget(ExpansionPanelItem())
asynckivy.start(set_panel_list())
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
deftap_expansion_chevron(
self,panel:MDExpansionPanel,chevron:TrailingPressedIconButton
):
Animation(
padding=[0,dp(12),0,dp(12)]
ifnotpanel.is_open
else[0,0,0,0],
d=0.2,
).start(panel)
panel.open()ifnotpanel.is_openelsepanel.close()
panel.set_chevron_down(
chevron
)ifnotpanel.is_openelsepanel.set_chevron_up(chevron)
```

```
Example().run()
```

###### **API break** 

###### **1.2.0 version** 

```
MDExpansionPanel(
icon="icon.png",
content=Content(),#contentofpanel
panel_cls=MDExpansionPanelThreeLine(#contentofheader
text="Text",
secondary_text="Secondarytext",
tertiary_text="Tertiarytext",
)
)
```

**2.3. Components** 

**551** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
MDExpansionPanel:
```

```
MDExpansionPanelHeader:
#Contentofheader.
[...]
MDExpansionPanelContent:
#Contentofpanel.
[...]
```

###### **API -** `kivymd.uix.expansionpanel.expansionpanel` 

- `class kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanelContent(` _*args_ , _**kwargs_ `)` Implements a container for panel content. 

Added in version 2.0.0. 

For more information, see in the _`DeclarativeBehavior`_ and _`ThemableBehavior`_ and _`BackgroundColorBehavior`_ and `BoxLayout` classes documentation. 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

**_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

`class kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanelHeader(` _*args_ , _**kwargs_ `)` 

Implements a container for the content of the panel header. 

Added in version 2.0.0. 

**Chapter 2. Contents** 

**552** 

**KivyMD, Release 2.0.1.dev0** 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

`class kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel(` _*args_ , _**kwargs_ `)` Expansion panel class. 

For more information, see in the _`DeclarativeBehavior`_ and `BoxLayout` classes documentation. 

###### **Events** 

_`on_open`_ Fired when a panel is opened. 

_`on_close`_ Fired when a panel is closed. 

###### `opening_transition` 

The name of the animation transition type to use when animating to the `state` _‘open’_ . 

_`opening_transition`_ is a `StringProperty` and defaults to _‘out_cubic’_ . 

###### `opening_time` 

The time taken for the panel to slide to the `state` _‘open’_ . 

_`opening_time`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `closing_transition` 

The name of the animation transition type to use when animating to the `state` ‘close’. 

_`closing_transition`_ is a `StringProperty` and defaults to _‘out_sine’_ . 

###### `closing_time` 

The time taken for the panel to slide to the `state` _‘close’_ . 

_`closing_time`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `is_open` 

The panel is open or closed. 

Added in version 2.0.0. 

_`is_open`_ is a `BooleanProperty` and defaults to _False_ . 

`on_open(` _*args_ `)` _→_ None 

Fired when a panel is opened. 

- `on_close(` _*args_ `)` _→_ None 

Fired when a panel is closed. 

- `set_chevron_down(` _instance_ `)` _→_ None 

Sets the chevron down. 

- `set_chevron_up(` _instance_ `)` _→_ None 

Sets the chevron up. 

`close(` _*args_ `)` _→_ None 

Method closes the panel. 

Changed in version 2.0.0: Rename from _close_panel_ to _close_ method. 

`open(` _*args_ `)` _→_ None 

Method opens a panel. 

Changed in version 2.0.0: Rename from _open_panel_ to _open_ method. 

**2.3. Components** 

**553** 

**KivyMD, Release 2.0.1.dev0** 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### **2.3.52 FitImage** 

###### **Example** 

Imperative Python Styles 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
radius:"36dp"
pos_hint:{"center_x":.5,"center_y":.5}
size_hint:.4,.8
md_bg_color:self.theme_cls.onSurfaceVariantColor
FitImage:
source:"image.png"
size_hint_y:.35
pos_hint:{"top":1}
```

(continues on next page) 

**Chapter 2. Contents** 

**554** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
radius:"36dp","36dp",0,0
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python Styles 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.cardimportMDCard
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
return(
MDScreen(
MDBoxLayout(
FitImage(
source="image.png",
size_hint_y=0.35,
pos_hint={"top":1},
radius=(dp(36),dp(36),0,0),
),
radius=dp(36),
md_bg_color=self.theme_cls.onSurfaceVariantColor,
pos_hint={"center_x":0.5,"center_y":0.5},
size_hint=(0.4,0.8),
),
)
)
Example().run()
```

**2.3. Components** 

**555** 



<!-- Start of picture text -->
eS<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

Available shape options are: _‘circle’_ , _‘square’_ , _‘slanted’_ , _‘arch’_ , _‘semiCircle’_ , _‘oval’_ , _‘pill’_ , _‘triangle’_ , _‘arrow’_ , _‘fan’_ , _‘diamond’_ , _‘clamShell’_ , _‘pentagon’_ , _‘gem’_ , _‘sunny’_ , _‘verySunny’_ , _‘cookie4Sided’_ , _‘cookie6Sided’_ , _‘cookie7Sided’_ , _‘cookie9Sided’_ , _‘cookie12Sided’_ , _‘clover4Leaf’_ , _‘clover8Leaf’_ , _‘burst’_ , _‘softBurst’_ , _‘boom’_ , _‘softBoom’_ , _‘flower’_ , _‘puffy’_ , _‘puffyDiamond’_ , _‘ghostish’_ , _‘pixelCircle’_ , _‘pixelTriangle’_ , _‘bun’_ , _‘heart’_ . 

If set to `None` , the image will be rendered as a standard rectangle. 

_`shape`_ is an `OptionProperty` and defaults to _None_ . 

Imperative Python Styles 

```
fromkivy.langimportBuilder
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.labelimportMDLabel
KV='''
MDScreen:
md_bg_color:app.theme_cls.surfaceColor
MDScrollView:
MDGridLayout:
id:shape_grid
cols:6
adaptive_height:True
padding:dp(16)
spacing:dp(16)
'''
```

```
classExampleApp(MDApp):
SHAPES=[
"circle",
"square",
"slanted",
"arch",
"semiCircle",
"oval",
"pill",
"triangle",
"arrow",
"fan",
"diamond",
"clamShell",
"pentagon",
"gem",
"sunny",
"verySunny",
"cookie4Sided",
"cookie6Sided",
```

(continues on next page) 

**2.3. Components** 

**557** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
"cookie7Sided",
"cookie9Sided",
"cookie12Sided",
"clover4Leaf",
"clover8Leaf",
"burst",
"softBurst",
"boom",
"softBoom",
"flower",
"puffy",
"puffyDiamond",
"ghostish",
"pixelCircle",
"pixelTriangle",
"bun",
"heart",
```

```
]
IMAGE_PATH="bg.jpg"
```

```
defbuild(self):
returnBuilder.load_string(KV)
```

```
defon_start(self):
grid=self.root.ids.shape_grid
```

```
forshape_nameinself.SHAPES:
item_box=MDBoxLayout(
orientation="vertical",
adaptive_height=True,
spacing=dp(8),
```

```
)
```

```
shape_widget=FitImage(
size_hint=(None,None),
size=(dp(90),dp(90)),
pos_hint={"center_x":0.5},
shape=shape_name,
source=self.IMAGE_PATH,
```

```
)
```

```
label=MDLabel(
text=shape_name,
halign="center",
adaptive_height=True,
font_style="Label",
role="medium",
```

```
)
```

```
item_box.add_widget(shape_widget)
item_box.add_widget(label)
grid.add_widget(item_box)
```

(continues on next page) 

**Chapter 2. Contents** 

**558** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
if__name__=="__main__":
ExampleApp().run()
```

Declarative Python Styles 

```
fromkivy.metricsimportdp
```

```
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.fitimageimportFitImage
fromkivymd.uix.gridlayoutimportMDGridLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.scrollviewimportMDScrollView
fromkivymd.uix.screenimportMDScreen
```

```
classExampleApp(MDApp):
SHAPES=[
"circle",
"square",
"slanted",
"arch",
"semiCircle",
"oval",
"pill",
"triangle",
"arrow",
"fan",
"diamond",
"clamShell",
"pentagon",
"gem",
"sunny",
"verySunny",
"cookie4Sided",
"cookie6Sided",
"cookie7Sided",
"cookie9Sided",
"cookie12Sided",
"clover4Leaf",
"clover8Leaf",
"burst",
"softBurst",
"boom",
"softBoom",
"flower",
"puffy",
"puffyDiamond",
"ghostish",
"pixelCircle",
```

(continues on next page) 

**2.3. Components** 

**559** 

**KivyMD, Release 2.0.1.dev0** 



<!-- Start of picture text -->
(continued from previous page)<br>"pixelTriangle",<br>"bun",<br>"heart",<br>]<br>IMAGE_PATH = "bg.jpg"<br>def build(self):<br>return MDScreen(<br>MDScrollView(<br>MDGridLayout(<br>*[<br>MDBoxLayout(<br>FitImage(<br>size_hint=(None, None),<br>size=(dp(90), dp(90)),<br>pos_hint={"center_x": 0.5},<br>shape=shape_name,<br>source=self.IMAGE_PATH,<br>),<br>MDLabel(<br>text=shape_name,<br>halign="center",<br>adaptive_height=True,<br>font_style="Label",<br>role="medium",<br>),<br>orientation="vertical",<br>adaptive_height=True,<br>spacing=dp(8),<br>)<br>for shape_name in self.SHAPES<br>],<br>cols=6,<br>adaptive_height=True,<br>padding=dp(16),<br>spacing=dp(16),<br>)<br>),<br>md_bg_color=self.theme_cls.surfaceColor,<br>)<br>if __name__ == "__main__":<br>ExampleApp().run()<br><!-- End of picture text -->

**Chapter 2. Contents** 

**560** 



<!-- Start of picture text -->
38 }<br>. Z3 @&<br>circle square slanted arch semiCircle oval<br>pill triangle arrow fan diamond clamShell<br>pentagon gem sunny verySunny cookie4Sided cookie6Sided<br>» &<br>y a9 ;<br>7<br>cookie7Sided cookie9Sided cookie12Sided clover4Leaf clover8Leaf burst<br>softBurst boom softBoom flower puffy puffyDiamond<br>7®<br>ghostish pixelCircle pixelTriangle bun heart<br><!-- End of picture text -->



<!-- Start of picture text -->
VA<br>€ 6 :<br>a ra S Saved podcasts<br>Cards contain content and actions about a single subject FA iz a od<br>= ‘ff ><br>= 4 =<br>wt Ads!<br><!-- End of picture text -->



<!-- Start of picture text -->
Elevated Filled Outlined<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative KV and imperative python styles 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.cardimportMDCard
KV='''
<MyCard>
padding:"4dp"
size_hint:None,None
size:"240dp","100dp"
MDRelativeLayout:
MDIconButton:
icon:"dots-vertical"
pos_hint:{"top":1,"right":1}
MDLabel:
text:root.text
adaptive_size:True
color:"grey"
pos:"12dp","12dp"
bold:True
MDScreen:
theme_bg_color:"Custom"
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
id:box
adaptive_size:True
spacing:"12dp"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classMyCard(MDCard):
'''Implementsamaterialcard.'''
text=StringProperty()
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defon_start(self):
```

(continues on next page) 

**2.3. Components** 

**563** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
forstylein("elevated","filled","outlined"):
self.root.ids.box.add_widget(
MyCard(style=style,text=style.capitalize())
)
Example().run()
```

Declarative python styles 

```
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.cardimportMDCard
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.relativelayoutimportMDRelativeLayout
fromkivymd.uix.screenimportMDScreen
classMyCard(MDCard):
'''Implementsamaterialcard.'''
classExample(MDApp):
defbuild(self):
return(
MDScreen(
MDBoxLayout(
id="box",
adaptive_size=True,
spacing="12dp",
pos_hint={"center_x":0.5,"center_y":0.5},
),
theme_bg_color="Custom",
md_bg_color=self.theme_cls.backgroundColor,
)
)
defon_start(self):
forstylein("elevated","filled","outlined"):
self.root..get_ids().box.add_widget(
MyCard(
MDRelativeLayout(
MDIconButton(
icon="dots-vertical",
pos_hint={"top":1,"right":1}
),
MDLabel(
text=style.capitalize(),
adaptive_size=True,
pos=("12dp","12dp"),
),
```

(continues on next page) 

**Chapter 2. Contents** 

**564** 







<!-- Start of picture text -->
Elevated<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Filled** 

```
MDCard
style:"filled"
```



###### **Outlined** 

```
MDCard
style:"outlined"
```



**Chapter 2. Contents** 

**566** 

**KivyMD, Release 2.0.1.dev0** 

###### **Customization of card** 

Imperative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDCard:
style:"elevated"
pos_hint:{"center_x":.5,"center_y":.5}
padding:"4dp"
size_hint:None,None
size:"240dp","100dp"
#Setscustomproperties.
theme_shadow_color:"Custom"
shadow_color:"green"
theme_bg_color:"Custom"
md_bg_color:"white"
md_bg_color_disabled:"grey"
theme_shadow_offset:"Custom"
shadow_offset:(1,-2)
theme_shadow_softness:"Custom"
shadow_softness:1
theme_elevation_level:"Custom"
elevation_level:2
RelativeLayout:
MDIconButton:
icon:"dots-vertical"
pos_hint:{"top":1,"right":1}
MDLabel:
text:"Elevated"
adaptive_size:True
color:"grey"
pos:"12dp","12dp"
bold:True
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
returnBuilder.load_string(KV)
Example().run()
```

**2.3. Components** 

**567** 

**KivyMD, Release 2.0.1.dev0** 

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.cardimportMDCard
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.relativelayoutimportMDRelativeLayout
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
return(
MDScreen(
MDCard(
MDRelativeLayout(
MDIconButton(
icon="dots-vertical",
pos_hint={"top":1,"right":1},
),
MDLabel(
text="Elevated",
adaptive_size=True,
color="grey",
pos=("12dp","12dp"),
bold=True,
),
),
style="elevated",
pos_hint={"center_x":.5,"center_y":.5},
padding="4dp",
size_hint=(None,None),
size=("240dp","100dp"),
#Setscustomproperties.
theme_shadow_color="Custom",
shadow_color="green",
theme_bg_color="Custom",
md_bg_color="white",
md_bg_color_disabled="grey",
theme_shadow_offset="Custom",
shadow_offset=(1,-2),
theme_shadow_softness="Custom",
shadow_softness=1,
theme_elevation_level="Custom",
elevation_level=2,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**568** 



<!-- Start of picture text -->
Elevated<br><!-- End of picture text -->





**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative KV and imperative python styles 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.cardimportMDCardSwipe
KV='''
<SwipeToDeleteItem>:
size_hint_y:None
height:content.height
MDCardSwipeLayerBox:
padding:"8dp"
MDIconButton:
icon:"trash-can"
pos_hint:{"center_y":.5}
on_release:app.remove_item(root)
MDCardSwipeFrontBox:
MDListItem:
id:content
ripple_effect:False
MDListItemSupportingText
text:root.text
MDScreen:
MDScrollView:
MDList:
id:md_list
padding:0
'''
classSwipeToDeleteItem(MDCardSwipe):
text=StringProperty()
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
self.screen=Builder.load_string(KV)
```

(continues on next page) 

**Chapter 2. Contents** 

**570** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defbuild(self):
returnself.screen
defremove_item(self,instance):
self.screen.ids.md_list.remove_widget(instance)
defon_start(self):
foriinrange(20):
self.screen.ids.md_list.add_widget(
SwipeToDeleteItem(text=f"One-lineitem{i}")
)
Example().run()
```

Declarative python styles 

```
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.cardimport(
MDCardSwipe,MDCardSwipeLayerBox,MDCardSwipeFrontBox
)
fromkivymd.uix.listimportMDList,MDListItem,MDListItemSupportingText
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.scrollviewimportMDScrollView
classSwipeToDeleteItem(MDCardSwipe):
text=StringProperty()
classExample(MDApp):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
defbuild(self):
return(
MDScreen(
MDScrollView(
MDList(
id="md_list",
padding=10,
)
)
)
)
```

(continues on next page) 

**2.3. Components** 

**571** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
defremove_item(self,instance):
self.root.get_ids().md_list.remove_widget(instance)
defon_start(self):
foriinrange(20):
swipe_to_delete_item=SwipeToDeleteItem(
MDCardSwipeLayerBox(
MDIconButton(
id="trash_can",
icon="trash-can",
pos_hint={"center_y":0.5},
),
),
MDCardSwipeFrontBox(
MDListItem(
MDListItemSupportingText(
text=f"One-lineitem{i}",
),
id="content",
ripple_effect=False,
),
),
size_hint_y=None,
)
trash_can=swipe_to_delete_item.get_ids().trash_can
trash_can.bind(
on_release=lambdax,y=swipe_to_delete_item:self.remove_item(y)
)
self.root.get_ids().md_list.add_widget(swipe_to_delete_item)
swipe_to_delete_item.height=swipe_to_delete_item.get_ids().content.height
Example().run()
```

###### **Binding a swipe to one of the sides of the screen** 

```
<SwipeToDeleteItem>
#Bydefault,theparameteris"left"
anchor:"right"
```

**Note:** You cannot use the left and right swipe at the same time. 

**Chapter 2. Contents** 

**572** 

**KivyMD, Release 2.0.1.dev0** 

###### **Swipe behavior** 

```
<SwipeToDeleteItem>
#Bydefault,theparameteris"hand"
type_swipe:"hand"#"auto"
```

**Removing an item using the** `type_swipe = "auto"` **parameter** 

The map provides the _`MDCardSwipe.on_swipe_complete`_ event. You can use this event to remove items from a list: Declarative KV styles 

```
<SwipeToDeleteItem>:
on_swipe_complete:app.on_swipe_complete(root)
```

Declarative python styles 

```
..code-block::python
MDCardSwipe(
...
on_swipe_complete=self.on_swipe_complete,
)
```

Imperative python styles 

```
defon_swipe_complete(self,instance):
self.root.ids.md_list.remove_widget(instance)
```

Decralative python styles 

```
defon_swipe_complete(self,instance):
self.root.get_ids().md_list.remove_widget(instance)
```

###### **Add content to the bottom layer of the card** 

To add content to the bottom layer of the card, use the _`MDCardSwipeLayerBox`_ class. 

```
<SwipeToDeleteItem>:
MDCardSwipeLayerBox:
padding:"8dp"
MDIconButton:
icon:"trash-can"
pos_hint:{"center_y":.5}
on_release:app.remove_item(root)
```

**2.3. Components** 

**573** 

0 OneJine item 0 

**KivyMD, Release 2.0.1.dev0** 

###### `open_progress` 

Percent of visible part of side panel. The percent is specified as a floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if panel is opened. 

_`open_progress`_ is a `NumericProperty` and defaults to _0.0_ . 

###### `opening_transition` 

The name of the animation transition type to use when animating to the _`state` ‘opened’_ . 

_`opening_transition`_ is a `StringProperty` and defaults to _‘out_cubic’_ . 

###### `closing_transition` 

The name of the animation transition type to use when animating to the _`state`_ ‘closed’. 

_`closing_transition`_ is a `StringProperty` and defaults to _‘out_sine’_ . 

###### `closing_interval` 

Interval for closing the front layer. 

Added in version 1.1.0. 

_`closing_interval`_ is a `NumericProperty` and defaults to _0_ . 

###### `anchor` 

Anchoring screen edge for card. Available options are: _‘left’_ , _‘right’_ . 

_`anchor`_ is a `OptionProperty` and defaults to _left_ . 

###### `swipe_distance` 

The distance of the swipe with which the movement of navigation drawer begins. 

_`swipe_distance`_ is a `NumericProperty` and defaults to _50_ . 

###### `opening_time` 

The time taken for the card to slide to the _`state` ‘open’_ . 

_`opening_time`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `state` 

Detailed state. Sets before _`state`_ . Bind to _`state`_ instead of `status` . Available options are: _‘closed’_ , _‘opened’_ . 

`status` is a `OptionProperty` and defaults to _‘closed’_ . 

###### `max_swipe_x` 

If, after the events of _`on_touch_up`_ card position exceeds this value - will automatically execute the method _`open_card`_ , and if not - will automatically be _`close_card`_ method. 

_`max_swipe_x`_ is a `NumericProperty` and defaults to _0.3_ . 

###### `max_opened_x` 

The value of the position the card shifts to when _`type_swipe`_ s set to _‘hand’_ . 

_`max_opened_x`_ is a `NumericProperty` and defaults to _100dp_ . 

###### `type_swipe` 

Type of card opening when swipe. Shift the card to the edge or to a set position _`max_opened_x`_ . Available options are: _‘auto’_ , _‘hand’_ . 

_`type_swipe`_ is a `OptionProperty` and defaults to _auto_ . 

**2.3. Components** 

**575** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_swipe_complete(` _*args_ `)` 

Fired when a swipe of card is completed. 

`on_anchor(` _instance_swipe_to_delete_item_ , _anchor_value: str_ `)` _→_ None 

Fired when the value of _`anchor`_ changes. 

`on_open_progress(` _instance_swipe_to_delete_item_ , _progress_value: float_ `)` _→_ None 

Fired when the value of _`open_progress`_ changes. 

###### `on_touch_move(` _touch_ `)` 

Receive a touch move event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

###### `on_touch_up(` _touch_ `)` 

Receive a touch up event. The touch is in parent coordinates. 

See _`on_touch_down()`_ for more information. 

###### `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

###### `open_card()` _→_ None 

Animates the opening of the card. 

###### `close_card(` _*args_ `)` _→_ None 

Animates the closing of the card. 

`add_widget(` _widget_ , _index=0_ , _canvas=None_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

**Chapter 2. Contents** 

**576** 





<!-- Start of picture text -->
Phone ringtone<br>D e > None<br>lalogs -<br>Dialogs provide important prompts in a user flow Lama<br><!-- End of picture text -->



<!-- Start of picture text -->
MDDialogicon<br>MDDialogHeadlineText<br>MDDialogSupportingText<br>C<br>Reset settings?<br>This will reset your app preferences backto their default settings. The following<br>accountswill also be signed out:<br>KivyMD-library@yandex.com<br>kivydevelopment@gmail.com<br>MDDialogContentContainer MDDialogButtonContainer<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDListItemLeadingIcon,
MDListItemSupportingText,
)
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDButton:
pos_hint:{'center_x':.5,'center_y':.5}
on_release:app.show_alert_dialog()
MDButtonText:
text:"Showdialog"
'''
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defshow_alert_dialog(self):
MDDialog(
#----------------------------Icon-----------------------------
MDDialogIcon(
icon="refresh",
),
#-----------------------Headlinetext-------------------------
MDDialogHeadlineText(
text="Resetsettings?",
),
#-----------------------Supportingtext-----------------------
MDDialogSupportingText(
text="Thiswillresetyourapppreferencesbacktotheir"
"defaultsettings.Thefollowingaccountswillalso"
"besignedout:",
),
#-----------------------Customcontent------------------------
MDDialogContentContainer(
MDDivider(),
MDListItem(
MDListItemLeadingIcon(
icon="gmail",
),
MDListItemSupportingText(
text="KivyMD-library@yandex.com",
),
theme_bg_color="Custom",
md_bg_color=self.theme_cls.transparentColor,
),
MDListItem(
MDListItemLeadingIcon(
```

(continues on next page) 

**2.3. Components** 

**579** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
icon="gmail",
),
MDListItemSupportingText(
text="kivydevelopment@gmail.com",
),
theme_bg_color="Custom",
md_bg_color=self.theme_cls.transparentColor,
),
MDDivider(),
orientation="vertical",
),
#---------------------Buttoncontainer------------------------
MDDialogButtonContainer(
Widget(),
MDButton(
MDButtonText(text="Cancel"),
style="text",
),
MDButton(
MDButtonText(text="Accept"),
style="text",
),
spacing="8dp",
),
#-------------------------------------------------------------
).open()
Example().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.dialogimport(
MDDialog,
MDDialogIcon,
MDDialogHeadlineText,
MDDialogSupportingText,
MDDialogContentContainer,
MDDialogButtonContainer,
)
fromkivymd.uix.dividerimportMDDivider
fromkivymd.uix.listimport(
MDListItem,MDListItemSupportingText,MDListItemLeadingIcon
)
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.widgetimportMDWidget
classExample(MDApp):
defbuild(self):
```

(continues on next page) 

**Chapter 2. Contents** 

**580** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`self.theme_cls.primary_palette = "Olive" return ( MDScreen( MDButton( MDButtonText( text="Show dialog" ), id="button", pos_hint={'center_x': .5, 'center_y': 0.5}, on_release=self.show_alert_dialog, ), md_bg_color=self.theme_cls.backgroundColor ) ) def show_alert_dialog(self, *args): MDDialog(` _`# ----------------------------Icon-----------------------------`_ `MDDialogIcon( icon="refresh", ),` _`# -----------------------Headline text-------------------------`_ `MDDialogHeadlineText( text="Reset settings?", ),` _`# -----------------------Supporting text-----------------------`_ `MDDialogSupportingText( text="This will reset your app preferences back to their " "default settings. The following accounts will also " "be signed out:", ),` _`# -----------------------Custom content------------------------`_ `MDDialogContentContainer( MDDivider(), MDListItem( MDListItemLeadingIcon( icon="gmail", ), MDListItemSupportingText( text="KivyMD-library@yandex.com", ), theme_bg_color="Custom", md_bg_color=self.theme_cls.transparentColor, ), MDListItem( MDListItemLeadingIcon( icon="gmail", ), MDListItemSupportingText( text="kivydevelopment@gmail.com", ), theme_bg_color="Custom",` (continues on next page) 

**2.3. Components** 

**581** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
md_bg_color=self.theme_cls.transparentColor,
),
MDDivider(),
orientation="vertical",
),
#---------------------Buttoncontainer------------------------
MDDialogButtonContainer(
MDWidget(),
MDButton(
MDButtonText(text="Cancel"),
style="text",
),
MDButton(
MDButtonText(text="Accept"),
style="text",
),
spacing="8dp",
),
#-------------------------------------------------------------
).open()
Example().run()
```

**Warning:** Do not try to use the MDDialog widget in KV files. 

###### **API break** 

###### **1.2.0 version** 

`from kivy.uix.widget import Widget from kivymd.app import MDApp from kivymd.uix.button import MDFlatButton from kivymd.uix.dialog import MDDialog class Example(MDApp): def build(self): return Widget() def on_start(self): MDDialog( title="Discard draft?", buttons=[ MDFlatButton( text="CANCEL",` (continues on next page) 

**Chapter 2. Contents** 

**582** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
theme_text_color="Custom",
text_color=self.theme_cls.primary_color,
),
MDFlatButton(
text="DISCARD",
theme_text_color="Custom",
text_color=self.theme_cls.primary_color,
),
],
).open()
```

```
Example().run()
```



```
fromkivy.uix.widgetimportWidget
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDFlatButton
fromkivymd.uix.dialogimportMDDialog
```

```
classExample(MDApp):
defbuild(self):
returnWidget()
defon_start(self):
MDDialog(
title="Discarddraft?",
text="Thiswillresetyourdevicetoitsdefaultfactorysettings.",
buttons=[
MDFlatButton(
```

(continues on next page) 

**2.3. Components** 

**583** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) `text="CANCEL", theme_text_color="Custom", text_color=self.theme_cls.primary_color, ), MDFlatButton( text="DISCARD", theme_text_color="Custom", text_color=self.theme_cls.primary_color, ), ], ).open() Example().run()` 



`from kivy.lang import Builder from kivy.properties import StringProperty from kivy.uix.widget import Widget from kivymd import images_path from kivymd.app import MDApp from kivymd.uix.dialog import MDDialog from kivymd.uix.list import OneLineAvatarListItem KV = ''' <Item> ImageLeftWidget: source: root.source '''` (continues on next page) 

**Chapter 2. Contents** 

**584** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

`class` <u>`Item(OneLineAvatarListItem):`</u> `divider = None source = StringProperty() class Example(MDApp): def build(self): Builder.load_string(KV) return Widget() def on_start(self): MDDialog( title="Set backup account", type="simple", items=[ Item(text="user01@gmail.com", source=f"{images_path}/logo/kivymd-icon-` _˓→_ `128.png"), Item(text="user02@gmail.com", source="data/logo/kivy-icon-128.png"), ], ).open() Example().run()` 



**2.3. Components** 

**585** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.2.0 version** 

```
fromkivy.uix.widgetimportWidget
fromkivymd.uix.widgetimportMDWidget
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.dialogimportMDDialog,MDDialogHeadlineText,MDDialogButtonContainer
classExample(MDApp):
defbuild(self):
returnMDWidget(md_bg_color=self.theme_cls.backgroundColor)
defon_start(self):
MDDialog(
MDDialogHeadlineText(
text="Discarddraft?",
halign="left",
),
MDDialogButtonContainer(
Widget(),
MDButton(
MDButtonText(text="Cancel"),
style="text",
),
MDButton(
MDButtonText(text="Discard"),
style="text",
),
spacing="8dp",
),
).open()
Example().run()
```

**Chapter 2. Contents** 

**586** 

Discard draft? 



<!-- Start of picture text -->
Cancel Discard<br><!-- End of picture text -->





###### Discard draft? 

This will reset your deviceto its default factory settings. 

Cancel Discard 





Set backup account © user01 @gmail.com g user01@gmail.com 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.dialog.dialog` 

`class kivymd.uix.dialog.dialog.MDDialog(` _*args_ , _**kwargs_ `)` 

Dialog class. 

For more information, see in the _`MDCard`_ and _`MotionDialogBehavior`_ classes documentation. 

###### **Events** 

###### **_on_pre_open_ :** 

Fired before the MDDialog is opened. When this event is fired MDDialog is not yet added to window. 

**_on_open_ :** 

Fired when the MDDialog is opened. 

###### **_on_pre_dismiss_ :** 

Fired before the MDDialog is closed. 

###### **_on_dismiss_ :** 

Fired when the MDDialog is closed. If the callback returns True, the dismiss will be canceled. 

###### `width_offset` 

Dialog offset from device width. 

_`width_offset`_ is an `NumericProperty` and defaults to _dp(48)_ . 

###### `radius` 

Dialog corners rounding value. 

_`radius`_ is an `VariableListProperty` and defaults to _[dp(28), dp(28), dp(28), dp(28)]_ . 

###### `scrim_color` 

Color for scrim in (r, g, b, a) or string format. 

_`scrim_color`_ is a `ColorProperty` and defaults to _[0, 0, 0, 0.5]_ . 

###### `auto_dismiss` 

This property determines if the dialog is automatically dismissed when the user clicks outside it. 

..versionadded:: 2.0.0 

_`auto_dismiss`_ is a `BooleanProperty` and defaults to True. 

###### `update_width(` _*args_ `)` _→_ None 

Fired when the application window is resized. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

Added in version 1.0.5. 

**Chapter 2. Contents** 

**590** 

**KivyMD, Release 2.0.1.dev0** 

###### **_canvas_ : str, defaults to None** 

Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas. 

Added in version 1.9.0. 

```
>>>fromkivy.uix.buttonimportButton
>>>fromkivy.uix.sliderimportSlider
>>>root=Widget()
>>>root.add_widget(Button())
>>>slider=Slider()
>>>root.add_widget(slider)
```

###### `set_properties_widget()` _→_ None 

Fired _on_release/on_press/on_enter/on_leave_ events. 

`open()` _→_ None 

Show the dialog. 

- `on_pre_open(` _*args_ `)` _→_ None 

Fired when a dialog pre opened. 

- `on_open(` _*args_ `)` _→_ None 

Fired when a dialog opened. 

- `on_dismiss(` _*args_ `)` _→_ None 

Fired when a dialog dismiss. 

- `on_pre_dismiss(` _*args_ `)` _→_ None 

Fired when a dialog pre-dismiss. 

- `on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

**_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

`dismiss(` _*args_ `)` _→_ None 

Closes the dialog. 

`class kivymd.uix.dialog.dialog.MDDialogIcon(` _*args_ , _**kwargs_ `)` 

The class implements an icon. 

For more information, see in the _`MDIcon`_ class documentation. 

`class kivymd.uix.dialog.dialog.MDDialogHeadlineText(` _*args_ , _**kwargs_ `)` 

The class implements the headline text. 

For more information, see in the _`MDLabel`_ class documentation. 

**2.3. Components** 

**591** 



<!-- Start of picture text -->
HOV<br>, - i<br>4 Se ¥ «6 —— 5 ™ /<br>4 MP? age { eel<br>~~ | 1 a<br>os ; | f " \ j<br>eiteeadee ee 5 (<br><!-- End of picture text -->







<!-- Start of picture text -->
MDSmartTile<br>Ibanez GRG121DX-BKF = ——————____» WWiDSmartTileOverlayContainer<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Example** 

Declarative python style with KV 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDSmartTile:
pos_hint:{"center_x":.5,"center_y":.5}
size_hint:None,None
size:"320dp","320dp"
overlap:False
MDSmartTileImage:
source:"bg.jpg"
radius:[dp(24),dp(24),0,0]
MDSmartTileOverlayContainer:
md_bg_color:0,0,0,.5
adaptive_height:True
padding:"8dp"
spacing:"8dp"
radius:[0,0,dp(24),dp(24)]
MDIconButton:
icon:"heart-outline"
theme_icon_color:"Custom"
icon_color:1,0,0,1
pos_hint:{"center_y":.5}
on_release:
self.icon="heart"\
ifself.icon=="heart-outline"else\
"heart-outline"
MDLabel:
text:"IbanezGRG121DX-BKF"
theme_text_color:"Custom"
text_color:"white"
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

**Chapter 2. Contents** 

**594** 

**KivyMD, Release 2.0.1.dev0** 

Declarative python style 

```
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.buttonimportMDIconButton
fromkivymd.uix.imagelistimport(
MDSmartTile,
MDSmartTileImage,
MDSmartTileOverlayContainer,
)
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
classExample(MDApp):
defset_icon(self,heart_outline):
heart_outline.icon=(
"heart"
ifheart_outline.icon=="heart-outline"
else"heart-outline"
)
defon_start(self):
self.root.get_ids().heart_outline.bind(on_release=self.set_icon)
defbuild(self):
self.theme_cls.theme_style="Dark"
returnMDScreen(
MDSmartTile(
MDSmartTileImage(
source="bg.jpg",
radius=[dp(24),dp(24),0,0],
),
MDSmartTileOverlayContainer(
MDIconButton(
id="heart_outline",
icon="heart-outline",
theme_icon_color="Custom",
icon_color=(1,0,0,1),
pos_hint={"center_y":0.5},
),
MDLabel(
text="IbanezGRG121DX-BKF",
theme_text_color="Custom",
text_color="white",
),
md_bg_color=(0,0,0,0.5),
adaptive_height=True,
padding="8dp",
spacing="8dp",
radius=[0,0,dp(24),dp(24)],
),
```

(continues on next page) 

**2.3. Components** 

**595** 





<!-- Start of picture text -->
Ibanez GRG121DX-BKF<br><!-- End of picture text -->



**KivyMD, Release 2.0.1.dev0** 

###### **2.0.0 version** 

```
MDSmartTile:
[...]
MDSmartTileImage:
[...]
MDSmartTileOverlayContainer:
[...]
#Content.
[...]
```

###### **API -** `kivymd.uix.imagelist.imagelist` 

- `class kivymd.uix.imagelist.imagelist.MDSmartTileImage(` _**kwargs_ `)` 

Implements the tile image. 

Changed in version 2.0.0: The _SmartTileImage_ class has been renamed to _MDSmartTileImage_ . 

For more information, see in the _`RectangularRippleBehavior`_ and `ButtonBehavior` and _`FitImage`_ classes documentation. 

`on_touch_down(` _touch_ `)` 

Receive a touch down event. 

###### **Parameters** 

###### **_touch_ :** `MotionEvent` **class** 

Touch received. The touch is in parent coordinates. See `relativelayout` for a discussion on coordinate systems. 

###### **Returns** 

bool If True, the dispatching of the touch event will stop. If False, the event will continue to be dispatched to the rest of the widget tree. 

- `class kivymd.uix.imagelist.imagelist.MDSmartTileOverlayContainer(` _*args_ , _**kwargs_ `)` 

Implements a container for custom widgets to be added to the tile. 

Changed in version 2.0.0: The _SmartTileOverlayBox_ class has been renamed to _MDSmartTileOverlayContainer_ . 

For more information, see in the `BoxLayout` class documentation. 

`add_widget(` _widget_ , _*args_ , _**kwargs_ `)` 

Add a new widget as a child of this widget. 

###### **Parameters** 

###### **_widget_ :** `Widget` 

Widget to add to our list of children. 

###### **_index_ : int, defaults to 0** 

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide. 

**2.3. Components** 

**597** 





<!-- Start of picture text -->
Ibanez GRG1?1BX-BKF<br><!-- End of picture text -->



<!-- Start of picture text -->
> BOS > SEE<br>o +/ Whanez<br>Ibanez GRG121DX-BKF Ibanez GRG121DX-BKF<br>overlap = True overlap = False<br><!-- End of picture text -->





<!-- Start of picture text -->
Allow access<br>Microphone access<br>Location access<br>Haptics Oo<br>Location access O<br><!-- End of picture text -->

Checkboxes allow users to select one or more items from a set. Checkboxes can turn an option on or off. 



**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
size:"48dp","48dp"
pos_hint:{'center_x':.5,'center_y':.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.selectioncontrolimportMDCheckbox
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
return(
MDFloatLayout(
MDCheckbox(
size_hint=(None,None),
size=("48dp","48dp"),
pos_hint={'center_x':.5,'center_y':.5},
)
)
)
Example().run()
```

**Note:** Be sure to specify the size of the checkbox. By default, it is _(dp(48), dp(48))_ , but the ripple effect takes up all the available space. 

**2.3. Components** 

**601** 

**KivyMD, Release 2.0.1.dev0** 

###### **Control state** 

Declarative KV style 

```
MDCheckbox:
on_active:app.on_checkbox_active(*args)
```

Declarative Python style 

```
MDCheckbox(
on_active=self.on_checkbox_active,
)
```

```
defon_checkbox_active(self,checkbox,value):
ifvalue:
print('Thecheckbox',checkbox,'isactive','and',checkbox.state,'state')
else:
print('Thecheckbox',checkbox,'isinactive','and',checkbox.state,'state')
```

###### **MDCheckbox with group** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
<Check@MDCheckbox>:
group:'group'
size_hint:None,None
size:dp(48),dp(48)
MDFloatLayout:
Check:
active:True
pos_hint:{'center_x':.4,'center_y':.5}
Check:
pos_hint:{'center_x':.6,'center_y':.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
```

(continues on next page) 

**Chapter 2. Contents** 

**602** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Declarative Python style 

```
fromkivymd.material_resourcesimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.selectioncontrolimportMDCheckbox
classCheck(MDCheckbox):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.group='group'
self.size_hint=(None,None)
self.size=(dp(48),dp(48))
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
return(
MDFloatLayout(
Check(
pos_hint={'center_x':0.4,'center_y':0.5},
),
Check(
pos_hint={'center_x':0.6,'center_y':0.5},
)
)
)
Example().run()
```

**2.3. Components** 

**603** 

**KivyMD, Release 2.0.1.dev0** 

###### **Parent and child checkboxes** 

Checkboxes can have a parent-child relationship with other checkboxes. When the parent checkbox is checked, all child checkboxes are checked. If a parent checkbox is unchecked, all child checkboxes are unchecked. If some, but not all, child checkboxes are checked, the parent checkbox becomes an indeterminate checkbox. 

###### **Usage** 

Declarative KV style 

```
MDCheckbox:
group:"root"#thisisarequirednamefortheparentcheckboxgroup
MDCheckbox:
group:"child"#thisisarequirednameforagroupofchildcheckboxes
MDCheckbox:
group:"child"#thisisarequirednameforagroupofchildcheckboxes
```

Declarative Python style 

```
MDCheckbox(
#Thisisarequirednamefortheparentcheckboxgroup.
group="root",
)
MDCheckbox(
#Thisisarequirednameforagroupofchildcheckboxes.
group="child",
)
MDCheckbox(
#Thisisarequirednameforagroupofchildcheckboxes.
group="child",
)
```

###### **Example** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
KV='''
<CheckItem>
adaptive_height:True
MDCheckbox:
```

(continues on next page) 

**Chapter 2. Contents** 

**604** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
group:root.group
MDLabel:
text:root.text
adaptive_height:True
padding_x:"12dp"
pos_hint:{"center_y":.5}
MDBoxLayout:
orientation:"vertical"
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
orientation:"vertical"
adaptive_height:True
padding:"12dp","36dp",0,0
spacing:"12dp"
CheckItem:
text:"Recieveemails"
group:"root"
MDBoxLayout:
orientation:"vertical"
adaptive_height:True
padding:"24dp",0,0,0
spacing:"12dp"
CheckItem:
text:"Daily"
group:"child"
CheckItem:
text:"Weekly"
group:"child"
CheckItem:
text:"Monthly"
group:"child"
MDWidget:
'''
classCheckItem(MDBoxLayout):
text=StringProperty()
group=StringProperty()
classExample(MDApp):
defbuild(self):
```

(continues on next page) 

**2.3. Components** 

**605** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self.theme_cls.primary_palette="Teal"
returnBuilder.load_string(KV)
```

```
Example().run()
```

Declarative Python style 

```
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.selectioncontrolimportMDCheckbox
fromkivymd.uix.widgetimportMDWidget
```

```
classCheckItem(MDBoxLayout):
text=StringProperty()
group=StringProperty()
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.adaptive_height=True
self.widgets=[
MDCheckbox(
group=self.group,
),
MDLabel(
text=self.text,
adaptive_height=True,
padding_x="12dp",
pos_hint={"center_y":.5},
),
]
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Teal"
return(
MDBoxLayout(
MDBoxLayout(
CheckItem(
text="Recieveemails",
group="root",
),
MDBoxLayout(
CheckItem(
text="Daily",
group="child",
),
```

(continues on next page) 

**Chapter 2. Contents** 

**606** 





<!-- Start of picture text -->
9:30 e745<br>€ Settings<br>Ger al<br>e@<br>witc ; ©<br>Bluetoott<br>Switches toggle the state of a single item on or off.<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

###### **Usage** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDFloatLayout:
MDSwitch:
pos_hint:{'center_x':.5,'center_y':.5}
'''
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.selectioncontrolimportMDSwitch
classExample(MDApp):
defbuild(self):
self.theme_cls.primary_palette="Green"
self.theme_cls.theme_style="Dark"
return(
MDFloatLayout(
MDSwitch(
pos_hint={'center_x':.5,'center_y':.5},
)
)
)
Example().run()
```

**Note:** Control state of _`MDSwitch`_ same way as in _`MDCheckbox`_ . 

**Chapter 2. Contents** 

**608** 





~~P~~ e 



<!-- Start of picture text -->
ee<br><!-- End of picture text -->

##### ~~ee~~ 

~~B~~ S 

















~~B~~ O 



<!-- Start of picture text -->
ee<br><!-- End of picture text -->

~~ee e~~ d ~~e~~ e ~~a e~~ e ~~a e~~ e 

###### ~~=~~ 







<!-- Start of picture text -->
e e<br><!-- End of picture text -->

~~e~~ e 

~~e~~ e 

**KivyMD, Release 2.0.1.dev0** 

`on_ripple_effect(` _instance_ , _value_ `)` _→_ None 

Fired when the values of _`ripple_effect`_ change. 

`on_active(` _*args_ `)` _→_ None 

Fired when the values of `active` change. 

- `on_thumb_down()` _→_ None 

Fired at the on_touch_down event of the `Thumb` object. Indicates the state of the switch “on/off” by an animation of increasing the size of the thumb. 

###### **2.4 Controllers** 

###### **2.4.1 WindowController** 

Added in version 1.0.0. 

Modules and classes that implement useful methods for getting information about the state of the current application window. 

###### **Controlling the resizing direction of the application window** 

_`# When resizing the application window, the direction of change will be # printed -` '_ _`left` '_ _`or` '_ _`right` '_ _`.`_ `from kivymd.app import MDApp from kivymd.uix.controllers import WindowController from kivymd.uix.screen import MDScreen class MyScreen(MDScreen, WindowController): def on_width(self, *args): print(self.get_window_width_resizing_direction()) class` <u>`Test(MDApp):`</u> `def build(self): return MyScreen() Test().run()` 

**2.4. Controllers** 

**615** 

**KivyMD, Release 2.0.1.dev0** 

**API -** `kivymd.uix.controllers.windowcontroller` 

```
classkivymd.uix.controllers.windowcontroller.WindowController
```

`on_size(` _instance_ , _size: list_ `)` _→_ None 

Called when the application screen size changes. 

`get_real_device_type()` _→_ str 

Returns the device type - ‘mobile’, ‘tablet’ or ‘desktop’. 

`get_window_width_resizing_direction()` _→_ str 

Return window width resizing direction - ‘left’ or ‘right’. 

###### **2.5 Behaviors** 

###### **2.5.1 Scale** 

Added in version 1.1.0. 

Base class for controlling the scale of the widget. 

**Note:** See kivy.graphics.Rotate for more information. 

###### **Kivy** 

```
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivy.propertiesimportNumericProperty
fromkivy.uix.buttonimportButton
fromkivy.appimportApp
KV='''
Screen:
ScaleButton:
size_hint:.5,.5
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.change_scale(self)
canvas.before:
PushMatrix
Scale:
x:self.scale_value_x
y:self.scale_value_y
z:self.scale_value_x
origin:self.center
```

(continues on next page) 

**Chapter 2. Contents** 

**616** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
canvas.after:
PopMatrix
'''
classScaleButton(Button):
scale_value_x=NumericProperty(1)
scale_value_y=NumericProperty(1)
scale_value_z=NumericProperty(1)
classTest(App):
defbuild(self):
returnBuilder.load_string(KV)
defchange_scale(self,instance_button:Button)->None:
Animation(
scale_value_x=0.5,
scale_value_y=0.5,
scale_value_z=0.5,
d=0.3,
).start(instance_button)
Test().run()
```

###### **KivyMD** 

```
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportScaleBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
KV='''
MDScreen:
ScaleBox:
size_hint:.5,.5
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.change_scale(self)
md_bg_color:"red"
'''
classScaleBox(ButtonBehavior,ScaleBehavior,MDBoxLayout):
pass
```

(continues on next page) 

**2.5. Behaviors** 

**617** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defchange_scale(self,instance_button:ScaleBox)->None:
Animation(
scale_value_x=0.5,
scale_value_y=0.5,
scale_value_z=0.5,
d=0.3,
).start(instance_button)
Test().run()
```

**Warning:** Do not use _ScaleBehavior_ class with classes that inherited` from _CommonElevationBehavior_ class. _CommonElevationBehavior_ classes by default contains attributes for scale widget. 

###### **API -** `kivymd.uix.behaviors.scale_behavior` 

```
classkivymd.uix.behaviors.scale_behavior.ScaleBehavior
```

Base class for controlling the scale of the widget. 

###### `scale_value_x` 

X-axis value. 

_`scale_value_x`_ is an `NumericProperty` and defaults to _1_ . 

###### `scale_value_y` 

Y-axis value. 

_`scale_value_y`_ is an `NumericProperty` and defaults to _1_ . 

```
scale_value_z
```

Z-axis value. 

_`scale_value_z`_ is an `NumericProperty` and defaults to _1_ . 

###### `scale_value_center` 

Origin of the scale. Added in version 1.2.0. The format of the origin can be either (x, y) or (x, y, z). 

_`scale_value_center`_ is an `NumericProperty` and defaults to _[]_ . 

**Chapter 2. Contents** 

**618** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.5.2 Focus** 

###### **Changing the background color when the mouse is on the widget.** 

To apply focus behavior, you must create a new class that is inherited from the widget to which you apply the behavior and from the _`StateFocusBehavior`_ class. 

###### **Usage** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCommonElevationBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.behaviors.focus_behaviorimportStateFocusBehavior
KV='''
MDScreen:
md_bg_color:app.theme_cls.backgroundColor
FocusWidget:
size_hint:.5,.3
pos_hint:{"center_x":.5,"center_y":.5}
md_bg_color:self.theme_cls.surfaceContainerHighestColor
MDLabel:
text:"Label"
pos_hint:{"center_y":.5}
halign:"center"
'''
classFocusWidget(MDBoxLayout,CommonElevationBehavior,StateFocusBehavior):
defon_enter(self):
'''Firedwhenmouseenterthebboxofthewidget.'''
self.md_bg_color=self.theme_cls.surfaceVariantColor
defon_leave(self):
'''Firedwhenthemousegoesoutsidethewidgetborder.'''
self.md_bg_color=self.theme_cls.surfaceContainerHighestColor
classExmple(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
returnBuilder.load_string(KV)
```

(continues on next page) 

**2.5. Behaviors** 

**619** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Exmple().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCommonElevationBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.behaviors.focus_behaviorimportStateFocusBehavior
fromkivymd.uix.labelimportMDLabel
fromkivymd.uix.screenimportMDScreen
```

```
classFocusWidget(MDBoxLayout,CommonElevationBehavior,StateFocusBehavior):
defon_enter(self):
```

```
'''Firedwhenmouseenterthebboxofthewidget.'''
```

```
self.md_bg_color=self.theme_cls.surfaceVariantColor
defon_leave(self):
'''Firedwhenthemousegoesoutsidethewidgetborder.'''
self.md_bg_color=self.theme_cls.surfaceContainerHighestColor
```

```
classExmple(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
return(
MDScreen(
FocusWidget(
MDLabel(
text="Label",
pos_hint={"center_y":.5},
halign="center",
),
size_hint=(.5,.3),
pos_hint={"center_x":.5,"center_y":.5},
md_bg_color=self.theme_cls.surfaceContainerHighestColor,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Exmple().run()
```

Color change at focus/defocus 

Declarative KV style 

**Chapter 2. Contents** 

**620** 

**KivyMD, Release 2.0.1.dev0** 

```
FocusWidget:
focus_color:1,0,1,1
unfocus_color:0,0,1,1
```

Declarative Python style 

```
FocusWidget(
focus_color=[1,0,1,1],
unfocus_color=[0,0,1,1],
)
```

###### **API -** `kivymd.uix.behaviors.focus_behavior` 

`class kivymd.uix.behaviors.focus_behavior.StateFocusBehavior(` _*args_ , _**kwargs_ `)` 

Focus behavior class. 

###### **Events** 

###### `on_enter` 

Fired when mouse enters the bbox of the widget AND the widget is visible. 

###### `on_leave` 

Fired when the mouse exits the widget AND the widget is visible. 

For more information, see in the `HoverBehavior` class documentation. 

Added in version 2.0.0. 

###### `focus_behavior` 

Using focus when hovering over a widget. 

_`focus_behavior`_ is a `BooleanProperty` and defaults to _False_ . 

###### `focus_color` 

The color of the widget when the mouse enters the bbox of the widget. 

_`focus_color`_ is a `ColorProperty` and defaults to _None_ . 

###### `unfocus_color` 

The color of the widget when the mouse exits the bbox widget. 

_`unfocus_color`_ is a `ColorProperty` and defaults to _None_ . 

`class kivymd.uix.behaviors.focus_behavior.FocusBehavior(` _*args_ , _**kwargs_ `)` 

Focus behavior class. 

For more information, see in the `StateFocusBehavior` class documentation. 

Deprecated since version 2.0.0. 

**2.5. Behaviors** 

**621** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.5.3 ToggleButton** 

This behavior must always be inherited after the button’s Widget class since it works with the inherited properties of the button class. 

example: 

```
classMyToggleButtonWidget(MDButton,MDToggleButton):
#[...]
pass
```

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.behaviors.toggle_behaviorimportMDToggleButton
fromkivymd.uix.buttonimportMDButton
KV='''
MDScreen:
MDBoxLayout:
adaptive_size:True
spacing:"12dp"
pos_hint:{"center_x":.5,"center_y":.5}
MyToggleButton:
group:"x"
MDButtonText:
text:"Showads"
MyToggleButton:
group:"x"
MDButtonText:
text:"Donotshowads"
MyToggleButton:
group:"x"
MDButtonIcon:
icon:"pencil"
MDButtonText:
text:"Doesnotmatter"
'''
classMyToggleButton(MDButton,MDToggleButton):
...
```

(continues on next page) 

**Chapter 2. Contents** 

**622** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classTest(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
returnBuilder.load_string(KV)
Test().run()
```

Declarative python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.behaviors.toggle_behaviorimportMDToggleButton
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDButton,MDButtonText,MDButtonIcon
fromkivymd.uix.screenimportMDScreen
```

```
classMyToggleButton(MDButton,MDToggleButton):
...
classTest(MDApp):
defbuild(self):
self.theme_cls.theme_style="Dark"
self.theme_cls.primary_palette="Orange"
return(
MDScreen(
MDBoxLayout(
MyToggleButton(
MDButtonText(
text="Showads",
),
group="x",
),
MyToggleButton(
MDButtonIcon(
icon="pencil",
),
MDButtonText(
text="Donotshowads",
),
group="x",
),
MyToggleButton(
MDButtonText(
text="Doesnotmatter",
),
group="x",
),
```

(continues on next page) 

**2.5. Behaviors** 

**623** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
adaptive_size=True,
spacing="12dp",
pos_hint={"center_x":.5,"center_y":.5},
),
)
)
Test().run()
```

**You can inherit the** `MyToggleButton` **class only from the following classes** 

- `MDRaisedButton` 

- `MDFlatButton` 

- `MDRectangleFlatButton` 

- `MDRectangleFlatIconButton` 

- `MDRoundFlatButton` 

- `MDRoundFlatIconButton` 

- `MDFillRoundFlatButton` 

- `MDFillRoundFlatIconButton` 

**API -** `kivymd.uix.behaviors.toggle_behavior` 

`class kivymd.uix.behaviors.toggle_behavior.MDToggleButtonBehavior(` _*args_ , _**kwargs_ `)` 

This mixin class provides `togglebutton` behavior. Please see the `togglebutton behaviors module` documentation for more information. 

Added in version 1.8.0. 

```
background_normal
```

Color of the button in `rgba` format for the ‘normal’ state. 

_`background_normal`_ is a `ColorProperty` and is defaults to _None_ . 

###### `background_down` 

Color of the button in `rgba` format for the ‘down’ state. 

_`background_down`_ is a `ColorProperty` and is defaults to _None_ . 

```
font_color_normal
```

Color of the font’s button in `rgba` format for the ‘normal’ state. 

_`font_color_normal`_ is a `ColorProperty` and is defaults to _None_ . 

```
font_color_down
```

Color of the font’s button in `rgba` format for the ‘down’ state. 

_`font_color_down`_ is a `ColorProperty` and is defaults to _None_ . 

**Chapter 2. Contents** 

**624** 





**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
size_hint:None,None
size:"250dp","50dp"
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
#Withelevationeffect
ElevationWidget:
pos_hint:{"center_x":.5,"center_y":.6}
theme_elevation_level:"Custom"
elevation_level:4
theme_shadow_offset:"Custom"
shadow_offset:0,-6
theme_shadow_softness:"Custom"
shadow_softness:4
#Withoutelevationeffect
ElevationWidget:
pos_hint:{"center_x":.5,"center_y":.4}
'''
classElevationWidget(
RectangularRippleBehavior,
CommonElevationBehavior,
ButtonBehavior,
BackgroundColorBehavior,
):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.md_bg_color="red"
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimport(
RectangularRippleBehavior,
BackgroundColorBehavior,
CommonElevationBehavior,
)
fromkivymd.uix.screenimportMDScreen
```

(continues on next page) 

**Chapter 2. Contents** 

**626** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classElevationWidget(
RectangularRippleBehavior,
CommonElevationBehavior,
ButtonBehavior,
BackgroundColorBehavior,
):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.md_bg_color="red"
self.size_hint=(None,None)
self.size=("250dp","50dp")
classExample(MDApp):
defbuild(self):
return(
MDScreen(
ElevationWidget(
pos_hint={"center_x":.5,"center_y":.6},
theme_elevation_level="Custom",
theme_shadow_softness="Custom",
theme_shadow_softness="Custom",
shadow_softness=4,
elevation_level=4,
shadow_offset=(0,-6),
),
ElevationWidget(
pos_hint={"center_x":.5,"center_y":.4},
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```



**2.5. Behaviors** 

**627** 

**KivyMD, Release 2.0.1.dev0** 

**Warning:** If before the KivyMD 1.1.0 library version you used the elevation property with an average value of _12_ for the shadow, then starting with the KivyMD 1.1.0 library version, the average value of the elevation property will be somewhere _4_ . 

Similarly, create a circular button: 

Declarative style with KV 

```
fromkivy.langimportBuilder
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCircularRippleBehavior,CommonElevationBehavior
fromkivymd.uix.floatlayoutimportMDFloatLayout
KV='''
<CircularElevationButton>
size_hint:None,None
size:"100dp","100dp"
radius:self.size[0]/2
shadow_radius:self.radius[0]
md_bg_color:"red"
MDIcon:
icon:"hand-heart"
halign:"center"
valign:"center"
pos_hint:{"center_x":.5,"center_y":.5}
size:root.size
pos:root.pos
theme_font_size:"Custom"
font_size:root.size[0]*.6
theme_text_color:"Custom"
text_color:"white"
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
CircularElevationButton:
pos_hint:{"center_x":.5,"center_y":.6}
theme_elevation_level:"Custom"
theme_shadow_softness:"Custom"
elevation_level:4
shadow_softness:4
'''
classCircularElevationButton(
CommonElevationBehavior,
CircularRippleBehavior,
ButtonBehavior,
MDFloatLayout,
```

(continues on next page) 

**Chapter 2. Contents** 

**628** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
):
pass
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.metricsimportdp
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCircularRippleBehavior,CommonElevationBehavior
fromkivymd.uix.floatlayoutimportMDFloatLayout
fromkivymd.uix.labelimportMDIcon
fromkivymd.uix.screenimportMDScreen
classCircularElevationButton(
CommonElevationBehavior,
CircularRippleBehavior,
ButtonBehavior,
MDFloatLayout,
):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.size_hint=(None,None)
self.size=(dp(100),dp(100))
self.radius=dp(100)/2
self.shadow_radius=dp(100)/2
self.md_bg_color="red"
self.add_widget(
MDIcon(
icon="hand-heart",
halign="center",
valign="center",
pos_hint={"center_x":.5,"center_y":.5},
size=self.size,
theme_text_color="Custom",
text_color="white",
theme_font_size="Custom",
font_size=self.size[0]*0.6,
)
)
classExample(MDApp):
```

(continues on next page) 

**2.5. Behaviors** 

**629** 

# ~~a a~~ 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
elevation:2
radius:dp(18)
'''
classElevatedWidget(
CommonElevationBehavior,
RectangularRippleBehavior,
ButtonBehavior,
MDWidget,
):
_elev=0#previouselevationvalue
defon_press(self,*args):
ifnotself._elev:
self._elev=self.elevation
Animation(elevation=self.elevation+2,d=0.4).start(self)
defon_release(self,*args):
Animation.cancel_all(self,"elevation")
Animation(elevation=self._elev,d=0.1).start(self)
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative python style 

```
fromkivy.animationimportAnimation
fromkivy.uix.behaviorsimportButtonBehavior
fromkivy.metricsimportdp
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCommonElevationBehavior,RectangularRippleBehavior
fromkivymd.uix.screenimportMDScreen
fromkivymd.uix.widgetimportMDWidget
classElevatedWidget(
CommonElevationBehavior,
RectangularRippleBehavior,
ButtonBehavior,
MDWidget,
):
_elev=0#previouselevationvalue
defon_press(self,*args):
ifnotself._elev:
```

(continues on next page) 

**2.5. Behaviors** 

**631** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
self._elev=self.elevation
Animation(elevation=self.elevation+2,d=0.4).start(self)
defon_release(self,*args):
Animation.cancel_all(self,"elevation")
Animation(elevation=self._elev,d=0.1).start(self)
classExample(MDApp):
defbuild(self):
return(
MDScreen(
ElevatedWidget(
pos_hint={'center_x':.5,'center_y':.5},
size_hint=(None,None),
size=(100,100),
md_bg_color="blue",
elevation=2,
radius=dp(18),
)
)
)
Example().run()
```

**API -** `kivymd.uix.behaviors.elevation` 

`class kivymd.uix.behaviors.elevation.CommonElevationBehavior(` _**kwargs_ `)` 

Common base class for rectangular and circular elevation behavior. 

For more information, see in the `Widget` class documentation. 

###### `elevation_level` 

Elevation level (values from 0 to 5) 

Added in version 1.2.0. 

_`elevation_level`_ is an `BoundedNumericProperty` and defaults to _0_ . 

###### `elevation_levels` 

Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps). 

Added in version 1.2.0. 

_`elevation_levels`_ is an `DictProperty` and defaults to _{0: dp(0), 1: dp(8), 2: dp(23), 3: dp(16), 4: dp(20), 5: dp(24)}_ . 

###### `elevation` 

Elevation of the widget. 

_`elevation`_ is an `BoundedNumericProperty` and defaults to _0_ . 

**Chapter 2. Contents** 

**632** 

**KivyMD, Release 2.0.1.dev0** 

###### `shadow_radius` 

Radius of the corners of the shadow. 

Added in version 1.1.0. 

You don’t have to use this parameter. The radius of the elevation effect is calculated automatically one way or another based on the radius of the parent widget, for example: 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
KV='''
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
MDCard:
radius:dp(12),dp(46),dp(12),dp(46)
size_hint:.5,.3
pos_hint:{"center_x":.5,"center_y":.5}
theme_elevation_level:"Custom"
elevation_level:2
theme_shadow_softness:"Custom"
shadow_softness:4
theme_shadow_offset:"Custom"
shadow_offset:(2,-2)
'''
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
```

```
Test().run()
```



**2.5. Behaviors** 

**633** 

**KivyMD, Release 2.0.1.dev0** 

_`shadow_radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `shadow_softness` 

Softness of the shadow. 

Added in version 1.1.0. 

`from kivy.lang import Builder from kivymd.app import MDApp from kivymd.uix.behaviors import BackgroundColorBehavior,␣` _˓→_ `CommonElevationBehavior KV = ''' <ElevationWidget> size_hint: None, None size: "250dp", "50dp" MDScreen: md_bg_color: self.theme_cls.backgroundColor ElevationWidget: pos_hint: {"center_x": .5, "center_y": .6} theme_elevation_level: "Custom" elevation_level: 5 theme_shadow_softness: "Custom" shadow_softness: 6 ElevationWidget: pos_hint: {"center_x": .5, "center_y": .4} theme_elevation_level: "Custom" elevation_level: 5 theme_shadow_softness: "Custom" shadow_softness: 12 ''' class ElevationWidget(CommonElevationBehavior, BackgroundColorBehavior): def __init__(self, **kwargs): super().__init__(**kwargs) self.md_bg_color = "blue" class Example(MDApp): def build(self): return Builder.load_string(KV) Example().run()` 

**Chapter 2. Contents** 

**634** 



<!-- Start of picture text -->
shadow_softness = 6<br>shadow_softness = 12<br><!-- End of picture text -->





shadow_offset = (-12, -12) 



shadow_offset = (12, -12) 



shadow_offset = (12, 12) 



shadow_offset = (-12, 12) 





**KivyMD, Release 2.0.1.dev0** 

###### **2.5.5 Rotate** 

Added in version 1.1.0. 

Base class for controlling the rotate of the widget. 

**Note:** See kivy.graphics.Rotate for more information. 

###### **Kivy** 

```
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivy.appimportApp
fromkivy.propertiesimportNumericProperty
fromkivy.uix.buttonimportButton
KV='''
Screen:
RotateButton:
size_hint:.5,.5
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.change_rotate(self)
canvas.before:
PushMatrix
Rotate:
angle:self.rotate_value_angle
axis:0,0,1
origin:self.center
canvas.after:
PopMatrix
'''
classRotateButton(Button):
rotate_value_angle=NumericProperty(0)
classTest(App):
defbuild(self):
returnBuilder.load_string(KV)
defchange_rotate(self,instance_button:Button)->None:
Animation(rotate_value_angle=45,d=0.3).start(instance_button)
Test().run()
```

**2.5. Behaviors** 

**639** 

**KivyMD, Release 2.0.1.dev0** 

###### **KivyMD** 

```
fromkivy.animationimportAnimation
fromkivy.langimportBuilder
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportRotateBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
KV='''
MDScreen:
RotateBox:
size_hint:.5,.5
pos_hint:{"center_x":.5,"center_y":.5}
on_release:app.change_rotate(self)
md_bg_color:"red"
'''
classRotateBox(ButtonBehavior,RotateBehavior,MDBoxLayout):
pass
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defchange_rotate(self,instance_button:RotateBox)->None:
Animation(rotate_value_angle=45,d=0.3).start(instance_button)
```

```
Test().run()
```

**Warning:** Do not use _RotateBehavior_ class with classes that inherited` from _CommonElevationBehavior_ class. _CommonElevationBehavior_ classes by default contains attributes for rotate widget. 

###### **API -** `kivymd.uix.behaviors.rotate_behavior` 

```
classkivymd.uix.behaviors.rotate_behavior.RotateBehavior
```

Base class for controlling the rotate of the widget. 

###### `rotate_value_angle` 

Property for getting/setting the angle of the rotation. 

_`rotate_value_angle`_ is an `NumericProperty` and defaults to _0_ . 

###### `rotate_value_axis` 

Property for getting/setting the axis of the rotation. 

_`rotate_value_axis`_ is an `ListProperty` and defaults to _(0, 0, 1)_ . 

**Chapter 2. Contents** 

**640** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.5.6 Ripple** 

###### **Classes implements a circular and rectangular ripple effects.** 

To create a widget with ircular ripple effect, you must create a new class that inherits from the _`CircularRippleBehavior`_ class. 

For example, let’s create an image button with a circular ripple effect: 

```
fromkivy.langimportBuilder
fromkivy.uix.behaviorsimportButtonBehavior
fromkivy.uix.imageimportImage
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportCircularRippleBehavior
KV='''
MDScreen:
CircularRippleButton:
source:"data/logo/kivy-icon-256.png"
size_hint:None,None
size:"250dp","250dp"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classCircularRippleButton(CircularRippleBehavior,ButtonBehavior,Image):
def__init__(self,**kwargs):
self.ripple_scale=0.85
super().__init__(**kwargs)
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

To create a widget with rectangular ripple effect, you must create a new class that inherits from the _`RectangularRippleBehavior`_ class: 

```
fromkivy.langimportBuilder
fromkivy.uix.behaviorsimportButtonBehavior
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportRectangularRippleBehavior,BackgroundColorBehavior
fromkivymd.uix.widgetimportMDWidget
```

(continues on next page) 

**2.5. Behaviors** 

**641** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
KV='''
MDScreen:
RectangularRippleButton:
size_hint:None,None
size:"250dp","50dp"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classRectangularRippleButton(
MDWidget,RectangularRippleBehavior,ButtonBehavior,BackgroundColorBehavior
):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.md_bg_color=[0,0,1,1]
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

**API -** `kivymd.uix.behaviors.ripple_behavior` 

```
classkivymd.uix.behaviors.ripple_behavior.CommonRipple
```

Base class for ripple effect. 

```
propertyactive_canvas
```

```
ripple_rad_default
```

The starting value of the radius of the ripple effect. 

Deprecated since version 2.0.0: Do not use this attribute. 

```
CircularRippleButton:
ripple_rad_default:100
```

_`ripple_rad_default`_ is an `NumericProperty` and defaults to _1_ . 

```
ripple_color
```

Ripple color in (r, g, b, a) format. 

```
CircularRippleButton:
ripple_color:app.theme_cls.primary_color
```

_`ripple_color`_ is an `ColorProperty` and defaults to _None_ . 

**Chapter 2. Contents** 

**642** 

**KivyMD, Release 2.0.1.dev0** 

###### `ripple_alpha` 

Alpha channel values for ripple effect. 

```
CircularRippleButton:
ripple_alpha:.9
ripple_color:app.theme_cls.primary_color
```

_`ripple_alpha`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `ripple_scale` 

Ripple effect scale. 

```
CircularRippleButton:
ripple_scale:.5
```

```
CircularRippleButton:
ripple_scale:1
```

_`ripple_scale`_ is an `NumericProperty` and defaults to _None_ . 

###### `ripple_duration_in_fast` 

Ripple duration when touching to widget. 

```
CircularRippleButton:
ripple_duration_in_fast:200
```

_`ripple_duration_in_fast`_ is an `NumericProperty` and defaults to _450_ . 

###### `ripple_duration_in_slow` 

Ripple duration when long touching to widget. 

```
CircularRippleButton:
ripple_duration_in_slow:1000
```

_`ripple_duration_in_slow`_ is an `NumericProperty` and defaults to _375_ . 

###### `ripple_duration_out` 

The duration of the disappearance of the wave effect. 

Deprecated since version 2.0.0: Do not use this attribute. 

```
CircularRippleButton:
ripple_duration_out:5
```

_`ripple_duration_out`_ is an `NumericProperty` and defaults to _0.3_ . 

**2.5. Behaviors** 

**643** 

**KivyMD, Release 2.0.1.dev0** 

###### `ripple_canvas_after` 

The ripple effect is drawn above/below the content. 

Added in version 1.0.0. 

Deprecated since version 2.0.0: Do not use this attribute. 

```
MDIconButton:
ripple_canvas_after:True
icon:"android"
ripple_alpha:.8
ripple_color:app.theme_cls.primary_color
icon_size:"100sp"
```

```
MDIconButton:
ripple_canvas_after:False
icon:"android"
ripple_alpha:.8
ripple_color:app.theme_cls.primary_color
icon_size:"100sp"
```

_`ripple_canvas_after`_ is an `BooleanProperty` and defaults to _True_ . 

```
ripple_func_in
```

Type of animation for ripple in effect. 

Deprecated since version 2.0.0: Use `ripple_func` instead. 

_`ripple_func_in`_ is an `StringProperty` and defaults to _‘out_quad’_ . 

```
ripple_func_out
```

Type of animation for ripple out effect. 

Deprecated since version 2.0.0: Use `ripple_func` instead. 

_`ripple_func_out`_ is an `StringProperty` and defaults to _‘ripple_func_out’_ . 

```
ripple_effect
```

Should I use the ripple effect. 

_`ripple_effect`_ is an `BooleanProperty` and defaults to _True_ . 

`abstract lay_canvas_instructions()` _→_ None 

`start_ripple()` _→_ None `finish_ripple()` _→_ None `fade_out(` _*args_ `)` _→_ None 

`anim_complete(` _*args_ `)` _→_ None 

Fired when the “fade_out” animation complete. 

`on_touch_down(` _touch_ `)` 

`call_ripple_animation_methods(` _touch_ `)` _→_ None 

**Chapter 2. Contents** 

**644** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_touch_move(` _touch_ , _*args_ `)` 

###### `on_touch_up(` _touch_ `)` 

###### `class kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` 

Class implements a rectangular ripple effect. 

For more information, see in the `CommonRipple` class documentation. 

###### `ripple_scale` 

See _`ripple_scale`_ . 

_`ripple_scale`_ is an `NumericProperty` and defaults to _2.75_ . 

###### `lay_canvas_instructions()` _→_ None 

Adds graphic instructions to the canvas to implement ripple animation. 

###### `class kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` 

Class implements a circular ripple effect. 

For more information, see in the `CommonRipple` class documentation. 

###### `ripple_scale` 

See _`ripple_scale`_ . 

_`ripple_scale`_ is an `NumericProperty` and defaults to _1_ . 

###### `lay_canvas_instructions()` _→_ None 

- `class kivymd.uix.behaviors.ripple_behavior.M3CommonRipple(` _**kwargs_ `)` 

   - Base class for Material 3 ripple effect. 

Added in version 2.0.0. 

###### `NOISE_ANIMATION_DURATION = 7000` 

###### `PHASE_DIVISOR = 214` 

###### `ripple_alpha` 

Alpha channel values for ripple effect. 

```
CircularRippleButton:
ripple_alpha:.9
ripple_color:app.theme_cls.primary_color
```

_`ripple_alpha`_ is an `NumericProperty` and defaults to _0.2_ . 

###### `ripple_origin_to_center` 

Move the ripple origin from the touch position to the widget center while the animation progresses. 

_`ripple_origin_to_center`_ is an `BooleanProperty` and defaults to _True_ . 

###### `sparkle_color` 

Sparkle color in (r, g, b, a) format. 

_`sparkle_color`_ is an `ColorProperty` and defaults to _ripple_color_ with alpha set to _1.0_ . 

**2.5. Behaviors** 

**645** 

**KivyMD, Release 2.0.1.dev0** 

###### `ripple_func` 

Type of animation for ripple in effect. 

Available options are: ‘standard’, ‘decelerated’, ‘accelerate’, ‘linear’. 

_`ripple_func`_ is an `OptionProperty` and defaults to _‘standard’_ . 

```
init_fbos()
```

`set_shader(` _obj_ `)` 

`call_ripple_animation_methods(` _touch_ `)` _→_ None 

`lay_canvas_instructions()` _→_ None 

`start_ripple()` _→_ None 

`finish_ripple()` _→_ None 

`anim_complete(` _*args_ `)` _→_ None 

Fired when the “fade_out” animation complete. 

`on_touch_down(` _touch_ `)` 

`class kivymd.uix.behaviors.ripple_behavior.M3RectangularRippleBehavior(` _**kwargs_ `)` 

Material 3 rectangular ripple behavior. 

`class kivymd.uix.behaviors.ripple_behavior.M3CircularRippleBehavior(` _**kwargs_ `)` Material 3 circular ripple behavior. 

```
kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior
```

```
kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior
```

###### **2.5.7 Magic** 

**Magical effects for buttons.** 

**Warning:** Magic effects do not work correctly with _KivyMD_ buttons! 

To apply magic effects, you must create a new class that is inherited from the widget to which you apply the effect and from the _`MagicBehavior`_ class. 

```
classMagicButton(MagicBehavior,MDButton):
```

```
...
```

**Chapter 2. Contents** 

**646** 

**KivyMD, Release 2.0.1.dev0** 

**The** `MagicBehavior` **class provides five effects:** 

- _`MagicBehavior.wobble`_ 

- _`MagicBehavior.grow`_ 

- _`MagicBehavior.shake`_ 

- _`MagicBehavior.twist`_ 

- _`MagicBehavior.shrink`_ 

###### **Example** 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportMagicBehavior
fromkivymd.uix.buttonimportMDButton,MDButtonText
KV='''
MDScreen:
md_bg_color:app.theme_cls.backgroundColor
MagicButtonGrowEffect:
on_release:self.grow()
pos_hint:{"center_x":.5,"center_y":.4}
MagicButtonShakeEffect:
on_release:self.shake()
pos_hint:{"center_x":.5,"center_y":.5}
MagicButtonTwistEffect:
on_release:self.twist()
pos_hint:{"center_x":.5,"center_y":.6}
MagicButtonShrinkEffect:
on_release:self.shrink()
pos_hint:{"center_x":.5,"center_y":.7}
MagicButtonWobbleEffect:
on_release:self.wobble()
pos_hint:{"center_x":.5,"center_y":.8}
'''
classBaseMagicButton(MDButton):
'''
Abasebuttonclasswithcustomizabletextandoutlinedstyle.
Thisclassservesasafoundationforcreatingmagic-effectbuttons
(likegrow,shake,twist)withpredefinedstylingandstructure.
```

(continues on next page) 

**2.5. Behaviors** 

**647** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
ItautomaticallyinitializesabuttonwithMDButtonTextasitschildwidget.
'''
text=StringProperty()
style="outlined"
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDButtonText(
text=self.text
)
]
super().__init__(*args,**kwargs)
classMagicButtonGrowEffect(MagicBehavior,BaseMagicButton):
scale_value=1.03
text="GrowEffect"
classMagicButtonShakeEffect(MagicBehavior,BaseMagicButton):
translate_value=15
text="ShakeEffect"
classMagicButtonTwistEffect(MagicBehavior,BaseMagicButton):
rotate_value=6
text="TwistEffect"
classMagicButtonShrinkEffect(MagicBehavior,BaseMagicButton):
scale_value=0.95
text="ShrinkEffect"
classMagicButtonWobbleEffect(MagicBehavior,BaseMagicButton):
scale_value=0.95
text="WobbleEffect"
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

Declarative Python style 

```
fromkivy.clockimportClock
fromkivy.propertiesimportStringProperty
```

(continues on next page) 

**Chapter 2. Contents** 

**648** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportMagicBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.buttonimportMDButton,MDButtonText
fromkivymd.uix.screenimportMDScreen
```

```
classBaseMagicButton(MDButton):
'''
Abasebuttonclasswithcustomizabletextandoutlinedstyle.
Thisclassservesasafoundationforcreatingmagic-effectbuttons
(likegrow,shake,twist)withpredefinedstylingandstructure.
ItautomaticallyinitializesabuttonwithMDButtonTextasitschildwidget.
'''
text=StringProperty()
style="outlined"
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
Clock.schedule_once(self.add_text)
defadd_text(self,*args)->None:
self.widgets=[
MDButtonText(
text=self.text,
pos_hint={"center_x":.5,"center_y":.5}
)
]
defon_release(self,*args)->None:
super().on_release(args)
{
"Grow":self.grow,
"Shake":self.shake,
"Twist":self.twist,
"Shrink":self.shrink,
"Wobble":self.wobble,
}.get(self.text.split()[0],"Grow")()
classMagicButtonGrowEffect(MagicBehavior,BaseMagicButton):
scale_value=1.03
text="GrowEffect"
classMagicButtonShakeEffect(MagicBehavior,BaseMagicButton):
translate_value=15
text="ShakeEffect"
```

(continues on next page) 

**2.5. Behaviors** 

**649** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classMagicButtonTwistEffect(MagicBehavior,BaseMagicButton):
rotate_value=6
text="TwistEffect"
```

```
classMagicButtonShrinkEffect(MagicBehavior,BaseMagicButton):
scale_value=0.95
text="ShrinkEffect"
```

```
classMagicButtonWobbleEffect(MagicBehavior,BaseMagicButton):
scale_value=0.95
text="WobbleEffect"
```

```
classExample(MDApp):
defbuild(self):
return(
MDScreen(
MDBoxLayout(
MagicButtonGrowEffect(
),
MagicButtonShakeEffect(
),
MagicButtonTwistEffect(
),
MagicButtonShrinkEffect(
),
MagicButtonWobbleEffect(
),
spacing="24dp",
orientation="vertical",
adaptive_size=True,
pos_hint={"center_x":.5,"center_y":.5}
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
Example().run()
```

**Chapter 2. Contents** 

**650** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.behaviors.magic_behavior` 

```
classkivymd.uix.behaviors.magic_behavior.MagicBehavior
```

A mixin class that provides animated visual effects for Kivy/KivyMD widgets. 

_MagicBehavior_ adds interactive animation effects that enhance user interface feedback and engagement. These animations include: 

- _grow()_ : Expands the widget slightly and returns to its original size. 

- _shake()_ : Shakes the widget horizontally. 

- _wobble()_ : Squashes and stretches the widget briefly. 

- _twist()_ : Rotates the widget and resets its angle. 

- _shrink()_ : Shrinks the widget temporarily and restores it. 

###### `scale_value` 

Scale factor for animation effects. 

Added in version 2.0.0. 

_`scale_value`_ is a `NumericProperty` and defaults to _1_ . 

###### `translate_value` 

Translation distance for animation effects. 

Added in version 2.0.0. 

_`translate_value`_ is a `NumericProperty` and defaults to _1_ . 

###### `rotate_value` 

Rotation angle in degrees for animation effects. 

Added in version 2.0.0. 

_`rotate_value`_ is a `NumericProperty` and defaults to _25_ . 

###### `magic_speed` 

Animation playback speed. 

_`magic_speed`_ is a `NumericProperty` and defaults to _1_ . 

###### `grow()` _→_ None 

Grow effect animation. 

###### `shake()` _→_ None 

Shake effect animation. 

`wobble()` _→_ None 

Wobble effect animation. 

`twist()` _→_ None 

Twist effect animation. 

`shrink()` _→_ None 

Shrink effect animation. 

`on_touch_up(` _*args_ `)` 

**2.5. Behaviors** 

**651** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.5.8 Hover** 

###### **Changing when the mouse is on the widget and the widget is visible.** 

To apply hover behavior, you must create a new class that is inherited from the widget to which you apply the behavior and from the _`HoverBehavior`_ class. 

In _KV file_ : 

```
<HoverItem@MDBoxLayout+HoverBehavior>
```

In _python file_ : 

```
classHoverItem(MDBoxLayout,HoverBehavior):
'''Customitemimplementinghoverbehavior.'''
```

After creating a class, you must define two methods for it: _`HoverBehavior.on_enter`_ and _`HoverBehavior. on_leave`_ , which will be automatically called when the mouse cursor is over the widget and when the mouse cursor goes beyond the widget. 

**Note:** _`HoverBehavior`_ will by default check to see if the current Widget is visible (i.e. not covered by a modal or popup and not a part of a RelativeLayout, MDTab or Carousel that is not currently visible etc) and will only issue events if the widget is visible. 

To get the legacy behavior that the events are always triggered, you can set _detect_visible_ on the Widget to _False_ . 

Declarative KV style 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportHoverBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
KV='''
MDScreen
md_bg_color:self.theme_cls.backgroundColor
MDBoxLayout:
id:box
pos_hint:{'center_x':.5,'center_y':.5}
size_hint:.8,.8
md_bg_color:self.theme_cls.secondaryContainerColor
'''
classHoverItem(MDBoxLayout,HoverBehavior):
'''Customitemimplementinghoverbehavior.'''
defon_enter(self,*args):
'''
```

(continues on next page) 

**Chapter 2. Contents** 

**652** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Themethodwillbecalledwhenthemousecursor
iswithinthebordersofthecurrentwidget.
'''
self.md_bg_color="white"
defon_leave(self,*args):
'''
Themethodwillbecalledwhenthemousecursorgoesbeyond
thebordersofthecurrentwidget.
'''
self.md_bg_color=self.theme_cls.secondaryContainerColor
classExample(MDApp):
defbuild(self):
self.screen=Builder.load_string(KV)
foriinrange(5):
self.screen.ids.box.add_widget(HoverItem())
returnself.screen
Example().run()
```

Declarative Python style 

```
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportHoverBehavior
fromkivymd.uix.boxlayoutimportMDBoxLayout
fromkivymd.uix.screenimportMDScreen
```

```
classHoverItem(MDBoxLayout,HoverBehavior):
'''Customitemimplementinghoverbehavior.'''
defon_enter(self,*args):
'''
Themethodwillbecalledwhenthemousecursor
iswithinthebordersofthecurrentwidget.
'''
self.md_bg_color="white"
defon_leave(self,*args):
'''
Themethodwillbecalledwhenthemousecursorgoesbeyond
thebordersofthecurrentwidget.
'''
self.md_bg_color=self.theme_cls.secondaryContainerColor
```

(continues on next page) 

**2.5. Behaviors** 

**653** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
self.screen=(
MDScreen(
MDBoxLayout(
id="box",
pos_hint={'center_x':.5,'center_y':.5},
size_hint=(.8,.8),
md_bg_color=self.theme_cls.secondaryContainerColor,
),
md_bg_color=self.theme_cls.backgroundColor,
)
)
foriinrange(5):
self.screen.get_ids().box.add_widget(HoverItem())
returnself.screen
Example().run()
```

###### **API -** `kivymd.uix.behaviors.hover_behavior` 

`class kivymd.uix.behaviors.hover_behavior.HoverBehavior(` _*args_ , _**kwargs_ `)` 

###### **Events** 

```
on_enter
```

Fired when mouse enters the bbox of the widget and the widget is visible. 

```
on_leave
```

Fired when the mouse exits the widget and the widget is visible. 

###### `hovering` 

_True_ , if the mouse cursor is within the borders of the widget. 

Note that this is set and cleared even if the widget is not visible. 

`hover` is a `BooleanProperty` and defaults to _False_ . 

###### `hover_visible` 

_True_ if hovering is _True_ and is the current widget is visible. 

_`hover_visible`_ is a `BooleanProperty` and defaults to _False_ . 

###### `enter_point` 

Holds the last position where the mouse pointer crossed into the Widget if the Widget is visible and is currently in a hovering state. 

_`enter_point`_ is a `ObjectProperty` and defaults to _None_ . 

###### `detect_visible` 

Should this widget perform the visibility check? 

Deprecated since version 2.0.0: Use _`allow_hover`_ instead. 

**Chapter 2. Contents** 

**654** 

**KivyMD, Release 2.0.1.dev0** 

_`detect_visible`_ is a `BooleanProperty` and defaults to _True_ . 

###### `allow_hover` 

Whether to use hover behavior. 

Added in version 2.0.0. 

_`allow_hover`_ is a `BooleanProperty` and defaults to _True_ . 

###### `is_mouse_inside_widget(` _pos_ `)` 

Check if the mouse is within the widget boundaries in window coordinates. 

`on_detect_visible(` _instance_ , _value_ `)` 

###### `on_mouse_update(` _*args_ `)` 

Main handler for mouse movement — determines whether mouse has entered or exited. 

###### `on_enter()` 

Fired when mouse enter the bbox of the widget. 

###### `on_leave()` 

Fired when the mouse goes outside the widget border. 

###### **2.5.9 Declarative** 

Added in version 1.0.0. 

As you already know, the Kivy framework provides the best/simplest/modern UI creation tool that allows you to separate the logic of your application from the description of the properties of widgets/GUI components. This tool is named KV Language. 

But in addition to creating a user interface using the KV Language Kivy allows you to create user interface elements directly in the Python code. And if you’ve ever created a user interface in Python code, you know how ugly it looks. Even in the simplest user interface design, which was created using Python code it is impossible to trace the widget tree, because in Python code you build the user interface in an imperative style. 

###### **Imperative style** 

```
fromkivymd.appimportMDApp
fromkivymd.uix.navigationbarimport(
MDNavigationBar,
MDNavigationItem,
MDNavigationItemIcon,
MDNavigationItemLabel,
```

```
)
fromkivymd.uix.screenimportMDScreen
```

```
classExample(MDApp):
defbuild(self):
screen=MDScreen()
bottom_navigation=MDNavigationBar()
```

(continues on next page) 

**2.5. Behaviors** 

**655** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
datas=[
{"text":"Mail","icon":"gmail"},
{"text":"GitHub","icon":"git"},
{"text":"LinkedIN","icon":"linkedin"},
]
fordataindatas:
text=data["text"]
navigation_item=MDNavigationItem(
MDNavigationItemIcon(
icon=data["icon"],
),
MDNavigationItemLabel(
text=text,
),
)
bottom_navigation.add_widget(navigation_item)
screen.add_widget(bottom_navigation)
returnscreen
Example().run()
```

Take a look at the above code example. This is a very simple UI. But looking at this code, you will not be able to figure the widget tree and understand which UI this code implements. This is named imperative programming style, which is used in Kivy. 

Now let’s see how the same code is implemented using the KV language, which uses a declarative style of describing widget properties. 

###### **Declarative style with KV language** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(
'''
MDScreen:
MDNavigationBar:
MDNavigationItem:
MDNavigationItemIcon:
icon:"gmail"
```

(continues on next page) 

**Chapter 2. Contents** 

**656** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
MDNavigationItemLabel:
text:"Mail"
MDNavigationItem:
MDNavigationItemIcon:
icon:"git"
MDNavigationItemLabel:
text:"GitHub"
MDNavigationItem:
MDNavigationItemIcon:
icon:"linkedin"
MDNavigationItemLabel:
text:"LinkedIN"
'''
)
Example().run()
```

Looking at this code, we can now clearly see the widget tree and their properties. We can quickly navigate through the components of the screen and quickly change/add new properties/widgets. This is named declarative UI creation style. 

But now the KivyMD library allows you to write Python code in a declarative style. Just as it is implemented in Flutter/Jetpack Compose/SwiftUI. 

###### **Declarative style with Python code** 

```
fromkivymd.appimportMDApp
fromkivymd.uix.navigationbarimport(
MDNavigationBar,
MDNavigationItemIcon,
MDNavigationItem,
MDNavigationItemLabel,
)
classExample(MDApp):
defbuild(self):
returnMDNavigationBar(
MDNavigationItem(
MDNavigationItemIcon(
icon="gmail",
),
MDNavigationItemLabel(
text="Mail",
),
```

(continues on next page) 

**2.5. Behaviors** 

**657** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
),
MDNavigationItem(
MDNavigationItemIcon(
icon="twitter",
),
MDNavigationItemLabel(
text="Twitter",
),
),
MDNavigationItem(
MDNavigationItemIcon(
icon="linkedin",
),
MDNavigationItemLabel(
text="LinkedIN",
),
),
)
Example().run()
```

**Note:** The KivyMD library does not support creating Kivy widgets in Python code in a declarative style. 

But you can still use the declarative style of creating Kivy widgets in Python code. To do this, you need to create a new class that will be inherited from the Kivy widget and the _`DeclarativeBehavior`_ class: 

```
fromkivy.uix.boxlayoutimportBoxLayout
fromkivy.uix.buttonimportButton
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportDeclarativeBehavior
classDeclarativeStyleBoxLayout(DeclarativeBehavior,BoxLayout):
pass
classExample(MDApp):
defbuild(self):
return(
DeclarativeStyleBoxLayout(
Button(),
Button(),
orientation="vertical",
)
)
Example().run()
```

**Chapter 2. Contents** 

**658** 

**KivyMD, Release 2.0.1.dev0** 

###### **Get objects by identifiers** 

In the declarative style in Python code, the ids parameter of the specified widget will return only the id of the child widget/container, ignoring other ids. Therefore, to get objects by identifiers in declarative style in Python code, you must specify all the container ids in which the widget is nested until you get to the desired id: 

`from kivymd.app import MDApp from kivymd.uix.boxlayout import MDBoxLayout from kivymd.uix.button import MDButton, MDButtonText from kivymd.uix.floatlayout import MDFloatLayout class Example(MDApp): def build(self): return ( MDBoxLayout( MDFloatLayout( MDButton( MDButtonText( text="Button 1", ), id="button_1", pos_hint={"center_x": 0.5, "center_y": 0.5}, ), id="box_container_1", ), MDBoxLayout( MDFloatLayout( MDButton( MDButtonText( text="Button 2", ), id="button_2", pos_hint={"center_x": 0.5, "center_y": 0.5}, ), id="float_container", ), id="box_container_2", ) ) ) def on_start(self):` _`# { #` '_ _`button_1` '_ _`: <kivymd.uix.button.button.MDButton object at 0x11d93c9e0>, #` '_ _`button_2` '_ _`: <kivymd.uix.button.button.MDButton object at 0x11da128f0>, #` '_ _`float_container` '_ _`: <kivymd.uix.floatlayout.MDFloatLayout object at`_ `␣` _˓→_ _`0x11da228f0>, #` '_ _`box_container_1` '_ _`: <kivymd.uix.floatlayout.MDFloatLayout object at`_ `␣` _˓→_ _`0x11d9fc3c0>, #` '_ _`box_container_2` '_ _`: <kivymd.uix.boxlayout.MDBoxLayout object at 0x11dbf06d0>, # }`_ `print(self.root.get_ids())` 

(continues on next page) 

**2.5. Behaviors** 

**659** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
Example().run()
```

Yes, this is not a very good solution, but I think it will be fixed soon. 

**Warning:** Declarative programming style in Python code in the KivyMD library is an experimental feature. Therefore, if you receive errors, do not hesitate to create new issue in the KivyMD repository. 

###### **API -** `kivymd.uix.behaviors.declarative_behavior` 

`class kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior(` _*args_ , _**kwargs_ `)` 

Implements the creation and addition of child widgets as declarative programming style. 

```
id
```

Widget ID. 

_`id`_ is an `StringProperty` and defaults to _‘’_ . 

###### `widgets` 

List of child widgets added declaratively. 

Added in version 2.0.0. 

The _widgets_ property allows you to define and manage child widgets in a declarative way. When assigned, the widgets in the list are automatically added to the parent container, and their IDs (if set) are registered internally for later reference. 

This property eliminates the need to call _add_widget()_ manually for each child widget. 

Declarative Python style 

```
classCustomListItem(MDListItem):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.widgets=[
MDListItemLeadingIcon(icon="account"),
MDListItemHeadlineText(text="Title"),
MDListItemSupportingText(text="Subtitle"),
MDListItemTertiaryText(text="Tertiary"),
MDListItemTrailingIcon(icon="lock"),
]
```

Imperative Python style 

```
classCustomListItem(MDListItem):
def__init__(self,**kwargs):
super().__init__(**kwargs)
self.add_widget(MDListItemLeadingIcon(icon="account"))
self.add_widget(MDListItemHeadlineText(text="Title"))
self.add_widget(MDListItemSupportingText(text="Subtitle"))
self.add_widget(MDListItemTertiaryText(text="Tertiary"))
self.add_widget(MDListItemTrailingIcon(icon="lock"))
```

**Chapter 2. Contents** 

**660** 

**KivyMD, Release 2.0.1.dev0** 

###### **Full example** 

```
fromkivymd.appimportMDApp
fromkivymd.uix.listimport(
MDListItem,
MDListItemLeadingIcon,
MDListItemHeadlineText,
MDListItemSupportingText,
MDListItemTertiaryText,
MDListItemTrailingIcon,
)
```

```
fromkivymd.uix.screenimportMDScreen
```

```
classCustomListItem(MDListItem):
def__init__(self,*args,**kwargs):
super().__init__(*args,**kwargs)
self.widgets=[
MDListItemLeadingIcon(
icon="account"
),
MDListItemHeadlineText(
text="MDListItemHeadlineText"
),
MDListItemSupportingText(
text="MDListItemSupportingText"
),
MDListItemTertiaryText(
text="MDListItemTertiaryText"
),
MDListItemTrailingIcon(
icon="lock"
)
]
classExample(MDApp):
defbuild(self):
return(
MDScreen(
CustomListItem(
pos_hint={"center_x":0.5,"center_y":0.5},
size_hint_x=0.5
),
md_bg_color=self.theme_cls.backgroundColor
)
)
```

```
Example().run()
```

**2.5. Behaviors** 

**661** 

**KivyMD, Release 2.0.1.dev0** 

**Warning:** When using the _widgets_ property, it is recommended to only interact with child widgets via their registered IDs. 

`class` <u>`CustomListItem(MDListItem):`</u> `def __init__(self, *args, **kwargs): [...] self.widgets = [ MDListItemLeadingIcon( id="icon_account", icon="account" ), [...] ] class Example(MDApp): def change_icon(self, list_item):` _`# This work.`_ `list_item.get_ids().icon_account.icon = "account-alert" def build(self): return ( MDScreen( CustomListItem( [...] on_release=self.change_icon, ), [...] ) )` Adding to or removing items from _self.widgets_ directly at runtime may lead to unexpected behavior. `class` <u>`CustomListItem(MDListItem):`</u> `def __init__(self, *args, **kwargs): [...] self.widgets = [ MDListItemLeadingIcon( id="icon_account", icon="account" ), [...] ] class Example(MDApp): def remove_icon(self, list_item):` _`# This won` '_ _`t work.`_ `list_item.widgets.remove(list_item.get_ids().icon_account)` <u>`def build(self):`</u> `return (` ~~`MDScreen(`~~ **Chapter 2. Contents** `CustomListItem( [...] on_release=self.remove_icon, ),` 

**662** 

**KivyMD, Release 2.0.1.dev0** 

_`widgets`_ is a `ListProperty` and defaults to an empty list _[]_ . 

- `on_widgets(` _instance_ , _value_ `)` _→_ None 

Fired when the values of _`widgets`_ change. 

Added in version 2.0.0. 

- `get_ids()` _→_ dict 

Returns a dictionary of widget IDs defined in Python code that is written in a declarative style. 

###### **2.5.10 Touch** 

###### **Provides easy access to events.** 

The following events are available: 

- on_long_touch 

- on_double_tap 

- on_triple_tap 

###### **Usage** 

```
fromkivy.langimportBuilder
fromkivy.propertiesimportStringProperty
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportTouchBehavior
fromkivymd.uix.buttonimportMDButton
KV='''
<TouchBehaviorButton>
style:"elevated"
MDButtonText:
text:root.text
MDScreen:
md_bg_color:self.theme_cls.backgroundColor
TouchBehaviorButton:
text:"TouchBehavior"
pos_hint:{"center_x":.5,"center_y":.5}
'''
classTouchBehaviorButton(MDButton,TouchBehavior):
```

(continues on next page) 

**2.5. Behaviors** 

**663** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
text=StringProperty()
```

```
defon_long_touch(self,*args):
print("<on_long_touch>event")
defon_double_tap(self,*args):
print("<on_double_tap>event")
defon_triple_tap(self,*args):
print("<on_triple_tap>event")
```

```
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Example().run()
```

**API -** `kivymd.uix.behaviors.touch_behavior` 

`class kivymd.uix.behaviors.touch_behavior.TouchBehavior(` _**kwargs_ `)` 

```
duration_long_touch
```

Time for a long touch. 

_`duration_long_touch`_ is an `NumericProperty` and defaults to _0.4_ . 

`create_clock(` _widget_ , _touch_ , _*args_ `)` 

`delete_clock(` _widget_ , _touch_ , _*args_ `)` 

Removes a key event from _touch.ud_ . 

`on_long_touch(` _touch_ , _*args_ `)` 

Fired when the widget is pressed for a long time. 

`on_double_tap(` _touch_ , _*args_ `)` 

Fired by double-clicking on the widget. 

`on_triple_tap(` _touch_ , _*args_ `)` 

Fired by triple clicking on the widget. 

###### **2.5.11 State Layer** 

###### **See also:** 

Material Design spec, State layers 

**Chapter 2. Contents** 

**664** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.behaviors.state_layer_behavior` 

`class kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior(` _*args_ , _**kwargs_ `)` 

Focus behavior class. 

###### **Events** 

```
on_enter
```

Fired when mouse enters the bbox of the widget AND the widget is visible. 

```
on_leave
```

Fired when the mouse exits the widget AND the widget is visible. 

For more information, see in the `HoverBehavior` class documentation. Added in version 2.0.0. 

###### `state_layer_color` 

The color of the layer state. 

_`state_layer_color`_ is an `ColorProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `state_hover` 

The transparency level of the layer as a percentage when hovering. 

_`state_hover`_ is an `NumericProperty` and defaults to _0.08_ . 

###### `state_press` 

The transparency level of the layer as a percentage when pressed. 

_`state_press`_ is an `NumericProperty` and defaults to _0.12_ . 

###### `state_drag` 

The transparency level of the layer as a percentage when dragged. 

_`state_drag`_ is an `NumericProperty` and defaults to _0.16_ . 

```
icon_button_filled_opacity_value_disabled_container
icon_button_filled_opacity_value_disabled_icon
```

```
icon_button_tonal_opacity_value_disabled_container
```

```
icon_button_tonal_opacity_value_disabled_icon
```

```
icon_button_outlined_opacity_value_disabled_container
```

```
icon_button_outlined_opacity_value_disabled_line
icon_button_outlined_opacity_value_disabled_icon
icon_button_standard_opacity_value_disabled_icon
```

```
fab_button_opacity_value_disabled_container
fab_button_opacity_value_disabled_icon
button_filled_opacity_value_disabled_container
button_filled_opacity_value_disabled_icon
button_filled_opacity_value_disabled_text
```

**2.5. Behaviors** 

**665** 

**KivyMD, Release 2.0.1.dev0** 

```
button_tonal_opacity_value_disabled_container
button_tonal_opacity_value_disabled_icon
button_tonal_opacity_value_disabled_text
button_outlined_opacity_value_disabled_container
button_outlined_opacity_value_disabled_line
button_outlined_opacity_value_disabled_icon
button_outlined_opacity_value_disabled_text
button_elevated_opacity_value_disabled_container
button_elevated_opacity_value_disabled_icon
button_elevated_opacity_value_disabled_text
button_text_opacity_value_disabled_icon
button_text_opacity_value_disabled_text
label_opacity_value_disabled_text
card_filled_opacity_value_disabled_state_container
card_outlined_opacity_value_disabled_state_container
card_opacity_value_disabled_state_elevated_container
segmented_button_opacity_value_disabled_container
segmented_button_opacity_value_disabled_container_active
segmented_button_opacity_value_disabled_line
segmented_button_opacity_value_disabled_icon
segmented_button_opacity_value_disabled_text
chip_opacity_value_disabled_container
chip_opacity_value_disabled_text
chip_opacity_value_disabled_icon
switch_opacity_value_disabled_line
switch_opacity_value_disabled_container
switch_thumb_opacity_value_disabled_container
switch_opacity_value_disabled_icon
checkbox_opacity_value_disabled_container
list_opacity_value_disabled_container
list_opacity_value_disabled_leading_avatar
```

**Chapter 2. Contents** 

**666** 

**KivyMD, Release 2.0.1.dev0** 

```
text_field_filled_opacity_value_disabled_state_container
text_field_outlined_opacity_value_disabled_state_container
text_field_opacity_value_disabled_max_length_label
text_field_opacity_value_disabled_helper_text_label
text_field_opacity_value_disabled_hint_text_label
text_field_opacity_value_disabled_leading_icon
text_field_opacity_value_disabled_trailing_icon
```

```
text_field_opacity_value_disabled_line
```

`set_properties_widget()` _→_ None 

Fired _on_release/on_press/on_enter/on_leave_ events. 

`on_disabled(` _instance_ , _value_ `)` _→_ None 

Fired when the _disabled_ value changes. 

`on_enter()` _→_ None 

Fired when mouse enter the bbox of the widget. 

- `on_leave()` _→_ None 

Fired when the mouse goes outside the widget border. 

###### **2.5.12 Motion** 

**Use motion to make a UI expressive and easy to use.** 



Added in version 1.2.0. 

Classes of the _Motion_ type implement the display behavior of widgets such as dialogs, dropdown menu, snack bars, and so on. 

**2.5. Behaviors** 

**667** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.uix.behaviors.motion_behavior` 

```
classkivymd.uix.behaviors.motion_behavior.MotionBase
```

Base class for widget display movement behavior. 

###### `show_transition` 

The type of transition of the widget opening. 

_`show_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `show_duration` 

Duration of widget display transition. 

_`show_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `hide_transition` 

The type of transition of the widget closing. 

_`hide_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `hide_duration` 

Duration of widget closing transition. 

_`hide_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

`class kivymd.uix.behaviors.motion_behavior.MotionDropDownMenuBehavior(` _**kwargs_ `)` 

Base class for the dropdown menu movement behavior. 

For more information, see in the _`MotionBase`_ class documentation. 

###### `show_transition` 

The type of transition of the widget opening. 

_`show_transition`_ is a `StringProperty` and defaults to _‘out_back’_ . 

###### `show_duration` 

Duration of widget display transition. 

_`show_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

###### `hide_transition` 

The type of transition of the widget closing. 

_`hide_transition`_ is a `StringProperty` and defaults to _‘out_cubic’_ . 

`set_opacity()` _→_ None 

`set_scale()` _→_ None 

`on_dismiss()` _→_ None 

###### `on_open(` _*args_ `)` 

`on__opacity(` _instance_ , _value_ `)` 

`on__scale_x(` _instance_ , _value_ `)` 

`on__scale_y(` _instance_ , _value_ `)` 

**Chapter 2. Contents** 

**668** 

**KivyMD, Release 2.0.1.dev0** 

###### `class kivymd.uix.behaviors.motion_behavior.MotionExtendedFabButtonBehavior` 

Base class for extended Fab button movement behavior. 

For more information, see in the _`MotionBase`_ class documentation. 

###### `show_transition` 

The type of transition of the widget opening. 

_`show_transition`_ is a `StringProperty` and defaults to _‘out_circ’_ . 

###### `shift_transition` 

Text label transition. 

_`shift_transition`_ is a `StringProperty` and defaults to _‘out_sine’_ . 

###### `show_duration` 

Duration of widget display transition. 

_`show_duration`_ is a `NumericProperty` and defaults to _0.3_ . 

###### `hide_transition` 

The type of transition of the widget closing. 

_`hide_transition`_ is a `StringProperty` and defaults to _‘linear’_ . 

###### `hide_duration` 

Duration of widget closing transition. 

_`hide_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

`collapse(` _*args_ `)` _→_ None 

Collapses the button. 

`expand(` _*args_ `)` _→_ None 

Expands the button. 

`set_opacity_text_button(` _value: int_ `)` _→_ None 

```
classkivymd.uix.behaviors.motion_behavior.MotionDialogBehavior
```

Base class for dialog movement behavior. 

For more information, see in the _`ScaleBehavior MotionBase`_ classes documentation. 

###### `show_transition` 

The type of transition of the widget opening. 

_`show_transition`_ is a `StringProperty` and defaults to _‘out_expo’_ . 

###### `show_button_container_transition` 

The type of transition of the widget opening. 

_`show_button_container_transition`_ is a `StringProperty` and defaults to _‘out_circ’_ . 

###### `hide_transition` 

The type of transition of the widget opening. 

_`show_transition`_ is a `StringProperty` and defaults to _‘hide_transition’_ . 

###### `show_duration` 

Duration of widget display transition. 

_`show_duration`_ is a `NumericProperty` and defaults to _0.2_ . 

**2.5. Behaviors** 

**669** 

**KivyMD, Release 2.0.1.dev0** 

###### `on_dismiss(` _*args_ `)` 

Fired when a dialog closed. 

###### `on_open(` _*args_ `)` 

Fired when a dialog opened. 

```
classkivymd.uix.behaviors.motion_behavior.MotionTimePickerBehavior
```

Base class for time picker movement behavior. 

For more information, see in the `MotionPickerBehavior` class documentation. 

- `class kivymd.uix.behaviors.motion_behavior.MotionDatePickerBehavior` Base class for date picker movement behavior. 

For more information, see in the `MotionPickerBehavior` class documentation. 

- `class kivymd.uix.behaviors.motion_behavior.MotionShackBehavior` 

The base class for the behavior of the movement of snack bars. 

For more information, see in the _`MotionBase`_ class documentation. 

`on_dismiss(` _*args_ `)` 

Fired when a snackbar closed. 

`on_open(` _*args_ `)` 

Fired when a snackbar opened. 

###### **2.5.13 Background Color** 

**Note:** The following classes are intended for in-house use of the library. 

###### **API -** `kivymd.uix.behaviors.backgroundcolor_behavior` 

`class kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior(` _**kwarg_ `)` 

###### `background` 

Background image path. 

_`background`_ is a `StringProperty` and defaults to _‘’_ . 

###### `radius` 

Canvas radius. 

```
#Topleftcornerslice.
MDBoxLayout:
md_bg_color:app.theme_cls.primary_color
radius:[25,0,0,0]
```

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

**Chapter 2. Contents** 

**670** 

**KivyMD, Release 2.0.1.dev0** 

###### `md_bg_color` 

The background color of the widget ( `Widget` ) that will be inherited from the _`BackgroundColorBehavior`_ class. 

For example: 

```
Widget:
canvas:
Color:
rgba:0,1,1,1
Rectangle:
size:self.size
pos:self.pos
```

similar to code: 

```
<MyWidget@BackgroundColorBehavior>
md_bg_color:0,1,1,1
```

_`md_bg_color`_ is an `ColorProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `line_color` 

If a custom value is specified for the _line_color_ parameter, the border of the specified color will be used to border the widget: 

```
MDBoxLayout:
size_hint:.5,.2
md_bg_color:0,1,1,.5
line_color:0,0,1,1
radius:[24,]
```

Added in version 0.104.2. 

_`line_color`_ is an `ColorProperty` and defaults to _[0, 0, 0, 0]_ . 

###### `line_width` 

Border of the specified width will be used to border the widget. 

Added in version 1.0.0. 

_`line_width`_ is an `NumericProperty` and defaults to _1_ . 

###### `angle` 

###### `background_origin` 

- `on_md_bg_color(` _instance_ , _color: list | str_ `)` 

Fired when the values of _`md_bg_color`_ change. 

- `update_background_origin(` _instance_ , _pos: list_ `)` _→_ None 

Fired when the values of `pos` change. 

**2.5. Behaviors** 

**671** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.5.14 Stencil** 

Added in version 1.1.0. 

Base class for controlling the stencil instructions of the widget. 

**Note:** See Stencil instructions for more information. 

###### **Kivy** 

```
fromkivy.langimportBuilder
fromkivy.appimportApp
KV='''
Carousel:
Button:
size_hint:.9,.8
pos_hint:{"center_x":.5,"center_y":.5}
canvas.before:
StencilPush
RoundedRectangle:
pos:root.pos
size:root.size
StencilUse
canvas.after:
StencilUnUse
RoundedRectangle:
pos:root.pos
size:root.size
StencilPop
'''
classTest(App):
defbuild(self):
returnBuilder.load_string(KV)
Test().run()
```

**Chapter 2. Contents** 

**672** 

**KivyMD, Release 2.0.1.dev0** 

###### **KivyMD** 

```
fromkivy.langimportBuilder
fromkivymd.appimportMDApp
fromkivymd.uix.behaviorsimportStencilBehavior
fromkivymd.uix.fitimageimportFitImage
KV='''
#:importosos
#:importimages_pathkivymd.images_path
Carousel:
StencilImage:
size_hint:.9,.8
pos_hint:{"center_x":.5,"center_y":.5}
source:os.path.join(images_path,"logo","kivymd-icon-512.png")
'''
classStencilImage(FitImage,StencilBehavior):
pass
classTest(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
Test().run()
```

**API -** `kivymd.uix.behaviors.stencil_behavior` 

```
classkivymd.uix.behaviors.stencil_behavior.StencilBehavior
```

Base class for controlling the stencil instructions of the widget. 

```
radius
```

Canvas radius. 

Added in version 1.0.0. 

```
#Topleftcornerslice.
MDWidget:
radius:[25,0,0,0]
```

_`radius`_ is an `VariableListProperty` and defaults to _[0, 0, 0, 0]_ . 

**2.5. Behaviors** 

**673** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.6 Effects** 

###### **2.6.1 StiffScrollEffect** 

An Effect to be used with ScrollView to prevent scrolling beyond the bounds, but politely. 

A ScrollView constructed with StiffScrollEffect, eg. ScrollView(effect_cls=StiffScrollEffect), will get harder to scroll as you get nearer to its edges. You can scroll all the way to the edge if you want to, but it will take more finger-movement than usual. 

Unlike DampedScrollEffect, it is impossible to overscroll with StiffScrollEffect. That means you cannot push the contents of the ScrollView far enough to see what’s beneath them. This is appropriate if the ScrollView contains, eg., a background image, like a desktop wallpaper. Overscrolling may give the impression that there is some reason to overscroll, even if just to take a peek beneath, and that impression may be misleading. 

StiffScrollEffect was written by Zachary Spector. His other stuff is at: https://github.com/LogicalDash/ He can be reached, and possibly hired, at: zacharyspector@gmail.com 

###### **API -** `kivymd.effects.stiffscroll.stiffscroll` 

###### `class kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect(` _**kwargs_ `)` 

Kinetic effect class. See module documentation for more information. 

###### `drag_threshold` 

Minimum distance to travel before the movement is considered as a drag. 

_`drag_threshold`_ is an `NumericProperty` and defaults to _’20sp’_ . 

###### `min` 

Minimum boundary to stop the scrolling at. 

_`min`_ is an `NumericProperty` and defaults to _0_ . 

###### `max` 

Maximum boundary to stop the scrolling at. 

_`max`_ is an `NumericProperty` and defaults to _0_ . 

###### `max_friction` 

How hard should it be to scroll, at the worst? 

_`max_friction`_ is an `NumericProperty` and defaults to _1_ . 

###### `body` 

Proportion of the range in which you can scroll unimpeded. 

_`body`_ is an `NumericProperty` and defaults to _0.7_ . 

###### `scroll` 

Computed value for scrolling 

_`scroll`_ is an `NumericProperty` and defaults to _0.0_ . 

**Chapter 2. Contents** 

**674** 

**KivyMD, Release 2.0.1.dev0** 

###### `transition_min` 

The AnimationTransition function to use when adjusting the friction near the minimum end of the effect. 

_`transition_min`_ is an `ObjectProperty` and defaults to `kivy.animation.AnimationTransition` . 

###### `transition_max` 

The AnimationTransition function to use when adjusting the friction near the maximum end of the effect. 

_`transition_max`_ is an `ObjectProperty` and defaults to `kivy.animation.AnimationTransition` . 

###### `target_widget` 

The widget to apply the effect to. 

_`target_widget`_ is an `ObjectProperty` and defaults to `None` . 

###### `displacement` 

The absolute distance moved in either direction. 

_`displacement`_ is an `NumericProperty` and defaults to _0_ . 

###### `update_velocity(` _dt_ `)` 

Before actually updating my velocity, meddle with `self.friction` to make it appropriate to where I’m at, currently. 

###### `on_value(` _*args_ `)` 

Prevent moving beyond my bounds, and update `self.scroll` 

###### `start(` _val_ , _t=None_ `)` 

   - Start movement with `self.friction` = `self.base_friction` 

- `update(` _val_ , _t=None_ `)` 

Reduce the impact of whatever change has been made to me, in proportion with my current friction. 

`stop(` _val_ , _t=None_ `)` 

Work out whether I’ve been flung. 

###### **2.7 Changelog** 

###### **2.7.1 Unreleased** 

See on GitHub: branch master | compare 2.0.0/master 

###### `pip install https://github.com/kivymd/KivyMD/archive/master.zip` 

- Issues closed: 

- [fix(behaviors): resolve magic behavior effects on touch and MDIconButton] Issue #1891 

- New feature: 

- [PR 1893] Integrate _MaterialShape_ support to _FitImage_ widget 

**2.7. Changelog** 

**675** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.2 2.0.0** 

See on GitHub: tag 2.0.0 | compare 2.0.0/master 

```
pipinstallkivymd==2.0.0
```

- Bug fixes and other minor improvements. 

- [commit b34b07f] Fix elevation properties. 

- [commit cb01c01] Fixed an infinite loop when typing text fast in the _MDTextfield_ widget. 

- Issues closed: 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- [issue 1880] Issue #1880 

- [issue 1531] Issue #1531 

- [issue 1442] Issue #1442 

- [issue 1414] Issue #1414 

- [issue 1248] Issue #1248 

- [issue 1193] Issue #1193 

- [issue 1123] Issue #1123 

- [issue 849] Issue #849 

- [issue 1415] Issue #1415 

- [issue 1838] Issue #1838 

- [issue 1794] Issue #1794 

- [issue 1763] Issue #1763 

- [issue 1758] Issue #1758 

- [issue 1851] Issue #1851 

- [issue 1737] Issue #1737 

- [issue 1634] Issue #1634 

- [issue 1638] Issue #1638 

**Chapter 2. Contents** 

**676** 

**KivyMD, Release 2.0.1.dev0** 

- [issue 1637] Issue #1637 

- [issue 1608] Issue #1608 

- [issue 1609] Issue #1609 

- [issue 1515] Issue #1515 

- [issue 1586] Issue #1586 

- [issue 1472] Issue #1472 

- [issue 1536] Issue #1536 

- [issue 1536] Issue #1593 

- [issue 1493] Issue #1493 

- [issue 1493] Issue #1600 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- New feature: 

- [commit 25f242e] Add the feature to use icons from custom fonts. 

- [compare] Add supports _Google’s Material Design 3_ and the _Material You_ concept. 

- [PR 1584] Implement bitmap scale down 

- [PR 1854] New _M3_ ripple effect 

- [PR 1825] New widget _MDLoadingIndicator_ 

- [PR 1825] New widget _MDCarousel_ 

- [PR 1629] Implement material design specifications for _MDScrollView_ 

- [PR 1673] Add material transition for _MDScreenManager_ 

- API break. Implement declarative style for all KivyMD widgents. 

**2.7. Changelog** 

**677** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.3 2.0.0** 

See on GitHub: tag 2.0.0 | compare 2.0.0/master 

```
pipinstallkivymd==2.0.0
```

- Bug fixes and other minor improvements. 

- [commit b34b07f] Fix elevation properties. 

- [commit cb01c01] Fixed an infinite loop when typing text fast in the _MDTextfield_ widget. 

- Issues closed: 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- [issue 1880] Issue #1880 

- [issue 1531] Issue #1531 

- [issue 1442] Issue #1442 

- [issue 1414] Issue #1414 

- [issue 1248] Issue #1248 

- [issue 1193] Issue #1193 

- [issue 1123] Issue #1123 

- [issue 849] Issue #849 

- [issue 1415] Issue #1415 

- [issue 1838] Issue #1838 

- [issue 1794] Issue #1794 

- [issue 1763] Issue #1763 

- [issue 1758] Issue #1758 

- [issue 1851] Issue #1851 

- [issue 1737] Issue #1737 

- [issue 1634] Issue #1634 

- [issue 1638] Issue #1638 

**Chapter 2. Contents** 

**678** 

**KivyMD, Release 2.0.1.dev0** 

- [issue 1637] Issue #1637 

- [issue 1608] Issue #1608 

- [issue 1609] Issue #1609 

- [issue 1515] Issue #1515 

- [issue 1586] Issue #1586 

- [issue 1472] Issue #1472 

- [issue 1536] Issue #1536 

- [issue 1536] Issue #1593 

- [issue 1493] Issue #1493 

- [issue 1493] Issue #1600 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- New feature: 

- [commit 25f242e] Add the feature to use icons from custom fonts. 

- [compare] Add supports _Google’s Material Design 3_ and the _Material You_ concept. 

- [PR 1584] Implement bitmap scale down 

- [PR 1854] New _M3_ ripple effect 

- [PR 1825] New widget _MDLoadingIndicator_ 

- [PR 1825] New widget _MDCarousel_ 

- [PR 1629] Implement material design specifications for _MDScrollView_ 

- [PR 1673] Add material transition for _MDScreenManager_ 

- API break. Implement declarative style for all KivyMD widgents. 

**2.7. Changelog** 

**679** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.4 2.0.0** 

See on GitHub: tag 2.0.0 | compare 2.0.0/master 

```
pipinstallkivymd==2.0.0
```

- Bug fixes and other minor improvements. 

- [commit b34b07f] Fix elevation properties. 

- [commit cb01c01] Fixed an infinite loop when typing text fast in the _MDTextfield_ widget. 

- Issues closed: 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- [issue 1880] Issue #1880 

- [issue 1531] Issue #1531 

- [issue 1442] Issue #1442 

- [issue 1414] Issue #1414 

- [issue 1248] Issue #1248 

- [issue 1193] Issue #1193 

- [issue 1123] Issue #1123 

- [issue 849] Issue #849 

- [issue 1415] Issue #1415 

- [issue 1838] Issue #1838 

- [issue 1794] Issue #1794 

- [issue 1763] Issue #1763 

- [issue 1758] Issue #1758 

- [issue 1851] Issue #1851 

- [issue 1737] Issue #1737 

- [issue 1634] Issue #1634 

- [issue 1638] Issue #1638 

**Chapter 2. Contents** 

**680** 

**KivyMD, Release 2.0.1.dev0** 

- [issue 1637] Issue #1637 

- [issue 1608] Issue #1608 

- [issue 1609] Issue #1609 

- [issue 1515] Issue #1515 

- [issue 1586] Issue #1586 

- [issue 1472] Issue #1472 

- [issue 1536] Issue #1536 

- [issue 1536] Issue #1593 

- [issue 1493] Issue #1493 

- [issue 1493] Issue #1600 

- [issue 1852] Issue #1852 

- [issue 1853] Issue #1853 

- [issue 1857] Issue #1857 

- [issue 1848] Issue #1848 

- [issue 1843] Issue #1843 

- [issue 1839] Issue #1839 

- [issue 1864] Issue #1864 

- [issue 1871] Issue #1871 

- [issue 1695] Issue #1695 

- [issue 1598] Issue #1598 

- [issue 1803] Issue #1803 

- New feature: 

- [commit 25f242e] Add the feature to use icons from custom fonts. 

- [compare] Add supports _Google’s Material Design 3_ and the _Material You_ concept. 

- [PR 1584] Implement bitmap scale down 

- [PR 1854] New _M3_ ripple effect 

- [PR 1825] New widget _MDLoadingIndicator_ 

- [PR 1825] New widget _MDCarousel_ 

- [PR 1629] Implement material design specifications for _MDScrollView_ 

- [PR 1673] Add material transition for _MDScreenManager_ 

- API break. Implement declarative style for all KivyMD widgents. 

**2.7. Changelog** 

**681** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.5 1.1.1** 

See on GitHub: tag 1.1.1 | compare 1.0.2/1.1.1 

```
pipinstallkivymd==1.1.1
```

- Bug fixes and other minor improvements. 

- Add closing_interval parameter to MDCardSwipe class. 

- Add implementation of elevation behavior on shaders. 

- Add validator property to MDTextField class: the type of text field for entering Email, time, etc. Automatically sets the type of the text field as _error_ if the user input does not match any of the set validation types. 

- Add theme_style_switch_animation property to animate the colors of the application when switching the color scheme of the application _(‘Dark/light’)_ . 

- Add theme_style_switch_animation_duration property to duration of the animation of switching the color scheme of the application _(“Dark/ light”)_ . 

- Fix memory leak when dynamically adding and removing _KivyMD_ widgets. 

- Fix slide transition MDBottomNavigation direction. 

- Add a default value for the icon attribute of MDApp class. 

- Add new properties to MDFileManager class: 

   - icon_selection_button - icon that will be used on the directory selection button; 

   - background_color_selection_button - background color of the current directory/path selection button; 

   - background_color_toolbar - background color of the file manager toolbar; 

   - icon_color - color of the folder icon when the _preview_ property is set to False; 

- Add binds to MDFloatingActionButtonSpeedDial individual buttons; 

- Add functionality for using multiple heroes. 

- Add shadow_softness_size attribute (value of the softness of the shadow) to CommonElevationBehavior class. 

- Optimize of MDDatePicker widget. 

###### **2.7.6 1.0.2** 

See on GitHub: tag 1.0.2 | compare 1.0.1/1.0.2 

```
pipinstallkivymd==1.0.2
```

- Bug fixes and other minor improvements. 

- Added a button to copy the code to the documentation. 

- Added the feature to view code examples of documentation in imperative and declarative styles. 

- Added console scripts for developer tools. 

**Chapter 2. Contents** 

**682** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.7 1.0.1** 

See on GitHub: tag 1.0.1 | compare 1.0.0/1.0.1 

```
pipinstallkivymd==1.0.1
```

- Bug fixes and other minor improvements. 

- Fix https://github.com/kivymd/KivyMD/issues/1305. 

###### **2.7.8 1.0.0** 

See on GitHub: tag 1.0.0 | compare 0.104.2/1.0.0 

```
pipinstallkivymd==1.0.0
```

- Bug fixes and other minor improvements. 

- Added _ImageLeftWidgetWithoutTouch_ , _ImageRightWidgetWithoutTouch_ , _IconRightWidgetWithoutTouch_ , _IconLeftWidgetWithoutTouch_ classes to _kivymd/uix/list.py_ module; 

- Added MDStepper component; 

- Added a feature, show_disks to the MDFileManager class, that allows you to display the disks and folders contained in them; 

- Added animation_tooltip_dismiss function and on_dismiss event to MDTooltip class; 

- Added MDColorPicker component; 

- Added new transition package - a set of classes for implementing transitions between application screens; 

- Now all modules from the uix directory are packages; 

- Type hints have been added to the source code of the KivyMD library; 

- Added divider_color attribute to BaseListItem class; 

- Added load_all_kv_files method to MDApp class; 

- Added Templates package - base classes for controlling the scale, rotation of the widget, etc.; 

- Added kivymd/tools/patterns package - scripts for creating projects with design patterns; 

- _FitImage_ widget move from _kivymd.utils_ to _kivymd.uix.fitimage_ ; 

- Added background_color_header, background_color_cell, background_color_selected_cell, added methods for adding/removing rows to a common table to MDDataTable widget; 

- Added method for update rows to MDDataTable class; 

- Delete _kivymd/utils/hot_reload_viewer.py_ ; 

- Added kivymd/tools/hotreload package; 

- Added _top_ value to position parameter of MDDropdownMenu class; 

- Added get_current_tab method to MDTabs class; 

- Added the feature to automatically create a virtual environment when creating a project using the kivymd.tools.patterns.create_project tool; 

- Added the feature to use the left_icon for MDTextField text fields; 

- The design and behavior of the MDChip widget is close to the material design spec; 

**2.7. Changelog** 

**683** 

**KivyMD, Release 2.0.1.dev0** 

- Added the feature to set the thickness of the MDProgressBar class; 

- Added localization support when creating a project using the create_project tool; 

- Added support _Material Design v3_ ; 

- Added support badge icon to MDIcon class; 

- Added the feature to use a radius for the _BaseListItem_ class; 

- MDFloatingActionButton class configured according to M3 style; 

- Ripple animation for round buttons customized to material design standards; 

- Fix Warning, too much iteration done before the next frame for button classes; 

- Added FadingEdgeEffect class 

- Added MDSliverAppBar widget; 

- Added the feature to use custom icons and font name for the MDBottomNavigation class; 

- Rename _MDToolbar_ to MDTopAppBar class; 

- The overflow behavior from the _ActionBar_ class of the _Kivy_ framework has been added to the _MDTopAppBar_ class; 

- Add _shift_right_ and _shift_right_ attributes to MDTooltip class; 

- Fixed the size of the MDIconButton icon when changing icon_size on mobile devices; 

- Add new MDSegmentedControl widget; 

- Add _on_release/on_press_ events to MDSmartTile class; 

- Add _mipmap_ property to FitImage class; 

- Added the feature to use Hero animation; 

- Added MDResponsiveLayout layout; 

- Added add_view utility; 

- Added the feature to create widgets in declarative programming style; 

###### **2.7.9 0.104.2** 

See on GitHub: tag 0.104.2 | compare 0.104.1/0.104.2 

```
pipinstallkivymd==0.104.2
```

- Bug fixes and other minor improvements. 

- Add _HotReloadViewer_ class 

- Added features to _Snackbar_ class: use padding, set custom button color, elevation 

- Add _MDToggleButton_ class 

- Change to _Material Design Baseline_ dark theme spec 

- Fix _ReferenceError: weakly-referenced object no longer exists_ when start demo application 

- Changed the default value for the _theme_text_color_ parameter in the _BaseButton_ class (to the value _“Primary”_ ) 

- Fix setting of the _text_color_normal_ and _text_color_active_ parameters - earlier their values did not affect anything 

**Chapter 2. Contents** 

**684** 

**KivyMD, Release 2.0.1.dev0** 

- Fixed the length of the right edge of the border in relation to the hint text when the _MDTextField_ is in the _rectangle_ mode 

- Add _get_tab_list_ method to _MDTabs_ class 

- Add hover behavior when using _MDDropdownMenu_ class 

- Added the feature to use the _FitImage_ component to download images from the network 

- The _elevation_ value for _RectangularElevationBehavior_ and _CircularElevationBehavior_ classes after pressing was always set to _2_ - fixed 

- Methods that implement the ripple effect have always been called twice - fixed 

- The _SmartTile_ class now uses the _FitImage_ class to display images instead of the _Image_ class 

- Removed dependency on _PIL_ library 

- Add _hint_bg_color_ , _hint_text_color_ , _hint_radius_ attributes to _MDSlider_ class 

- Delete _progressloader.py_ 

- Delete _context_menu.py_ 

- Added the feature to control the properties of menu items during creation in _MDDropdownMenu_ class 

- Added the feature to change the number of buttons after creating the _MDFloatingActionButtonSpeedDial_ object 

- Added the feature to set the _font_name_ property for the _MDTabsLabel_ class 

- Add _MDCarousel_ class 

- Delete _kivymd/uix/useranimationcard.py_ 

- Added usage types for _MDNavigationDrawer_ class: _modal/standard_ 

- Added stencil instructions to the _FitImage_ class canvas 

- Added _on_ref_press_ and _switch_tab_ methods to _MDTabs_ class 

- Added _on_release_ method for menu item events instead of callback method to _MDDropdownMenu_ class 

- Added _palette_ attribute - the feature to change the color of the _MDSpinner_ when changing rotation cycles 

- Added the feature to change the border color of the _MDRectangleFlatIconButton_ class 

- Add _MDRelativeLayout_ class 

- Added the feature to use radius for _MDNavigationDrawer_ corners 

- Removed _UserAnimationCard_ class 

- Added feature to set background color for _MDDialog_ class 

- Added _MDNavigationRail_ component 

- Added _MDSwiper_ component 

- Added ripple effect to _MDTabs_ class 

- Added the feature to set toast positions on an _Android_ device 

- Added of tooltips to _MDToolbar_ icons 

- Fixed _MDBottomAppBar_ notch transparency 

- Updated _MDDatePicker_ class to material design specification. 

- Updated _MDTimePicker_ class to material design specification. 

- Elevation behavior redesign to comply with the material design specification. 

**2.7. Changelog** 

**685** 

**KivyMD, Release 2.0.1.dev0** 

- Removed the _vendor_ package. 

- Added the feature to use a class instance ( _Kivy_ or _KivyMD_ widget), which will be added to the _MDDropdownMenu_ class menu header. 

###### **2.7.10 0.104.1** 

See on GitHub: tag 0.104.1 | compare 0.104.0/0.104.1 

```
pipinstallkivymd==0.104.1
```

- Bug fixes and other minor improvements. 

- Added _MDGridLayout_ and _MDBoxLayout_ classes 

- Add _TouchBehavior_ class 

- Add _radius_ parameter to _BackgroundColorBehavior_ class 

- Add _MDScreen_ class 

- Add _MDFloatLayout_ class 

- Added a _MDTextField_ with _fill_ mode 

- Added a shadow, increased speed of opening, added the feature to control the position of the _MDDropdownMenu_ class 

- The _MDDropDownItem_ class is now a regular element, such as a button 

- Added the ability to use the texture of the icon on the right in any _MDTextField_ classes 

- Added the feature to use ripple and focus behavior in _MDCard_ class 

- _MDDialogs_ class redesigned to meet material design requirements 

- Added _MDDataTable_ class 

###### **2.7.11 0.104.0** 

See on GitHub: tag 0.104.0 | compare 0.103.0/0.104.0 

```
pipinstallkivymd==0.104.0
```

- Fixed bug in `kivymd.uix.expansionpanel.MDExpansionPanel` if, with the panel open, without closing it, try to open another panel, then the chevron of the first panel remained open. 

- The `kivymd.uix.textfield.MDTextFieldRound` class is now directly inherited from the `kivy.uix. textinput.TextInput` class. 

- Removed `kivymd.uix.textfield.MDTextFieldClear` class. 

- `kivymd.uix.navigationdrawer.NavigationLayout` allowed to add `kivymd.uix.toolbar.MDToolbar` class. 

- Added feature to control range of dates to be active in `kivymd.uix.picker.MDDatePicker` class. 

- Updated `kivymd.uix.navigationdrawer.MDNavigationDrawer` realization. 

- Removed `kivymd.uix.card.MDCardPost` class. 

- Added `kivymd.uix.card.MDCardSwipe` class. 

**Chapter 2. Contents** 

**686** 

**KivyMD, Release 2.0.1.dev0** 

- Added _switch_tab_ method for switching tabs to `kivymd.uix.bottomnavigation.MDBottomNavigation` class. 

- Added feature to use panel type in the `kivymd.uix.expansionpanel.MDExpansionPanel` class: `kivymd.uix.expansionpanel.MDExpansionPanelOneLine` , `kivymd.uix.expansionpanel. MDExpansionPanelTwoLine` or `kivymd.uix.expansionpanel.MDExpansionPanelThreeLine` . 

- Fixed panel opening animation in the `kivymd.uix.expansionpanel.MDExpansionPanel` class. 

- Delete _kivymd.uix.managerswiper.py_ 

- Add _MDFloatingActionButtonSpeedDial_ class 

- Added the feature to create text on tabs using markup, thereby triggering the _on_ref_press_ event in the _MDTabsLabel_ class 

- Added _color_indicator_ attribute to set custom indicator color in the _MDTabs_ class 

- Added the feature to change the background color of menu items in the _BaseListItem_ class 

- Add _MDTapTargetView_ class 

###### **2.7.12 0.103.0** 

See on GitHub: tag 0.103.0 | compare 0.102.1/0.103.0 

```
pipinstallkivymd==0.103.0
```

- Fix _MDSwitch_ size according to _material design_ guides 

- Fix MDSwitch’s thumb position when size changes 

- Fix position of the icon relative to the right edge of the _MDChip_ class on mobile devices 

- Updated _MDBottomAppBar_ class. 

- Updated _navigationdrawer.py_ 

- Added _on_tab_switch_ method that is called when switching tabs ( _MDTabs_ class) 

- Added _FpsMonitor_ class 

- Added _fitimage.py_ - feature to automatically crop a _Kivy_ image to fit your layout 

- Added animation when changing the action button position mode in _MDBottomAppBar_ class 

- Delete _fanscreenmanager.py_ 

- Bug fixes and other minor improvements. 

###### **2.7.13 0.102.1** 

See on GitHub: tag 0.102.1 | compare 0.102.0/0.102.1 

```
pipinstallkivymd==0.102.1
```

- Implemented the ability [Backdrop](https://material.io/components/backdrop) 

- Added _MDApp_ class. Now app object should be inherited from _kivymd.app.MDApp_ . 

- Added _MDRoundImageButton_ class. 

- Added _MDTooltip_ class. 

**2.7. Changelog** 

**687** 

**KivyMD, Release 2.0.1.dev0** 

- Added _MDBanner_ class. 

- Added hook for _PyInstaller_ (add _hookspath=[kivymd.hooks_path]_ ). 

- Added examples of _spec_ files for building [Kitchen Sink demo](https://github.com/kivymd/KivyMD/tree/ master/demos/kitchen_sink). 

- Added some features to _MDProgressLoader_ . 

- Added feature to preview the current value of _MDSlider_ . 

- Added feature to use custom screens for dialog in _MDBottomSheet_ class. 

- Removed _MDPopupScreen_ . 

- Added [ _studies_ ](https://github.com/kivymd/KivyMD/tree/master/demos/kitchen_sink/studies) directory for demos in Material Design. 

- Bug fixes and other minor improvements. 

###### **2.7.14 0.102.0** 

See on GitHub: tag 0.102.0 | compare 0.101.8/0.102.0 

```
pipinstallkivymd==0.102.0
```

- Moved _kivymd.behaviors_ to _kivymd.uix.behaviors_ . 

- Updated [Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) (v4.5.95). 

- Added _blank_ icon to _icon_definitions_ . 

- Bug fixes and other minor improvements. 

###### **2.7.15 0.101.8** 

See on GitHub: tag 0.101.8 | compare 0.101.7/0.101.8 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.8.zip
```

- Added _uix_ and _behaviors_ folder to _package_data_ . 

###### **2.7.16 0.101.7** 

See on GitHub: tag 0.101.7 | compare 0.101.6/0.101.7 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.7.zip
```

- Fixed colors and position of the buttons in the _Buttons_ demo screen ([Kitchen Sink demo](https://github.com/ kivymd/KivyMD/tree/master/demos/kitchen_sink)). 

- Displaying percent of loading kv-files ([Kitchen Sink demo](https://github.com/kivymd/KivyMD/tree/master/ demos/kitchen_sink)). 

**Chapter 2. Contents** 

**688** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.17 0.101.6** 

See on GitHub: tag 0.101.6 | compare 0.101.5/0.101.6 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.6.zip
```

- Fixed _NameError: name ‘MDThemePicker’ is not defined_ . 

###### **2.7.18 0.101.5** 

See on GitHub: tag 0.101.5 | compare 0.101.4/0.101.5 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.5.zip
```

- Added feature to see source code of current example ([Kitchen Sink demo](https://github.com/kivymd/KivyMD/ tree/master/demos/kitchen_sink)). 

- Added names of authors of this fork ([Kitchen Sink demo](https://github.com/kivymd/KivyMD/tree/master/ demos/kitchen_sink)). 

- Bug fixes and other minor improvements. 

###### **2.7.19 0.101.4** 

See on GitHub: tag 0.101.4 | compare 0.101.3/0.101.4 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.4.zip
```

- Bug fixes and other minor improvements. 

###### **2.7.20 0.101.3** 

See on GitHub: tag 0.101.3 | compare 0.101.2/0.101.3 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.3.zip
```

- Bug fixes and other minor improvements. 

###### **2.7.21 0.101.2** 

See on GitHub: tag 0.101.2 | compare 0.101.1/0.101.2 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.2.zip
```

- Bug fixes and other minor improvements. 

**2.7. Changelog** 

**689** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.22 0.101.1** 

See on GitHub: tag 0.101.1 | compare 0.101.0/0.101.1 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.1.zip
```

- Bug fixes and other minor improvements. 

###### **2.7.23 0.101.0** 

See on GitHub: tag 0.101.0 | compare 0.100.2/0.101.0 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.101.0.zip
```

- Added _MDContextMenu_ class. 

- Added _MDExpansionPanel_ class. 

- Removed _MDAccordion_ and _MDAccordionListItem_ . Use _MDExpansionPanel_ instead. 

- Added _HoverBehavior_ class by [Olivier POYEN](https://gist.github.com/opqopq/15c707dc4cffc2b6455f). 

- Added markup support for buttons. 

- Added _duration_ property to _Toast_ . 

- Added _TextInput_ ’s events and properties to _MDTextFieldRound_ . 

- Added feature to resize text field 

- Added color property to _MDSeparator_ class 

- Added [tool](https://github.com/kivymd/KivyMD/blob/master/kivymd/tools/update_icons.py) for updating [Iconic font](https://github.com/Templarian/MaterialDesign-Webfont). 

- Updated [Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) (v4.3.95). 

- Added new examples for [Kitchen Sink demo](https://github.com/kivymd/KivyMD/tree/master/demos/kitchen_ sink). 

- Bug fixes and other minor improvements. 

###### **2.7.24 0.100.2** 

See on GitHub: tag 0.100.2 | compare 0.100.1/0.100.2 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.100.2.zip
```

- [Black](https://github.com/psf/black) formatting. 

**Chapter 2. Contents** 

**690** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.25 0.100.1** 

See on GitHub: tag 0.100.1 | compare 0.100.0/0.100.1 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.100.1.zip
```

- _MDUserAnimationCard_ uses _Image_ instead of _AsyncImage_ . 

###### **2.7.26 0.100.0** 

See on GitHub: tag 0.100.0 | compare 0.99.99/0.100.0 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.100.0.zip
```

- Added feature to change color for _MDStackFloatingButtons_ . 

###### **2.7.27 0.99.99.01** 

See on GitHub: tag 0.99.99.01 | compare 0.99.98/0.99.99.01 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.99.01.zip
```

- Fixed _MDNavigationDrawer.use_logo_ . 

###### **2.7.28 0.99.99** 

See on GitHub: tag 0.99.99 | compare 0.99.99.01/0.99.99 

###### `pip install https://github.com/kivymd/KivyMD/archive/0.99.99.zip` 

- Added _icon_color_ property for _NavigationDrawerIconButton_ . 

###### **2.7.29 0.99.98** 

See on GitHub: tag 0.99.98 | compare 0.99.97/0.99.98 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.98.zip
```

- Added _MDFillRoundFlatIconButton_ class. 

###### **2.7.30 0.99.97** 

See on GitHub: tag 0.99.97 | compare 0.99.96/0.99.97 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.97.zip
```

- Fixed _Spinner_ animation. 

**2.7. Changelog** 

**691** 

**KivyMD, Release 2.0.1.dev0** 

###### **2.7.31 0.99.96** 

See on GitHub: tag 0.99.96 | compare 0.99.95/0.99.96 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.96.zip
```

- Added _asynckivy_ module by [Natt¯osai Mit¯o](https://github.com/gottadiveintopython/asynckivy). 

###### **2.7.32 0.99.95** 

See on GitHub: tag 0.99.95 | compare 0.99.94/0.99.95 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.95.zip
```

- Added function to create a round image in _kivymd/utils/cropimage.py_ module. 

- Added _MDCustomRoundIconButton_ class. 

- Added demo application [Account Page](https://www.youtube.com/watch?v=dfUOwqtYoYg) for [Kitchen Sink demo](https://github.com/kivymd/KivyMD/tree/master/demos/kitchen_sink). 

###### **2.7.33 0.99.94** 

See on GitHub: tag 0.99.94 | compare 0.99.93/0.99.94 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.94.zip
```

- Added __no_ripple_effect_ property to _BaseListItem_ class. 

- Added check to use _ripple effect_ in _RectangularRippleBehavior_ class. 

- [Disabled](https://www.youtube.com/watch?v=P_9oSx0Pz_U) using _ripple effect_ in _MDAccordionListItem_ class. 

###### **2.7.34 0.99.93** 

See on GitHub: tag 0.99.93 | compare 0.99.92/0.99.93 

```
pipinstallhttps://github.com/kivymd/KivyMD/archive/0.99.93.zip
```

- Updated [Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) (v3.6.95). 

###### **2.7.35 0.99.92** 

See on GitHub: tag 0.99.92 | compare 0.99.91/0.99.92 

###### `pip install https://github.com/kivymd/KivyMD/archive/0.99.92.zip` 

- Removed automatic change of text field length in _MDTextFieldRound_ class. 

**Chapter 2. Contents** 

**692** 





<!-- Start of picture text -->
/ r = = . Men, .<br>Lounge | ,a ee (Me<br>i|7Ve. iitBeSr ean> aP x =<¢ > ev<br>. ]<br>iB d P<br>peBlue Bottle Coffee © : .<br>46 ok ok ot 359 reviews »$ Chronomart $380<br>Coffee Shop<br>= FEYERT Logo Office Lady Fashion<br>& * ® ‘SmallStrap WristDial Stainless Watch  Steel Leather<br>Trendy cafe chain offering upscale cottee drink & . 7) More information v<br>pastries, plus beans & brewing equipment<br>- Beautiful 3D Design Dial, with '7 marking<br>Q 315 Linden st, san Francisco, CA 94102 -“Durable Comfortablestainless Soft Leathersteel buckle Watch Band<br>© Open today: 7:00 AM. - 6:00 PIM ; -= Comfortable Precise Quartz for movement Everyday Wear for accurate ti<br>lySH TworlneSecondary temtext withhereavatar WARRANTY- For defective INFORMATION:products, buyers may return<br>. the Zalora PH return period (within 30 days<br>"]] THIS WARRANTY DOES NOT COVER:<br>- Damage resulting from impact, accidents, Menu:<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

Is a collection of Material Design compliant widgets for use with, Kivy cross-platform graphical framework a framework for cross-platform, touch-enabled graphical applications. The project’s goal is to approximate Google’s Material Design spec as close as possible without sacrificing ease of use. 

This library is a fork of the KivyMD project. We found the strength and brought this project to a new level. 

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too. 

###### **2.9.2 API -** `kivymd` 

###### `kivymd.path` 

Path to KivyMD package directory. 

###### `kivymd.fonts_path` 

Path to fonts directory. 

###### `kivymd.images_path` 

Path to images directory. 

###### `kivymd.uix_path` 

Path to uix directory. 

###### `kivymd.glsl_path` 

Path to glsl directory. 

###### **2.9.3 Submodules** 

**Register KivyMD widgets to use without import.** 

Register KivyMD widgets to use without import. 

###### **API -** `kivymd.factory_registers` 

```
kivymd.factory_registers.register
```

###### **Material Resources** 

###### **API -** `kivymd.material_resources` 

```
kivymd.material_resources.dp
```

```
kivymd.material_resources.DEVICE_IOS
```

```
kivymd.material_resources.DEVICE_TYPE='desktop'
```

**Chapter 2. Contents** 

**694** 

**KivyMD, Release 2.0.1.dev0** 

###### **Effects** 

**API -** `kivymd.effects` 

**Submodules** 

**kivymd.effects.stiffscroll** 

**API -** `kivymd.effects.stiffscroll` 

###### **Submodules** 

**kivymd.toast** 

**API -** `kivymd.toast` 

**Submodules** 

**AndroidToast** 

**Native implementation of toast for Android devices.** 

_`# Will be automatically used native implementation of the toast # if your application is running on an Android device. # On desktop use`  MDSnackbar < https://kivymd.readthedocs.io/en/latest/components/` ` ˓→_ _`snackbar/> _`_ `from kivy.lang import Builder from kivymd.toast import toast from kivymd.app import MDApp KV = ''' MDScreen: md_bg_color: self.theme_cls.backgroundColor MDButton: pos_hint:{"center_x": .5, "center_y": .5} on_press: app.show_toast() MDButtonText: text: "Make toast" '''` 

(continues on next page) 

**2.9. KivyMD** 

**695** 

**KivyMD, Release 2.0.1.dev0** 

(continued from previous page) 

```
classExample(MDApp):
defbuild(self):
returnBuilder.load_string(KV)
defshow_toast(self):
toast("HelloWorld",True,80,200,0)
Example().run()
```

**API -** `kivymd.toast.androidtoast` 

`kivymd.toast.androidtoast.toast(` _text_ , _length_long=False_ , _gravity=0_ , _y=0_ , _x=0_ `)` Displays a toast. 

###### **Parameters** 

- `length_long` – the amount of time (in seconds) that the toast is visible on the screen; 

- `text` – text to be displayed in the toast; 

- `length_long` – duration of the toast, if _True_ the toast will last 2.3s but if it is _False_ the toast will last 3.9s; 

- `gravity` – refers to the toast position, if it is 80 the toast will be shown below, if it is 40 the toast will be displayed above; 

- `y` – refers to the vertical position of the toast; 

- `x` – refers to the horizontal position of the toast; 

Important: if only the text value is specified and the value of the _gravity_ , _y_ , _x_ parameters is not specified, their values will be 0 which means that the toast will be shown in the center. 

###### **kivymd.tools** 

**API -** `kivymd.tools` 

###### **Submodules** 

###### **kivymd.tools.argument_parser** 

**API -** `kivymd.tools.argument_parser` 

`class kivymd.tools.argument_parser.ArgumentParserWithHelp(` _prog=None_ , _usage=None_ , 

_description=None_ , _epilog=None_ , _parents=[]_ , _formatter_class=HelpFormatter_ , _prefix_chars='-'_ , _fromfile_prefix_chars=None_ , _argument_default=None_ , _conflict_handler='error'_ , _add_help=True_ , _allow_abbrev=True_ , _exit_on_error=True_ `)` 

**Chapter 2. Contents** 

**696** 

**KivyMD, Release 2.0.1.dev0** 

Object for parsing command line strings into Python objects. 

###### **Keyword Arguments:** 

- **prog – The name of the program (default:** `os.path.basename(sys.argv[0])` ) 

- usage – A usage message (default: auto-generated from arguments) 

- description – A description of what the program does 

- epilog – Text following the argument descriptions 

- parents – Parsers whose arguments should be copied into this one 

- formatter_class – HelpFormatter class for printing help messages 

- prefix_chars – Characters that prefix optional arguments 

- **fromfile_prefix_chars – Characters that prefix files containing** additional arguments 

- argument_default – The default value for all arguments 

- conflict_handler – String indicating how to handle conflicts 

- add_help – Add a -h/-help option 

- allow_abbrev – Allow long options to be abbreviated unambiguously 

- **exit_on_error – Determines whether or not ArgumentParser exits with** error info when an error occurs 

`parse_args(` _args=None_ , _namespace=None_ `)` 

`error(` _message_ `)` 

error(message: string) 

Prints a usage message incorporating the message to stderr and exits. 

If you override this in a subclass, it should not return – it should either exit or raise an exception. 

```
format_help()
```

###### **kivymd.tools.hotreload** 

**API -** `kivymd.tools.hotreload` 

###### **Submodules** 

###### **HotReload** 

Added in version 1.0.0. 

**2.9. KivyMD** 

**697** 



**KivyMD, Release 2.0.1.dev0** 

###### **FIXME** 

- On Windows, hot reloading of Python files may not work; 

###### **API -** `kivymd.tools.hotreload.app` 

```
kivymd.tools.hotreload.app.original_argv
```

```
kivymd.tools.hotreload.app.monotonic
```

```
kivymd.tools.hotreload.app.PY3=True
```

```
classkivymd.tools.hotreload.app.ExceptionClass
```

Base handler that catches exceptions in `runTouchApp()` . You can subclass and extend it as follows: 

```
classE(ExceptionHandler):
defhandle_exception(self,inst):
Logger.exception('ExceptioncaughtbyExceptionHandler')
returnExceptionManager.PASS
```

```
ExceptionManager.add_handler(E())
```

Then, all exceptions will be set to PASS, and logged to the console! 

###### `handle_exception(` _inst_ `)` 

Called by `ExceptionManagerBase` to handle a exception. 

Defaults to returning `ExceptionManager.RAISE` that re-raises the exception. Return `ExceptionManager.PASS` to indicate that the exception was handled and should be ignored. 

This may be called multiple times with the same exception, if `ExceptionManager.RAISE` is returned as the exception bubbles through multiple kivy exception handling levels. 

`class kivymd.tools.hotreload.app.MDApp(` _**kwargs_ `)` 

HotReload Application class. 

###### `property appname` 

Return the name of the application class. 

###### `DEBUG` 

Control either we activate debugging in the app or not. Defaults depend if ‘DEBUG’ exists in os.environ. 

_`DEBUG`_ is a `BooleanProperty` . 

###### `FOREGROUND_LOCK` 

If _True_ it will require the foreground lock on windows. 

_`FOREGROUND_LOCK`_ is a `BooleanProperty` and defaults to _False_ . 

###### `KV_FILES` 

List of KV files under management for auto reloader. 

_`KV_FILES`_ is a `ListProperty` and defaults to _[]_ . 

###### `KV_DIRS` 

List of managed KV directories for autoloader. 

_`KV_DIRS`_ is a `ListProperty` and defaults to _[]_ . 

**2.9. KivyMD** 

**699** 

**KivyMD, Release 2.0.1.dev0** 

###### `AUTORELOADER_PATHS` 

List of path to watch for auto reloading. 

_`AUTORELOADER_PATHS`_ is a `ListProperty` and defaults to _([(“.”, {“recursive”: True})]_ . 

###### `AUTORELOADER_IGNORE_PATTERNS` 

List of extensions to ignore. 

_`AUTORELOADER_IGNORE_PATTERNS`_ is a `ListProperty` and defaults to _[‘*.pyc’, ‘*__pycache__*’]_ . 

###### `CLASSES` 

Factory classes managed by hotreload. 

_`CLASSES`_ is a `DictProperty` and defaults to _{}_ . 

###### `IDLE_DETECTION` 

Idle detection (if True, event on_idle/on_wakeup will be fired). Rearming idle can also be done with _rearm_idle()_ . 

_`IDLE_DETECTION`_ is a `BooleanProperty` and defaults to _False_ . 

###### `IDLE_TIMEOUT` 

Default idle timeout. 

_`IDLE_TIMEOUT`_ is a `NumericProperty` and defaults to _60_ . 

###### `RAISE_ERROR` 

Raise error. When the _DEBUG_ is activated, it will raise any error instead of showing it on the screen. If you still want to show the error when not in _DEBUG_ , put this to _False_ . 

_`RAISE_ERROR`_ is a `BooleanProperty` and defaults to _True_ . 

###### `build()` 

Initializes the application; it will be called only once. If this method returns a widget (tree), it will be used as the root widget and added to the window. 

###### **Returns** 

None or a root `Widget` instance if no self.root exists. 

###### `get_root()` 

Return a root widget, that will contains your application. It should not be your application widget itself, as it may be destroyed and recreated from scratch when reloading. 

By default, it returns a RelativeLayout, but it could be a Viewport. 

###### `get_root_path()` 

Return the root file path. 

###### `abstract build_app(` _first=False_ `)` 

Must return your application widget. 

If _first_ is set, it means that will be your first time ever that the application is built. Act according to it. 

###### `unload_app_dependencies()` 

Called when all the application dependencies must be unloaded. Usually happen before a reload 

###### `load_app_dependencies()` 

Load all the application dependencies. This is called before rebuild. 

`rebuild(` _*args_ , _**kwargs_ `)` 

**Chapter 2. Contents** 

**700** 

**KivyMD, Release 2.0.1.dev0** 

`set_error(` _exc_ , _tb=None_ `)` 

###### `bind_key(` _key_ , _callback_ `)` 

Bind a key (keycode) to a callback (cannot be unbind). 

###### `enable_autoreload()` 

Enable autoreload manually. It is activated automatically if “DEBUG” exists in environ. It requires the _watchdog_ module. 

###### `prepare_foreground_lock()` 

Try forcing app to front permanently to avoid windows pop ups and notifications etc.app. 

Requires fake full screen and borderless. 

**Note:** This function is called automatically if _FOREGROUND_LOCK_ is set 

###### `set_widget(` _wid_ `)` 

Clear the root container, and set the new approot widget to _wid_ . 

###### `apply_state(` _state_ `)` 

Whatever the current state is, reapply the current state. 

###### `install_idle(` _timeout=60_ `)` 

Install the idle detector. Default timeout is 60s. Once installed, it will check every second if the idle timer expired. The timer can be rearm using _`rearm_idle()`_ . 

###### `rearm_idle(` _*args_ `)` 

Rearm the idle timer. 

###### `patch_builder()` 

###### `on_idle(` _*args_ `)` 

Event fired when the application enter the idle mode. 

###### `on_wakeup(` _*args_ `)` 

Event fired when the application leaves idle mode. 

###### **kivymd.tools.packaging** 

###### **API -** `kivymd.tools.packaging` 

###### **Submodules** 

###### **PyInstaller hooks** 

Add `hookspath=[kivymd.hooks_path]` to your .spec file. 

**2.9. KivyMD** 

**701** 

**KivyMD, Release 2.0.1.dev0** 

###### **Example of .spec file** 

```
#-*-mode:python;coding:utf-8-*-
importsys
importos
fromkivy_depsimportsdl2,glew
fromkivymdimporthooks_pathaskivymd_hooks_path
path=os.path.abspath(".")
a=Analysis(
["main.py"],
pathex=[path],
hookspath=[kivymd_hooks_path],
win_no_prefer_redirects=False,
win_private_assemblies=False,
cipher=None,
noarchive=False,
)
pyz=PYZ(a.pure,a.zipped_data,cipher=None)
exe=EXE(
pyz,
a.scripts,
a.binaries,
a.zipfiles,
a.datas,
*[Tree(p)forpin(sdl2.dep_bins+glew.dep_bins)],
debug=False,
strip=False,
upx=True,
name="app_name",
console=True,
)
```

**API -** `kivymd.tools.packaging.pyinstaller` 

```
kivymd.tools.packaging.pyinstaller.hooks_path
```

Path to hook directory to use with PyInstaller. See _`kivymd.tools.packaging.pyinstaller`_ for more information. 

```
kivymd.tools.packaging.pyinstaller.get_hook_dirs()
```

```
kivymd.tools.packaging.pyinstaller.get_pyinstaller_tests()
```

**Chapter 2. Contents** 

**702** 

**KivyMD, Release 2.0.1.dev0** 

###### **Submodules** 

###### **PyInstaller hook for KivyMD** 

Adds fonts, images and KV files to package. 

All modules from uix directory are added by Kivy hook. 

**API -** `kivymd.tools.packaging.pyinstaller.hook-kivymd` 

```
kivymd.tools.packaging.pyinstaller.hook-kivymd.datas=[(),()]
```

###### **kivymd.tools.patterns** 

**API -** `kivymd.tools.patterns` 

###### **Submodules** 

###### **The script creates a new View package** 

The script creates a new View package in an existing project with an MVC template created using the create_project utility. 

Added in version 1.0.0. 

**See also:** 

Utility create_project 

###### **Use a clean architecture for your applications.** 

To add a new view to an existing project that was created using the _create_project_ utility, use the following command: 

```
kivymd.add_view\
name_pattern\
path_to_project\
name_view
```

Example command: 

```
kivymd.add_view\
MVC\
/Users/macbookair/Projects\
NewScreen
```

You can also add new views with responsive behavior to an existing project: 

**2.9. KivyMD** 

**703** 

**KivyMD, Release 2.0.1.dev0** 

```
kivymd.add_view\
MVC\
/Users/macbookair/Projects\
NewScreen\
--use_responsiveyes
```

For more information about adaptive design, see here. 

**API -** `kivymd.tools.patterns.add_view` 

```
kivymd.tools.patterns.add_view.main()
```

The function of adding a new view to the project. 

###### **Script creates a project with the MVC pattern** 

Added in version 1.0.0. 

###### **See also:** 

MVC pattern 

**Use a clean architecture for your applications.** 



Use a clean architecture for your applications. KivyMD allows you to quickly create a project template with the MVC pattern. So far, this is the only pattern that this utility offers. You can also include database support in your project. At the moment, support for the Firebase database (the basic implementation of the real time database) and RestDB (the full implementation) is available. 

###### **Project creation** 

Template command: 

```
kivymd.create_project\
name_pattern\
path_to_project\
name_project\
python_version\
kivy_version
```

Example command: 

**Chapter 2. Contents** 

**704** 





<!-- Start of picture text -->
MyMVCProject<br><!-- End of picture text -->

v Gi assets > Bi fonts & BB images ¥ WB Controller B _init_.py B main_screen.py ¥ Hi libs Bj _init_.py ¥ MB Model B _init_.py Bi base_model.py Bj main_screen.py ¥ BB utility Bj _init_.py By observer.py > Bi ven ¥ MB view * GB MainScreen ¥ GB components B _init_.py Bi _init_.py Bi main_screen.kv Ej main_screen.py Bj _init_.py Bj base_screen.py Bi screens.py Bj main.py B Makefile BB requirements.txt 

###### MyMVCProject 

> (i assets ® [i Controller » GH libs > Bi Model > BB Utility >» Bi venv > BB View B main.py By Makefile Ee requirements. bet 







<!-- Start of picture text -->
MyM¥VCProject<br>> (assets<br>* (i Controller<br>> HB libs<br>7 BB Model<br>By _ init__.py<br>By base_model.py<br>Ej database.py<br>By main_screen.py<br>> BB Utility<br>> BB ven<br>* BE View<br>Bj main.py<br>BR Makefile<br>& requirements.txt<br><!-- End of picture text -->

**KivyMD, Release 2.0.1.dev0** 

```
classDataBase:
def__init__(self):
database_url="https://restdbio-5498.restdb.io"
api_key="7ce258d66f919d3a891d1166558765f0b4dbd"
```

**Note:** Please note that _database.py_ the shell in the _DataBase_ class uses the _database_url_ and _api_key_ parameters on the test database (works only in read mode), so you should use your data for the database. 

###### **Create project with hot reload** 

Template command: 

```
kivymd.create_project\
name_pattern\
path_to_project\
name_project\
python_version\
kivy_version\
--use_hotreload
```

Example command: 

```
kivymd.create_project\
MVC\
/Users/macbookair/Projects\
MyMVCProject\
python3.10\
2.1.0\
--use_hotreloadyes
```

After creating the project, open the file _main.py_ , there is a lot of useful information. Also, the necessary information is in other modules of the project in the form of comments. So do not forget to look at the source files of the created project. 

###### **Create project with responsive view** 

When creating a project, you can specify which views should use responsive behavior. To do this, specify the name of the view/views in the _–use_responsive_ argument: 

Template command: 

```
kivymd.create_project\
name_pattern\
path_to_project\
name_project\
python_version\
kivy_version\
--name_screenFirstScreenSecondScreenThirdScreen\
--use_responsiveFirstScreenSecondScreen
```

**2.9. KivyMD** 

**707** 

**KivyMD, Release 2.0.1.dev0** 

The _FirstScreen_ and _SecondScreen_ views will be created with an responsive architecture. For more detailed information about using the adaptive view, see the MDResponsiveLayout widget. 

###### **Others command line arguments** 

###### **Required Arguments** 

- **pattern** 

**–** the name of the pattern with which the project will be created 

- **directory** 

**–** directory in which the project will be created 

- **name** 

   - project name 

- **python_version** 

   - the version of Python (specify as _python3.9_ or _python3.8_ ) with 

   - which the virtual environment will be created 

- **kivy_version** 

**–** version of Kivy (specify as _2.1.0_ or _master_ ) that will be used in the project 

###### **Optional arguments** 

- **name_screen** 

   - the name of the class which be used when creating the project pattern 

When you need to create an application template with multiple screens, use multiple values separated by a space for the _name_screen_ parameter, for example, as shown below: 

Template command: 

```
kivymd.create_project\
name_pattern\
path_to_project\
name_project\
python_version\
kivy_version\
--name_screenFirstScreenSecondScreenThirdScreen
```

- **name_database** 

   - provides a basic template for working with the ‘firebase’ library 

   - or a complete implementation for working with a database ‘restdb.io’ 

###### • **use_hotreload** 

   - creates a hot reload entry point to the application 

- **use_localization** 

   - creates application localization files 

**Chapter 2. Contents** 

**708** 

**KivyMD, Release 2.0.1.dev0** 

- **use_responsive** 

   - the name/names of the views to be used by the responsive UI 

**Warning:** On Windows, hot reloading of Python files may not work. But, for example, there is no such problem in macOS. If you fix this, please report it to the KivyMD community. 

**API -** `kivymd.tools.patterns.create_project` 

```
kivymd.tools.patterns.create_project.main()
```

Project creation function. 

###### **kivymd.tools.patterns.MVC** 

**API -** `kivymd.tools.patterns.MVC` 

###### **Submodules** 

###### **kivymd.tools.patterns.MVC.Model** 

**API -** `kivymd.tools.patterns.MVC.Model` 

###### **Submodules** 

###### **kivymd.tools.patterns.MVC.Model.database_firebase** 

**API -** `kivymd.tools.patterns.MVC.Model.database_firebase` 

`kivymd.tools.patterns.MVC.Model.database_firebase.get_connect(` _func_ , _host='8.8.8.8'_ , _port=53_ , _timeout=3_ `)` 

Checks for an active Internet connection. 

```
classkivymd.tools.patterns.MVC.Model.database_firebase.DataBase
```

Your methods for working with the database should be implemented in this class. 

```
name='Firebase'
```

`get_data_from_collection(` _name_collection: str_ `)` _→_ dict | bool 

Returns data of the selected collection from the database. 

**2.9. KivyMD** 

**709** 

**KivyMD, Release 2.0.1.dev0** 

###### **Restdb.io API Wrapper** 

This package is an API Wrapper for the website restdb.io, which allows for online databases. 

**API -** `kivymd.tools.patterns.MVC.Model.database_restdb` 

`kivymd.tools.patterns.MVC.Model.database_restdb.get_connect(` _func_ , _host='8.8.8.8'_ , _port=53_ , _timeout=3_ `)` 

Checks for an active Internet connection. 

```
classkivymd.tools.patterns.MVC.Model.database_restdb.DataBase
```

```
name='RestDB'
```

`upload_file(` _path_to_file: str_ `)` _→_ dict | bool 

Uploads a file to the database. You can upload a file to the database only from a paid account. 

`get_data_from_collection(` _collection_address: str_ `)` _→_ bool | list 

Returns data of the selected collection from the database. 

`delete_doc_from_collection(` _collection_address: str_ `)` _→_ bool 

Delete data of the selected collection from the database. 

###### **Parameters** 

`collection_address` – “database_url/id_collection”. 

`add_doc_to_collection(` _data: dict_ , _collection_address: str_ `)` _→_ bool 

Add collection to the database. 

`edit_data(` _collection: dict_ , _collection_address: str_ , _collection_id: str_ `)` _→_ bool Modifies data in a collection of data in a database. 

###### **kivymd.tools.patterns.MVC.libs** 

**API -** `kivymd.tools.patterns.MVC.libs` 

###### **Submodules** 

###### **kivymd.tools.patterns.MVC.libs.translation** 

**API -** `kivymd.tools.patterns.MVC.libs.translation` 

`class kivymd.tools.patterns.MVC.libs.translation.Translation(` _defaultlang_ , _domian_ , _resource_dir_ `)` Original source - https://github.com/tito/kivy-gettext-example. 

```
observers=[]
```

`fbind(` _name_ , _func_ , _args_ , _**kwargs_ `)` 

`funbind(` _name_ , _func_ , _args_ , _**kwargs_ `)` 

**Chapter 2. Contents** 

**710** 

**KivyMD, Release 2.0.1.dev0** 

`switch_lang(` _lang_ `)` 

###### **kivymd.tools.release** 

**API -** `kivymd.tools.release` 

###### **Submodules** 

###### **kivymd.tools.release.git_commands** 

###### **API -** `kivymd.tools.release.git_commands` 

- `kivymd.tools.release.git_commands.command(` _cmd: list_ , _capture_output: bool = False_ `)` _→_ str Run system command. 

- `kivymd.tools.release.git_commands.get_previous_version()` _→_ str 

Returns latest tag in git. 

- `kivymd.tools.release.git_commands.git_clean(` _ask: bool = True_ `)` 

Clean git repository from untracked and changed files. 

`kivymd.tools.release.git_commands.git_commit(` _message: str_ , _allow_error: bool = False_ , _add_files: list = None_ `)` 

Make commit. 

`kivymd.tools.release.git_commands.git_tag(` _name: str_ `)` Create tag. 

`kivymd.tools.release.git_commands.git_push(` _branches_to_push: list_ , _ask: bool = True_ , _push: bool = False_ `)` 

Push all changes. 

###### **Script to make release** 

Run this script before release (before deploying). 

What this script does: 

- Undo all local changes in repository 

- Update version in ___init__.py_ , _README.md_ 

- Format files 

- Rename file “unreleased.rst” to version, add to index.rst 

- Commit “Version ...” 

- Create tag 

- Add _unreleased.rst_ to Changelog, add to _index.rst_ 

- Commit 

**2.9. KivyMD** 

**711** 

**KivyMD, Release 2.0.1.dev0** 

- Git push 

###### **API -** `kivymd.tools.release.make_release` 

```
kivymd.tools.release.make_release.run_pre_commit()
```

Run pre-commit. 

`kivymd.tools.release.make_release.replace_in_file(` _pattern_ , _repl_ , _file_ `)` 

Replace one _pattern_ match to _repl_ in file _file_ . 

`kivymd.tools.release.make_release.update_version_py(` _version_ , _is_release_ , _test: bool = False_ `)` Change version in _kivymd/_version.py_ . 

`kivymd.tools.release.make_release.update_readme(` _previous_version_ , _version_ , _test: bool = False_ `)` 

Change version in _README.md_ . 

`kivymd.tools.release.make_release.move_changelog(` _index_file_ , _unreleased_file_ , _previous_version_ , _version_file_ , _version_ , _test: bool = False_ `)` 

Edit unreleased.rst and rename to <version>.rst. 

`kivymd.tools.release.make_release.create_unreleased_changelog(` _index_file_ , _unreleased_file_ , _version_ , 

_ask: bool = True_ , _test: bool = False_ `)` 

Create unreleased.rst by template. 

```
kivymd.tools.release.make_release.main()
```

```
kivymd.tools.release.make_release.create_argument_parser()
```

###### **Tool for updating Iconic font** 

Downloads archive from https://github.com/Templarian/MaterialDesign-Webfont and updates font file with icon_definitions. 

###### **API -** `kivymd.tools.release.update_icons` 

```
kivymd.tools.release.update_icons.kivymd_path
```

```
kivymd.tools.release.update_icons.font_path
```

```
kivymd.tools.release.update_icons.icon_definitions_path
```

```
kivymd.tools.release.update_icons.font_version='master'
```

```
kivymd.tools.release.update_icons.url
```

```
kivymd.tools.release.update_icons.temp_path
```

```
kivymd.tools.release.update_icons.temp_repo_path
```

```
kivymd.tools.release.update_icons.temp_font_path
```

**Chapter 2. Contents** 

**712** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.tools.release.update_icons.temp_preview_path kivymd.tools.release.update_icons.re_icons_json kivymd.tools.release.update_icons.re_additional_icons kivymd.tools.release.update_icons.re_version kivymd.tools.release.update_icons.re_quote_keys kivymd.tools.release.update_icons.re_icon_definitions kivymd.tools.release.update_icons.re_version_in_file kivymd.tools.release.update_icons.download_file(` _url_ , _path_ `) kivymd.tools.release.update_icons.unzip_archive(` _archive_path_ , _dir_path_ `) kivymd.tools.release.update_icons.get_icons_list()` 

`kivymd.tools.release.update_icons.make_icon_definitions(` _icons_ `)` 

`kivymd.tools.release.update_icons.export_icon_definitions(` _icon_definitions_ , _version_ `) kivymd.tools.release.update_icons.update_icons(` _make_commit: bool = False_ `) kivymd.tools.release.update_icons.main()` 

###### **kivymd.uix** 

**API -** `kivymd.uix` 

###### `class kivymd.uix.MDAdaptiveWidget` 

###### `adaptive_height` 

If _True_ , the following properties will be applied to the widget: 

```
size_hint_y:None
height:self.minimum_height
```

_`adaptive_height`_ is an `BooleanProperty` and defaults to _False_ . 

###### `adaptive_width` 

If _True_ , the following properties will be applied to the widget: 

```
size_hint_x:None
width:self.minimum_width
```

_`adaptive_width`_ is an `BooleanProperty` and defaults to _False_ . 

###### `adaptive_size` 

If _True_ , the following properties will be applied to the widget: 

```
size_hint:None,None
size:self.minimum_size
```

_`adaptive_size`_ is an `BooleanProperty` and defaults to _False_ . 

**2.9. KivyMD** 

**713** 

**KivyMD, Release 2.0.1.dev0** 

`on_adaptive_height(` _md_widget_ , _value: bool_ `)` _→_ None 

`on_adaptive_width(` _md_widget_ , _value: bool_ `)` _→_ None 

`on_adaptive_size(` _md_widget_ , _value: bool_ `)` _→_ None 

###### **Submodules** 

###### **kivymd.uix.appbar** 

**API -** `kivymd.uix.appbar` 

###### **Submodules** 

###### **kivymd.uix.badge** 

**API -** `kivymd.uix.badge` 

###### **Submodules** 

**Behaviors** 

Modules and classes implementing various behaviors for buttons etc. 

**API -** `kivymd.uix.behaviors` 

**Submodules** 

**kivymd.uix.bottomsheet** 

**API -** `kivymd.uix.bottomsheet` 

###### **Submodules** 

**kivymd.uix.button** 

**API -** `kivymd.uix.button` 

**Submodules** 

**kivymd.uix.card** 

**API -** `kivymd.uix.card` 

**Chapter 2. Contents** 

**714** 

**KivyMD, Release 2.0.1.dev0** 

###### **Submodules** 

**kivymd.uix.carousel** 

**API -** `kivymd.uix.carousel` 

**Submodules** 

**kivymd.uix.chip** 

**API -** `kivymd.uix.chip` 

###### **Submodules** 

**Controllers** 

Added in version 1.0.0. 

Modules and classes that implement useful methods for getting information about the state of the current application window. 

**API -** `kivymd.uix.controllers` 

**Submodules** 

**kivymd.uix.datatables** 

**API -** `kivymd.uix.datatables` 

**Submodules** 

**kivymd.uix.dialog** 

**API -** `kivymd.uix.dialog` 

**Submodules** 

**kivymd.uix.divider** 

**API -** `kivymd.uix.divider` 

**Submodules** 

**kivymd.uix.dropdownitem** 

**2.9. KivyMD** 

**715** 

**KivyMD, Release 2.0.1.dev0** 

**API -** `kivymd.uix.dropdownitem` 

###### **Submodules** 

###### **kivymd.uix.expansionpanel** 

**API -** `kivymd.uix.expansionpanel` 

###### **Submodules** 

###### **kivymd.uix.exprogressindicator** 

**API -** `kivymd.uix.exprogressindicator` 

###### **Submodules** 

###### **Animation delegates for Material Design progress indicators.** 

Animation delegates for Material Design progress indicators. 

This module implements the animation algorithms used by the linear and circular indeterminate progress indicators. The implementations are based on the original Android Material Components library and reproduce the behavior of the corresponding Material animations. 

The module provides animators for: 

- linear indeterminate (disjoint); 

- linear indeterminate (contiguous); 

- circular indeterminate (retreat); 

- circular indeterminate (advanced). 

Each animator calculates the current geometry of the animated indicator from the elapsed animation time and returns normalized values that can be used by the rendering layer. 

Ported from the Android Material Components library. 

**API -** `kivymd.uix.exprogressindicator.animators` 

###### `class kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimator` 

Animator for the Material Design linear indeterminate progress indicator using the disjoint animation style. 

The animation consists of two independent line segments whose head and tail positions are animated with individual cubic Bézier interpolators. 

Ported from the Android Material Components implementation ( _LinearIndeterminateDisjointAnimatorDelegate_ ). 

###### `INTERPOLATORS` 

```
DURATION_TO_MOVE_SEGMENT_ENDS=[533,567,850,750]
```

```
DELAY_TO_MOVE_SEGMENT_ENDS=[1267,1000,333,0]
```

**Chapter 2. Contents** 

**716** 

**KivyMD, Release 2.0.1.dev0** 

```
TOTAL_DURATION_IN_MS=1800
```

```
LOOP_DELAY=20
```

`get_fraction_in_range(` _playtime_ , _start_ , _duration_ `)` 

Returns the normalized animation fraction for the specified time range. 

###### **Parameters** 

- `playtime` – Current animation playtime in milliseconds. 

- `start` – Start time of the animation interval in milliseconds. 

- `duration` – Duration of the animation interval in milliseconds. 

###### **Returns** 

Normalized value in the range `[0.0, 1.0]` . 

`compute_bar(` _playtime_ , _head_idx_ , _tail_idx_ `)` 

Computes the start and end positions of an animated line segment. 

###### **Parameters** 

- `playtime` – Current animation playtime in milliseconds. 

- `head_idx` – Interpolator index for the segment head. 

- `tail_idx` – Interpolator index for the segment tail. 

###### **Returns** 

Tuple containing the normalized start and end positions of the segment. 

`bars(` _time_sec_ `)` 

Calculates the current state of the disjoint linear indicator. 

###### **Parameters** 

`time_sec` – Current animation time in seconds. 

###### **Returns** 

Two animated line segments represented as: 

```
(
(start1,end1),
(start2,end2),
)
```

```
classkivymd.uix.exprogressindicator.animators.LinearIndeterminateContiguousAnimator
```

Animator for the Material Design linear indeterminate progress indicator using the contiguous animation style. 

The progress indicator is divided into three connected segments that move continuously across the track while cycling through the color palette. 

Ported from the Android Material Components implementation ( _LinearIndeterminateContiguousAnimatorDelegate_ ). 

```
INTERPOLATOR
```

```
TOTAL_DURATION_IN_MS=667
```

```
DURATION_PER_CYCLE_IN_MS=333
```

```
last_cycle_count
```

**2.9. KivyMD** 

**717** 

**KivyMD, Release 2.0.1.dev0** 

###### `current_indices = [0, 0, 0]` 

###### `len_palette = 0` 

###### `get_fraction_in_range(` _playtime_ , _start_ , _duration_ `)` 

Returns the normalized animation fraction for the specified time range. 

###### **Parameters** 

- `playtime` – Current animation playtime in milliseconds. 

- `start` – Start time of the animation interval in milliseconds. 

- `duration` – Duration of the animation interval in milliseconds. 

###### **Returns** 

Animation progress. 

###### `bars(` _time_sec_ `)` 

Calculates the current state of the contiguous linear indicator. 

###### **Parameters** 

`time_sec` – Current animation time in seconds. 

###### **Returns** 

Three contiguous segments represented as: 

```
(
(start0,end0,color_index0),
(start1,end1,color_index1),
(start2,end2,color_index2),
)
```

###### `class kivymd.uix.exprogressindicator.animators.CircularIndeterminateRetreatAnimator` 

Animator for the Material Design circular indeterminate progress indicator using the retreat animation style. 

The animation continuously rotates the indicator while expanding and shrinking the visible arc. The active color changes after each rotation cycle. 

Ported from the Android Material Components implementation ( _CircularIndeterminateRetreatAnimatorDelegate_ ). 

```
INTERPOLATOR
TOTAL_DURATION_MS=6000
DURATION_SPIN_MS=500
DURATION_GROW_MS=3000
DURATION_SHRINK_MS=3000
DELAY_SPINS_MS=[0,1500,3000,4500]
CONSTANT_ROTATION_DEGREES=1080
SPIN_ROTATION_DEGREES=90
END_FRACTION_RANGE=[0.1,0.87]
```

**Chapter 2. Contents** 

**718** 

**KivyMD, Release 2.0.1.dev0** 

###### `get_fraction_in_range(` _playtime_ , _start_ , _duration_ `)` 

Returns the normalized animation fraction for the specified time range. 

###### **Parameters** 

- `playtime` – Current animation playtime in milliseconds. 

- `start` – Start time of the animation interval in milliseconds. 

- `duration` – Duration of the animation interval in milliseconds. 

###### **Returns** 

Normalized value in the range `[0.0, 1.0]` . 

`bars(` _time_sec_ `)` 

Calculates the current state of the retreat circular indicator. 

###### **Parameters** 

`time_sec` – Current animation time in seconds. 

###### **Returns** 

Tuple containing: 

```
(
rotation_in_radians,
(
start_fraction,
end_fraction,
color_index,
),
)
```

###### `class kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator` 

Animator for the Material Design circular indeterminate progress indicator using the advanced animation style. 

The animation expands and collapses the arc while smoothly rotating around the circle. Color transitions are synchronized with each animation cycle. 

Ported from the Android Material Components implementation ( _CircularIndeterminateAdvanceAnimatorDelegate_ ). 

```
INTERPOLATOR
TOTAL_DURATION_MS=5400
TOTAL_CYCLES=4
DURATION_EXPAND=667
DURATION_COLLAPSE=667
DURATION_FADE_IN=333
DELAY_EXPAND=[0,1350,2700,4050]
DELAY_COLLAPSE=[667,2017,3367,4717]
DELAY_FADE_IN=[1000,2350,3700,5050]
```

```
TAIL_DEGREES_OFFSET
```

**2.9. KivyMD** 

**719** 

**KivyMD, Release 2.0.1.dev0** 

```
EXTRA_DEGREES_PER_CYCLE=250
```

###### `CONSTANT_ROTATION_DEGREES = 1520` 

`get_fraction_in_range(` _playtime_ , _start_ , _duration_ `)` 

Returns the normalized animation fraction for the specified time range. 

###### **Parameters** 

- `playtime` – Current animation playtime in milliseconds. 

- `start` – Start time of the animation interval in milliseconds. 

- `duration` – Duration of the animation interval in milliseconds. 

###### **Returns** 

Normalized value in the range `[0.0, 1.0]` . 

`get_color(` _time_sec_ , _playtime_ms_ `)` 

Calculates the current color transition. 

###### **Parameters** 

- `time_sec` – Current animation time in seconds. 

- `playtime_ms` – Current animation playtime in milliseconds. 

###### **Returns** 

Tuple containing the start color index, end color index, and interpolation factor. 

`bars(` _time_sec_ `)` 

Calculates the current state of the advanced circular indicator. 

###### **Parameters** 

`time_sec` – Current animation time in seconds. 

###### **Returns** 

Tuple containing: 



<!-- Start of picture text -->
(<br>rotation,<br>(<br>start_fraction,<br>end_fraction,<br>(<br>start_color_index,<br>end_color_index,<br>color_lerp,<br>),<br>),<br>)<br><!-- End of picture text -->

The rotation value is always `0` because the rotation is already encoded into the calculated arc fractions. 

**Chapter 2. Contents** 

**720** 

**KivyMD, Release 2.0.1.dev0** 

**kivymd.uix.filemanager** 

**API -** `kivymd.uix.filemanager` 

**Submodules** 

**kivymd.uix.fitimage** 

**API -** `kivymd.uix.fitimage` 

**Submodules** 

###### **kivymd.uix.imagelist** 

**API -** `kivymd.uix.imagelist` 

**Submodules** 

**kivymd.uix.label** 

**API -** `kivymd.uix.label` 

**Submodules** 

###### **kivymd.uix.list** 

**API -** `kivymd.uix.list` 

**Submodules** 

**kivymd.uix.loadingindicator** 

**API -** `kivymd.uix.loadingindicator` 

**Submodules** 

**kivymd.uix.menu** 

**API -** `kivymd.uix.menu` 

**Submodules** 

**kivymd.uix.navigationbar** 

**API -** `kivymd.uix.navigationbar` 

**2.9. KivyMD** 

**721** 

**KivyMD, Release 2.0.1.dev0** 

###### **Submodules** 

###### **kivymd.uix.navigationdrawer** 

**API -** `kivymd.uix.navigationdrawer` 

###### **Submodules** 

###### **kivymd.uix.navigationrail** 

**API -** `kivymd.uix.navigationrail` 

###### **Submodules** 

###### **kivymd.uix.pickers** 

**API -** `kivymd.uix.pickers` 

###### **Submodules** 

###### **kivymd.uix.pickers.datepicker** 

**API -** `kivymd.uix.pickers.datepicker` 

###### **Submodules** 

###### **kivymd.uix.pickers.timepicker** 

**API -** `kivymd.uix.pickers.timepicker` 

**Submodules** 

**kivymd.uix.progressindicator** 

**API -** `kivymd.uix.progressindicator` 

###### **Submodules** 

**kivymd.uix.refreshlayout** 

**API -** `kivymd.uix.refreshlayout` 

**Submodules** 

**kivymd.uix.search** 

**Chapter 2. Contents** 

**722** 

**KivyMD, Release 2.0.1.dev0** 

**API -** `kivymd.uix.search` 

###### **Submodules** 

**kivymd.uix.segmentedbutton** 

**API -** `kivymd.uix.segmentedbutton` 

**Submodules** 

**kivymd.uix.selectioncontrol** 

**API -** `kivymd.uix.selectioncontrol` 

**Submodules** 

###### **kivymd.uix.slider** 

**API -** `kivymd.uix.slider` 

**Submodules** 

**kivymd.uix.sliverappbar** 

**API -** `kivymd.uix.sliverappbar` 

**Submodules** 

**kivymd.uix.snackbar** 

**API -** `kivymd.uix.snackbar` 

**Submodules** 

**kivymd.uix.swiper** 

**API -** `kivymd.uix.swiper` 

**Submodules** 

**kivymd.uix.tab** 

**API -** `kivymd.uix.tab` 

###### **Submodules** 

**2.9. KivyMD** 

**723** 

**KivyMD, Release 2.0.1.dev0** 

###### **kivymd.uix.textfield** 

**API -** `kivymd.uix.textfield` 

###### **Submodules** 

###### **kivymd.uix.tooltip** 

**API -** `kivymd.uix.tooltip` 

###### **Submodules** 

###### **kivymd.uix.transition** 

**API -** `kivymd.uix.transition` 

###### **Submodules** 

**kivymd.utils** 

**API -** `kivymd.utils` 

`kivymd.utils.next_frame(` _func_ , _*args_ , _**kwargs_ `)` 

###### **Submodules** 

###### **Cubic Bézier curve interpolation utilities.** 

Cubic Bézier curve interpolation utilities. 

This module provides a mathematical implementation of a cubic Bézier curve interpolator ported from the Android Material Design animation framework. 

The implementation is primarily used for calculating easing functions and animation timing curves. It allows converting an input progress value (X-axis) into the corresponding interpolated output value (Y-axis) based on four Bézier control points. 

###### **The module includes:** 

- A compatibility implementation of the cubic root function for Python versions older than 3.11. 

- Numerical helpers for solving cubic equations. 

- The CubicBezier class for evaluating cubic Bézier easing curves. 

The implementation follows the algorithm used in Android’s Material Design motion system to achieve accurate interpolation behavior. 

**Chapter 2. Contents** 

**724** 

**KivyMD, Release 2.0.1.dev0** 

###### **API -** `kivymd.utils.cubic_bezier` 

###### `kivymd.utils.cubic_bezier.float_epsilon = 8.34465e-07` 

```
kivymd.utils.cubic_bezier.cbrt
```

`class kivymd.utils.cubic_bezier.CubicBezier(` _*args_ `)` 

Ported from Android source code. Represents a cubic Bézier curve interpolator. 

A cubic Bézier curve is defined by four control points: 

P0 — start point P1 — first control point P2 — second control point P3 — end point 

The curve is commonly used in UI animations to define easing behavior. Given an input progress value _x_ in the range [0, 1], the class calculates the corresponding output value _y_ on the curve. 

This implementation solves the cubic equation required to find the curve parameter _t_ for a given X value and then evaluates the curve at that parameter to obtain the interpolated Y value. 

###### **Attributes:** 

p0 (float): First control point value. p1 (float): Second control point value. p2 (float): Third control point value. p3 (float): Fourth control point value. 

###### **This type of interpolation is commonly used for:** 

- Animation easing functions. 

- Progress indicators. 

- UI transitions. 

- Material Design motion effects. 

###### `p0 = 0` 

###### `p1 = 0` 

###### `p2 = 0` 

###### `p3 = 0` 

###### `evaluate_cubic(` _p1_ , _p2_ , _t_ `)` 

Evaluates a cubic Bézier polynomial. 

###### **Args:** 

p1 (float): First control point. p2 (float): Second control point. t (float): Curve parameter in the range [0, 1]. 

###### **Returns:** 

float: Calculated Bézier curve value. 

###### `clamp_range(` _r_ `)` 

Clamps a calculated root value into the valid Bézier range. 

Small floating-point calculation errors are corrected using an epsilon tolerance. Values outside the acceptable range are converted to NaN. 

###### **Args:** 

r (float): Calculated root value. 

###### **Returns:** 

float: Corrected value or NaN if invalid. 

**2.9. KivyMD** 

**725** 

**KivyMD, Release 2.0.1.dev0** 

###### `close_to(` _x_ , _y_ `)` 

Checks whether two floating-point numbers are approximately equal. 

###### **Args:** 

x (float): First value. y (float): Second value. 

###### **Returns:** 

bool: True when the difference is below the precision threshold. 

###### `find_first_cubic_root(` _p0_ , _p1_ , _p2_ , _p3_ `)` 

Finds the first valid root of a cubic equation. 

The method solves the cubic polynomial generated from the Bézier curve equation and returns a parameter _t_ within the valid interval [0, 1]. 

###### **The implementation handles:** 

- Linear equations. 

- Quadratic equations. 

- Cubic equations with one or multiple roots. 

- Floating-point precision issues. 

###### **Args:** 

p0 (float): Polynomial coefficient. p1 (float): Polynomial coefficient. p2 (float): Polynomial coefficient. p3 (float): Polynomial coefficient. 

###### **Returns:** 

**float:** 

The first valid root in the range [0, 1], or NaN if no valid root exists. 

`t(` _value: float_ `)` 

Calculates the interpolated Bézier value for an input progress value. 

This method converts an X-axis position into the corresponding Y-axis position on the cubic Bézier curve. 

**Args:** 

**value (float):** Input progress value, normally in the range [0, 1]. 

**Returns:** 

**float:** Interpolated output value based on the Bézier curve. 

###### **Monitor module** 

The Monitor module is a toolbar that shows the activity of your current application : 

- FPS 

**Chapter 2. Contents** 

**726** 



<!-- Start of picture text -->
| (09:05 BF ca |<br>| }<br>MDToolbar<br><!-- End of picture text -->











<!-- Start of picture text -->
91 @<br>/ ( \<br>MDToolbar<br><!-- End of picture text -->

**CHAPTER THREE** 

###### **INDICES AND TABLES** 

- genindex 

- modindex 

- search 

**729** 

**KivyMD, Release 2.0.1.dev0** 

**Chapter 3. Indices and tables** 

**730** 

###### **PYTHON MODULE INDEX** 

###### k 

`kivymd.uix.appbar.appbar` , 496 `kivymd.uix.badge` , 714 `kivymd.uix.badge.badge` , 235 `kivymd.uix.behaviors` , 714 `kivymd.uix.behaviors.backgroundcolor_behavior` , 670 `kivymd.uix.behaviors.declarative_behavior` , 655 `kivymd.uix.behaviors.elevation` , 625 `kivymd.uix.behaviors.focus_behavior` , 619 `kivymd.uix.behaviors.hover_behavior` , 652 `kivymd.uix.behaviors.magic_behavior` , 646 `kivymd.uix.behaviors.motion_behavior` , 667 `kivymd.uix.behaviors.ripple_behavior` , 641 `kivymd.uix.behaviors.rotate_behavior` , 639 `kivymd.uix.behaviors.scale_behavior` , 616 `kivymd.uix.behaviors.state_layer_behavior` , 664 `kivymd.uix.behaviors.stencil_behavior` , 672 `kivymd.uix.behaviors.toggle_behavior` , 622 `kivymd.uix.behaviors.touch_behavior` , 663 `kivymd.uix.bottomsheet` , 714 `kivymd.uix.bottomsheet.bottomsheet` , , 432 `kivymd.uix.boxlayout` , 110 `kivymd.uix.button` , 714 `kivymd.uix.button.button` , 288 `kivymd.uix.card` , 714 `kivymd.uix.card.card` , 562 `kivymd.uix.carousel` , 715 `kivymd.uix.carousel.carousel` , 279 `kivymd.uix.chip` , 715 `kivymd.uix.chip.chip` , 341 `kivymd.uix.circularlayout` , , 71 `kivymd.uix.controllers` , 715 `kivymd.uix.controllers.windowcontroller` , , 615 `kivymd.uix.datatables` , 715 `kivymd.uix.datatables.datatables` , 158 `kivymd.uix.dialog` , 715 `kivymd.uix.dialog.dialog` , 577 `kivymd.uix.divider` , 715 `kivymd.uix.divider.divider` , 514 `kivymd.uix.dropdownitem` , 715 

`kivymd` , 693 `kivymd.animation` , 37 `kivymd.app` , 24 `kivymd.dynamic_color` , 42 `kivymd.effects` , 695 `kivymd.effects.stiffscroll` , 695 `kivymd.effects.stiffscroll.stiffscroll` , 674 `kivymd.factory_registers` , 694 `kivymd.font_definitions` , 32 `kivymd.icon_definitions` , 27 `kivymd.material_resources` , 694 `kivymd.theming` , 7 `kivymd.toast` , 695 `kivymd.toast.androidtoast` , 695 `kivymd.tools` , 696 `kivymd.tools.argument_parser` , 696 `kivymd.tools.hotreload` , 697 `kivymd.tools.hotreload.app` , 697 `kivymd.tools.packaging` , 701 `kivymd.tools.packaging.pyinstaller` , 701 `kivymd.tools.packaging.pyinstaller.hook-kivymd` , 703 `kivymd.tools.patterns` , 703 `kivymd.tools.patterns.add_view` , 703 `kivymd.tools.patterns.create_project` , 704 `kivymd.tools.patterns.MVC` , 709 `kivymd.tools.patterns.MVC.libs` , 710 `kivymd.tools.patterns.MVC.libs.translation` , 710 `kivymd.tools.patterns.MVC.Model` , 709 `kivymd.tools.patterns.MVC.Model.database_firebase` , 709 `kivymd.tools.patterns.MVC.Model.database_restdb` , 710 `kivymd.tools.release` , 711 `kivymd.tools.release.git_commands` , 711 `kivymd.tools.release.make_release` , 711 `kivymd.tools.release.update_icons` , 712 `kivymd.uix` , 713 `kivymd.uix.anchorlayout` , 108 `kivymd.uix.appbar` , 714 

**731** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.uix.dropdownitem.dropdownitem` , 231 `kivymd.uix.segmentedbutton.segmentedbutton` , `kivymd.uix.expansionpanel` , 716 414 `kivymd.uix.expansionpanel.expansionpanel` , 546 `kivymd.uix.selectioncontrol` , 723 `kivymd.uix.exprogressindicator` , 716 `kivymd.uix.selectioncontrol.selectioncontrol` , `kivymd.uix.exprogressindicator.animators` , 716 600 `kivymd.uix.exprogressindicator.exprogressindicatorkivymd.uix.slider` , , 723 145 `kivymd.uix.slider.slider` , 541 `kivymd.uix.filemanager` , 721 `kivymd.uix.sliverappbar` , 723 `kivymd.uix.filemanager.filemanager` , 250 `kivymd.uix.sliverappbar.sliverappbar` , 487 `kivymd.uix.fitimage` , 721 `kivymd.uix.snackbar` , 723 `kivymd.uix.fitimage.fitimage` , 554 `kivymd.uix.snackbar.snackbar` , 479 `kivymd.uix.floatlayout` , 69 `kivymd.uix.stacklayout` , 55 `kivymd.uix.gridlayout` , 117 `kivymd.uix.swiper` , 723 `kivymd.uix.hero` , 84 `kivymd.uix.swiper.swiper` , 198 `kivymd.uix.imagelist` , 721 `kivymd.uix.tab` , 723 `kivymd.uix.imagelist.imagelist` , 592 `kivymd.uix.tab.tab` , 119 `kivymd.uix.label` , 721 `kivymd.uix.textfield` , 724 `kivymd.uix.label.label` , 444 `kivymd.uix.textfield.textfield` , 204 `kivymd.uix.list` , 721 `kivymd.uix.tooltip` , 724 `kivymd.uix.list.list` , 405 `kivymd.uix.tooltip.tooltip` , 190 `kivymd.uix.loadingindicator` , 721 `kivymd.uix.transition` , 724 `kivymd.uix.loadingindicator.loadingindicator` , `kivymd.uix.transition.transition` , 430 142 `kivymd.uix.widget` , 112 `kivymd.uix.menu` , 721 `kivymd.utils` , 724 `kivymd.uix.menu.menu` , 378 `kivymd.utils.cubic_bezier` , 724 `kivymd.uix.navigationbar` , 721 `kivymd.utils.fpsmonitor` , 726 `kivymd.uix.navigationbar.navigationbar` , 267 `kivymd.utils.set_bars_colors` , 727 `kivymd.uix.navigationdrawer` , 722 `kivymd.uix.navigationdrawer.navigationdrawer` , 519 `kivymd.uix.navigationrail` , 722 `kivymd.uix.navigationrail.navigationrail` , 237 `kivymd.uix.pickers` , 722 `kivymd.uix.pickers.datepicker` , 722 `kivymd.uix.pickers.datepicker.datepicker` , 323 `kivymd.uix.pickers.timepicker` , 722 `kivymd.uix.pickers.timepicker.timepicker` , 308 `kivymd.uix.progressindicator` , 722 `kivymd.uix.progressindicator.progressindicator` , 369 `kivymd.uix.recycleboxlayout` , 60 `kivymd.uix.recyclegridlayout` , 115 `kivymd.uix.recycleview` , 74 `kivymd.uix.refreshlayout` , 722 `kivymd.uix.refreshlayout.refreshlayout` , 262 `kivymd.uix.relativelayout` , 58 `kivymd.uix.responsivelayout` , 79 `kivymd.uix.screen` , 77 `kivymd.uix.screenmanager` , 53 `kivymd.uix.scrollview` , 62 `kivymd.uix.search` , 722 `kivymd.uix.search.search` , 466 `kivymd.uix.segmentedbutton` , 723 

**Python Module Index** 

**732** 

###### **INDEX** 

###### A 

_method_ ), 534 `add_widget()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `absorb_impact()` ( _kivymd.uix.scrollview.StretchOverScrollStencil method_ ), 68 _method_ ), 514 `action_items` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `add_widget()` ( _kivymd.uix.appbar.appbar.MDTopAppBar attribute_ ), 512 _method_ ), 511 `active` ( _kivymd.uix.chip.chip.MDChip attribute_ ), 368 `add_widget()` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet_ `active` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem method_ ), 443 _attribute_ ), 277 `add_widget()` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheetDragHandle_ `active` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemmethod_ ), 442 _attribute_ ), 248 `add_widget()` ( _kivymd.uix.button.button.MDButton_ `active` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicatormethod_ ), 305 _attribute_ ), 377 `add_widget()` ( _kivymd.uix.button.button.MDExtendedFabButton_ `active` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItemmethod_ ), 307 _attribute_ ), 427 `add_widget()` ( _kivymd.uix.card.card.MDCardSwipe_ `active_canvas` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipplemethod_ ), 576 _property_ ), 642 `add_widget()` ( _kivymd.uix.carousel.carousel.MDCarousel_ `active_indicator_color` _method_ ), 286 `add_widget()` ( _kivymd.uix.carousel.carousel.MDCarouselItem_ ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicator attribute_ ), 145 _method_ ), 284 `active_indicator_color add_widget()` ( _kivymd.uix.chip.chip.MDChip method_ ), 369 ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItem attribute_ ), 535 `add_widget()` ( _kivymd.uix.dialog.dialog.MDDialog_ `active_indicator_color` _method_ ), 590 `add_widget()` ( _kivymd.uix.dropdownitem.dropdownitem.MDDropDownItem_ ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemIcon attribute_ ), 247 _method_ ), 234 `active_track_color` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `add_widget()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel attribute_ ), 155 _method_ ), 553 `adaptive_height` ( _kivymd.uix.MDAdaptiveWidget at-_ `add_widget()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanelContent tribute_ ), 713 _method_ ), 552 `adaptive_size` ( _kivymd.uix.MDAdaptiveWidget at-_ `add_widget()` ( _kivymd.uix.imagelist.imagelist.MDSmartTile tribute_ ), 713 _method_ ), 599 `add_widget()` ( _kivymd.uix.imagelist.imagelist.MDSmartTileOverlayContainer_ `adaptive_width` ( _kivymd.uix.MDAdaptiveWidget attribute_ ), 713 _method_ ), 597 `add_doc_to_collection() add_widget()` ( _kivymd.uix.label.label.MDIcon method_ ), 465 ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBase method_ ), 710 `add_widget()` ( _kivymd.uix.list.list.MDListItem method_ ), 414 `add_marked_icon_to_chip()` ( _kivymd.uix.chip.chip.MDChip method_ ), `add_widget()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem_ 369 _method_ ), 278 `add_row()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `add_widget()` ( _method_ ), 185 _method_ ), 535 `add_scrim()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationLayout_ `add_widget()` ( 

**733** 

**KivyMD, Release 2.0.1.dev0** 

_method_ ), 536 _method_ ), 404 `add_widget()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationLayout_ `allow_copy` ( _kivymd.uix.label.label.MDLabel attribute_ ), _method_ ), 534 464 `add_widget()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ `allow_hidden` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 249 _attribute_ ), 513 `add_widget()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailIte_ `allow_hover` ( _kivy_ **_m_** _d.uix.behaviors.hover_behavior.HoverBehavior method_ ), 248 _attribute_ ), 655 `add_widget()` ( _kivymd.uix.screenmanager.MDScreenManager_ `allow_selection` ( _kivymd.uix.label.label.MDLabel atmethod_ ), 55 _tribute_ ), 464 `add_widget()` ( _kivymd.uix.search.search.MDSearchBar_ `allow_stretch` ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), 478 _attribute_ ), 139 `add_widget()` ( _kivymd.uix.search.search.MDSearchViewContainer_ `am_pm` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker method_ ), 476 _attribute_ ), 320 `add_widget()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton_ `amplitude` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar method_ ), 429 _attribute_ ), 156 `add_widget()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItem_ `anchor` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), _method_ ), 427 575 `add_widget()` ( _kivymd.uix.slider.slider.MDSlider_ `anchor` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer method_ ), 544 _attribute_ ), 537 `add_widget()` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `anchor` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail method_ ), 495 _attribute_ ), 249 `add_widget()` ( _kivymd.uix.snackbar.snackbar.MDSnackbar_ `anchor` ( _kivymd.utils.fpsmonitor.FpsMonitor attribute_ ), _method_ ), 486 727 `add_widget()` ( _kivymd.uix.snackbar.snackbar.MDSnackbarButtonContainer_ `android_animation()` _method_ ), 485 ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), `add_widget()` ( _kivymd.uix.swiper.swiper.MDSwiper_ 140 _method_ ), 202 `angle` ( _kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior_ `add_widget()` ( _kivymd.uix.tab.tab.MDTabsCarousel attribute_ ), 671 _method_ ), 137 `anim_complete()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `add_widget()` ( _kivymd.uix.tab.tab.MDTabsItem method_ ), 644 _method_ ), 138 `anim_complete()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `add_widget()` ( _kivymd.uix.tab.tab.MDTabsItemSecondary method_ ), 646 _method_ ), 141 `anim_duration` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `add_widget()` ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), 139 _method_ ), 140 `animated_hero_in()` ( _kivymd.uix.transition.transition.MDTransitionBase_ `add_widget()` ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 430 _method_ ), 230 `animated_hero_out() add_widget()` ( _kivymd.uix.tooltip.tooltip.MDTooltip_ ( _kivymd.uix.transition.transition.MDTransitionBase method_ ), 197 _method_ ), 430 `adjust_height()` ( _kivymd.uix.textfield.textfield.MDTextField_ `animation` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 231 _attribute_ ), 512 `adjust_pos()` ( _kivymd.uix.button.button.MDButton_ `animation_duration` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker method_ ), 304 _attribute_ ), 321 `adjust_position()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `animation_tooltip_dismiss()` _method_ ), 404 ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), `adjust_segment_radius()` 197 ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton_ `animation_tooltip_show()` _method_ ), 429 ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), `adjust_tooltip_position()` 197 ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), `animation_transition` 197 ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `adjust_width()` ( _kivymd.uix.button.button.MDButton attribute_ ), 321 _method_ ), 305 `apply_state()` ( _kivymd.tools.hotreload.app.MDApp_ `adjust_width()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 701 

**Index** 

**734** 

**KivyMD, Release 2.0.1.dev0** 

`appname` ( _kivymd.tools.hotreload.app.MDApp property_ ), `background_origin` ( 699 _attribute_ ), 671 `approx_normailzer` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `backgroundColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 68 _attribute_ ), 51 `ArgumentParserWithHelp` ( _class in_ `BackgroundColorBehavior` ( _class in kivymd.tools.argument_parser_ ), 696 _kivymd.uix.behaviors.backgroundcolor_behavior_ ), `auto_dismiss` ( _kivymd.uix.dialog.dialog.MDDialog at-_ 670 _tribute_ ), 590 `bar_is_hidden` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `auto_dismiss` ( _kivymd.uix.snackbar.snackbar.MDSnackbar attribute_ ), 513 _attribute_ ), 486 `bars()` ( `auto_dismiss` ( _kivymd.uix.tooltip.tooltip.MDTooltipRich method_ ), 720 _attribute_ ), 198 `bars()` ( `AutoFormatTelephoneNumber` ( _class in method_ ), 719 _kivymd.uix.textfield.textfield_ ), 211 `bars()` ( `AUTORELOADER_IGNORE_PATTERNS` _method_ ), 718 ( _kivymd.tools.hotreload.app.MDApp attribute_ ), `bars()` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimator_ 700 _method_ ), 717 `AUTORELOADER_PATHS` ( _kivymd.tools.hotreload.app.MDApp_ `BaseButton` ( _class in kivymd.uix.button.button_ ), 303 _attribute_ ), 699 `BaseDropdownItem` ( _class in kivymd.uix.menu.menu_ ), 398 B `BaseFabButton` ( _class in kivymd.uix.button.button_ ), 303 `back()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `BaseListItem` ( _class in kivymd.uix.list.list_ ), 412 _method_ ), 261 `BaseListItemIcon` ( _class in kivymd.uix.list.list_ ), 413 `background` ( _kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior_ `BaseListItemText` ( _class in kivymd.uix.list.list_ ), 412 _attribute_ ), 670 `BaseNavigationDrawerItem` ( _class in_ `background_color` ( _kivymd.uix.datatables.datatables.MDDataTablekivymd.uix.navigationdrawer.navigationdrawer_ ), _attribute_ ), 178 534 `background_color` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `BaseTextFieldIcon` ( _class in attribute_ ), 403 _kivymd.uix.textfield.textfield_ ), 216 `background_color` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `BaseTextFieldLabel` ( _class in attribute_ ), 539 _kivymd.uix.textfield.textfield_ ), 211 `background_color` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `bind_key()` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), 493 _method_ ), 701 `background_color` ( _kivymd.uix.snackbar.snackbar.MDSnackbar_ `body` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect attribute_ ), 486 _attribute_ ), 674 `background_color_cell border_margin` ( _kivymd.uix.menu.menu.MDDropdownMenu_ ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 401 _attribute_ ), 180 `build()` ( _kivymd.tools.hotreload.app.MDApp method_ ), `background_color_header` 700 ( _kivymd.uix.datatables.datatables.MDDataTable_ `build_app()` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), 180 _method_ ), 700 `background_color_selected_cell button_centering_animation()` ( _kivymd.uix.datatables.datatables.MDDataTable_ ( _kivymd.uix.appbar.appbar.MDBottomAppBar attribute_ ), 181 _method_ ), 513 `background_color_selection_button button_elevated_opacity_value_disabled_container` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 257 _attribute_ ), 666 `background_color_toolbar button_elevated_opacity_value_disabled_icon` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 258 _attribute_ ), 666 `background_down` ( _kivymd.uix.behaviors.toggle_behavior.MDToggleButtonBehavior_ `button_elevated_opacity_value_disabled_text` _attribute_ ), 624 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `background_normal` ( _kivymd.uix.behaviors.toggle_behavior.MDToggleButtonBehaviorattribute_ ), 666 _attribute_ ), 624 `button_filled_opacity_value_disabled_container` 

**Index** 

**735** 

**KivyMD, Release 2.0.1.dev0** 

( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 666 _attribute_ ), 665 `card_opacity_value_disabled_state_elevated_container button_filled_opacity_value_disabled_icon` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 666 _attribute_ ), 665 `card_outlined_opacity_value_disabled_state_container button_filled_opacity_value_disabled_text` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 666 _attribute_ ), 665 `catching_determinate_duration button_outlined_opacity_value_disabled_container` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 376 _attribute_ ), 666 `catching_determinate_transition button_outlined_opacity_value_disabled_icon` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 376 _attribute_ ), 666 `catching_indeterminate_duration button_outlined_opacity_value_disabled_line` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 376 _attribute_ ), 666 `catching_indeterminate_transition button_outlined_opacity_value_disabled_text` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 376 _attribute_ ), 666 `catching_up()` ( `button_text_opacity_value_disabled_icon` _method_ ), 377 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `cbrt` ( _in module kivymd.utils.cubic_bezier_ ), 725 _attribute_ ), 666 `change_month()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `button_text_opacity_value_disabled_text` _method_ ), 339 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `check` ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 666 _attribute_ ), 175 `button_tonal_opacity_value_disabled_container check_all_rows()` ( _kivymd.uix.datatables.datatables.MDDataTable_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviormethod_ ), 184 _attribute_ ), 665 `check_determinate() button_tonal_opacity_value_disabled_icon` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviormethod_ ), 378 _attribute_ ), 666 `check_hor_growth()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `button_tonal_opacity_value_disabled_text` _method_ ), 404 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `check_scroll_direction()` _attribute_ ), 666 ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 513 C `check_size()` ( `calendar_layout` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickermethod_ ), 376 _attribute_ ), 339 `check_transition()` ( _kivymd.uix.screenmanager.MDScreenManager_ `call_ripple_animation_methods()` _method_ ), 55 ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `check_ver_growth()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 644 _method_ ), 404 `call_ripple_animation_methods() checkbox_icon_down` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple attribute_ ), 609 _method_ ), 646 `checkbox_icon_normal caller` ( _kivymd.uix.menu.menu.MDDropdownMenu at-_ ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox tribute_ ), 403 _attribute_ ), 609 `can_stretch_touch() checkbox_opacity_value_disabled_container` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior method_ ), 68 _attribute_ ), 666 `cancel_selection()` ( _kivymd.uix.label.label.MDLabel_ `chip_opacity_value_disabled_container` _method_ ), 464 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `card_filled_opacity_value_disabled_state_container` _attribute_ ), 666 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `chip_opacity_value_disabled_icon` 

**Index** 

**736** 

**KivyMD, Release 2.0.1.dev0** 

( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 553 _attribute_ ), 666 `closing_transition` ( `chip_opacity_value_disabled_text` _attribute_ ), 539 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `collapse()` ( _kivymd.uix.behaviors.motion_behavior.MotionExtendedFabButtonBehavior attribute_ ), 666 _method_ ), 669 `circle_color` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout_ `color` ( _kivymd.uix.divider.divider.MDDivider attribute_ ), _attribute_ ), 266 518 `circular_padding` ( _kivymd.uix.circularlayout.MDCircularLayout_ `color` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator attribute_ ), 73 _attribute_ ), 377 `circular_radius` ( _kivymd.uix.circularlayout.MDCircularLayout_ `color_active` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox attribute_ ), 73 _attribute_ ), 609 `CircularIndeterminateAdvancedAnimator` ( _class_ `color_array` ( _in kivymd.uix.exprogressindicator.animators_ ), _attribute_ ), 156 719 `color_deselection` ( _kivymd.uix.label.label.MDLabel_ `CircularIndeterminateRetreatAnimator` ( _class attribute_ ), 464 _in kivymd.uix.exprogressindicator.animators_ ), `color_disabled` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ 718 _attribute_ ), 610 `CircularRippleBehavior` ( _class in_ `color_inactive` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox kivymd.uix.behaviors.ripple_behavior_ ), 645 _attribute_ ), 609 `CircularRippleBehavior` ( _in module_ `color_map` ( _kivymd.uix.button.button.BaseFabButton atkivymd.uix.behaviors.ripple_behavior_ ), 646 _tribute_ ), 303 `clamp()` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `color_obj()` ( _method_ ), 68 _method_ ), 156 `clamp_range()` ( _kivymd.utils.cubic_bezier.CubicBezier_ `color_selection` ( _kivymd.uix.label.label.MDLabel atmethod_ ), 725 _tribute_ ), 464 `CLASSES` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), `color_to_rgba()` ( _kivymd.theming.ThemeManager_ 700 _method_ ), 21 `cleanup_lines()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicator_ `column_data` ( _kivymd.uix.datatables.datatables.MDDataTable method_ ), 157 _attribute_ ), 161 `clear_all_checks()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `command()` ( _in module method_ ), 184 _kivymd.tools.release.git_commands_ ), 711 `clockwise` ( _kivymd.uix.circularlayout.MDCircularLayout_ `CommonElevationBehavior` ( _class in attribute_ ), 74 _kivymd.uix.behaviors.elevation_ ), 632 `close()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ `CommonRipple` ( _class in method_ ), 553 _kivymd.uix.behaviors.ripple_behavior_ ), 642 `close()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `compare_date_range()` _method_ ), 261 ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `close_card()` ( _kivymd.uix.card.card.MDCardSwipe method_ ), 339 _method_ ), 576 `complete_anim_ripple() close_on_click` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ ( _kivymd.uix.chip.chip.MDChip method_ ), _attribute_ ), 538 368 `close_to()` ( _kivymd.utils.cubic_bezier.CubicBezier_ `compute_bar()` ( _method_ ), 725 _method_ ), 717 `close_view()` ( _kivymd.uix.search.search.MDSearchBar_ `compute_inactive_segments()` _method_ ), 479 ( `closing_interval` ( _kivymd.uix.card.card.MDCardSwipe method_ ), 157 _attribute_ ), 575 `CONSTANT_ROTATION_DEGREES closing_time` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ ( _attribute_ ), 553 _attribute_ ), 720 `closing_time` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `CONSTANT_ROTATION_DEGREES` _attribute_ ), 539 ( `closing_transition` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), 718 _attribute_ ), 575 `container_color` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicator_ `closing_transition` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanelattribute_ ), 145 

**Index** 

**737** 

**KivyMD, Release 2.0.1.dev0** 

`convert_overscroll() DELAY_EXPAND` ( ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 719 _method_ ), 68 `DELAY_FADE_IN` ( `create_argument_parser()` ( _in module attribute_ ), 719 _kivymd.tools.release.make_release_ ), 712 `DELAY_SPINS_MS` ( `create_clock()` ( _kivymd.uix.behaviors.touch_behavior.TouchBehaviorattribute_ ), 718 _method_ ), 664 `DELAY_TO_MOVE_SEGMENT_ENDS create_pagination_menu()` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimator_ ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 716 _method_ ), 189 `delete_clock()` ( _kivymd.uix.behaviors.touch_behavior.TouchBehavior_ `create_unreleased_changelog()` ( _in module method_ ), 664 _kivymd.tools.release.make_release_ ), 712 `delete_clock()` ( _kivymd.uix.tooltip.tooltip.MDTooltip_ `CubicBezier` ( _class in kivymd.utils.cubic_bezier_ ), 725 _method_ ), 197 `current_hero` ( _kivymd.uix.screenmanager.MDScreenManager_ `delete_doc_from_collection()` _attribute_ ), 55 ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBase_ `current_heroes` ( _kivymd.uix.screenmanager.MDScreenManager method_ ), 710 _attribute_ ), 55 `desktop_view` ( _kivymd.uix.responsivelayout.MDResponsiveLayout_ `current_indices` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateContiguousAnimatorattribute_ ), 83 _attribute_ ), 717 `detect_visible` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior_ `current_path` ( _kivymd.uix.filemanager.filemanager.MDFileManagerattribute_ ), 654 _attribute_ ), 260 `determinate` ( `current_schemes_color_data` _attribute_ ), 156 ( _kivymd.dynamic_color.DynamicColor at-_ `determinate` ( _tribute_ ), 47 _attribute_ ), 377 `determinate_time` ( D _attribute_ ), 377 `DataBase` ( _class in kivymd.tools.patterns.MVC.Model.database_firebase_ `DEVICE_IOS` ), ( _in module kivymd.material_resources_ ), 694 709 `device_ios` ( _kivymd.theming.ThemableBehavior at-_ `DataBase` ( _class in kivymd.tools.patterns.MVC.Model.database_restdbtribute_ ), ), 22 710 `device_orientation` ( _kivymd.theming.ThemeManager_ `datas` ( _in module kivymd.tools.packaging.pyinstaller.hookattribute_ ), 17 _kivymd_ ), 703 `DEVICE_TYPE` ( _in module kivymd.material_resources_ ), `date_format` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ 694 _attribute_ ), 341 `disable_animation` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `date_format` ( _kivymd.uix.textfield.textfield.Validator atattribute_ ), 610 _tribute_ ), 211 `disable_animation` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `date_interval` ( _kivymd.uix.textfield.textfield.Validator attribute_ ), 614 _attribute_ ), 211 `disabled_color` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `datetime_date` ( _kivymd.uix.textfield.textfield.Validator attribute_ ), 610 _attribute_ ), 211 `disabled_hint_text_color day` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ ( _kivymd.theming.ThemeManager attribute_ ), 16 _attribute_ ), 338 `disabledTextColor` ( _kivymd.dynamic_color.DynamicColor_ `DEBUG` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), _attribute_ ), 52 699 `dismiss()` ( _kivymd.uix.dialog.dialog.MDDialog_ `DeclarativeBehavior` ( _class in method_ ), 591 _kivymd.uix.behaviors.declarative_behavior_ ), `dismiss()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ 660 _method_ ), 405 `default_input_date` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ `dismiss()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 341 _method_ ), 339 `degree_spacing` ( _kivymd.uix.circularlayout.MDCircularLayout_ `dismiss()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker attribute_ ), 73 _method_ ), 322 `DELAY_COLLAPSE` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `dismiss()` ( _kivymd.uix.snackbar.snackbar.MDSnackbar attribute_ ), 719 _method_ ), 486 `dismiss()` ( _kivymd.uix.tooltip.tooltip.MDTooltipRich_ 

**Index** 

**738** 

**KivyMD, Release 2.0.1.dev0** 

_method_ ), 198 _attribute_ ), 664 `displacement` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `duration_normailzer` _attribute_ ), 675 ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `display_tooltip()` ( _kivymd.uix.tooltip.tooltip.MDTooltip attribute_ ), 68 _method_ ), 197 `DURATION_PER_CYCLE_IN_MS divider` ( _kivymd.uix.list.list.BaseListItem attribute_ ), 412 ( `divider` ( _kivymd.uix.menu.menu.BaseDropdownItem atattribute_ ), 717 _tribute_ ), 399 `DURATION_SHRINK_MS` ( `divider_color` ( _kivymd.uix.list.list.BaseListItem atattribute_ ), 718 _tribute_ ), 412 `DURATION_SPIN_MS` ( `divider_color` ( _kivymd.uix.menu.menu.BaseDropdownItem attribute_ ), 718 _attribute_ ), 399 `DURATION_TO_MOVE_SEGMENT_ENDS divider_width` ( _kivymd.uix.divider.divider.MDDivider_ ( _attribute_ ), 519 _attribute_ ), 716 `do_autoscroll_tabs() dynamic_color` ( _kivymd.theming.ThemeManager_ ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), _attribute_ ), 9 140 `dynamic_color_names do_backspace()` ( _kivymd.uix.textfield.textfield.AutoFormatTelephoneNumber_ ( _kivymd.theming.ThemeManager attribute_ ), 19 _method_ ), 211 `dynamic_color_quality do_layout()` ( _kivymd.uix.circularlayout.MDCircularLayout_ ( _kivymd.theming.ThemeManager attribute_ ), 9 _method_ ), 74 `dynamic_scheme_contrast do_selection()` ( _kivymd.uix.label.label.MDLabel_ ( _kivymd.theming.ThemeManager attribute_ ), 12 _method_ ), 464 `dynamic_scheme_name docked` ( _kivymd.uix.search.search.MDSearchBar at-_ ( _kivymd.theming.ThemeManager attribute_ ), 12 _tribute_ ), 477 `DynamicColor` ( _class in kivymd.dynamic_color_ ), 47 `docked_height` ( _kivymd.uix.search.search.MDSearchBar attribute_ ), 477 E `docked_width` ( _kivymd.uix.search.search.MDSearchBar_ `easing_accelerated` ( _kivymd.animation.MDAnimationTransition attribute_ ), 477 _attribute_ ), 41 `download_file()` ( _in module_ `easing_decelerated` ( _kivymd.animation.MDAnimationTransition kivymd.tools.release.update_icons_ ), 713 _attribute_ ), 41 `dp` ( _in module kivymd.material_resources_ ), 694 `easing_emphasized() drag_handle_color` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheetDragHandle_ ( _kivymd.animation.MDAnimationTransition attribute_ ), 442 _method_ ), 41 `drag_threshold` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `easing_linear` ( _kivymd.animation.MDAnimationTransition attribute_ ), 674 _attribute_ ), 41 `drawer_type` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `easing_standard` ( _kivymd.animation.MDAnimationTransition attribute_ ), 537 _attribute_ ), 41 `duration` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicator_ `edit_data()` ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBase attribute_ ), 144 _method_ ), 710 `duration` ( _kivymd.uix.snackbar.snackbar.MDSnackbar_ `effect_cls` ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 486 _attribute_ ), 181 `duration` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ `elevation` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior attribute_ ), 431 _attribute_ ), 632 `DURATION_COLLAPSE` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `elevation_level` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior attribute_ ), 719 _attribute_ ), 632 `DURATION_EXPAND` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `elevation_level` ( _attribute_ ), 719 _attribute_ ), 539 `DURATION_FADE_IN` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `elevation_levels` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior attribute_ ), 719 _attribute_ ), 632 `DURATION_GROW_MS` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateRetreatAnimator_ `elevation_levels` ( _kivymd.uix.button.button.BaseButton attribute_ ), 718 _attribute_ ), 303 `duration_long_touch elevation_levels` ( _kivymd.uix.button.button.BaseFabButton_ ( _kivymd.uix.behaviors.touch_behavior.TouchBehavior attribute_ ), 303 

**Index** 

**739** 

**KivyMD, Release 2.0.1.dev0** 

`elevation_levels` ( _kivymd.uix.button.button.MDExtendedFabButton_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 306 _attribute_ ), 665 `enable_autoreload() fab_state` ( _kivymd.uix.button.button.BaseFabButton at-_ ( _kivymd.tools.hotreload.app.MDApp method_ ), _tribute_ ), 303 701 `fade_out()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `enable_swiping` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawermethod_ ), 644 _attribute_ ), 539 `fbind()` ( _kivymd.tools.patterns.MVC.libs.translation.Translation_ `END_FRACTION_RANGE` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateRetreatAnimatormethod_ ), 710 _attribute_ ), 718 `field_filter()` ( _kivymd.uix.textfield.textfield.AutoFormatTelephoneNumber_ `enter_point` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior method_ ), 211 _attribute_ ), 654 `fill_color_focus` ( _kivymd.uix.textfield.textfield.MDTextField_ `error` ( _kivymd.uix.textfield.textfield.MDTextField atattribute_ ), 223 _tribute_ ), 220 `fill_color_normal` ( _kivymd.uix.textfield.textfield.MDTextField_ `error()` ( _kivymd.tools.argument_parser.ArgumentParserWithHelp attribute_ ), 223 _method_ ), 697 `find_first_cubic_root() error_color` ( _kivymd.uix.textfield.textfield.MDTextField_ ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 220 _method_ ), 726 `error_text` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ `finish_ripple()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple attribute_ ), 341 _method_ ), 644 `errorColor` ( _kivymd.dynamic_color.DynamicColor at-_ `finish_ripple()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple tribute_ ), 51 _method_ ), 646 `errorContainerColor finish_ripple()` ( _kivymd.uix.button.button.BaseButton_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 304 _tribute_ ), 51 `fit_mode` ( _kivymd.uix.fitimage.fitimage.FitImage at-_ `errorDimColor` ( _kivymd.dynamic_color.DynamicColor tribute_ ), 556 _attribute_ ), 51 `FitImage` ( _class in kivymd.uix.fitimage.fitimage_ ), 556 `errorPaletteKeyColorColor float_epsilon` ( _in module kivymd.utils.cubic_bezier_ ), ( _kivymd.dynamic_color.DynamicColor at-_ 725 _tribute_ ), 52 `focus_behavior` ( _kivymd.uix.behaviors.focus_behavior.StateFocusBehavior_ `evaluate_cubic()` ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 621 _method_ ), 725 `focus_color` ( _kivymd.uix.behaviors.focus_behavior.StateFocusBehavior_ `ExceptionClass` ( _class in kivymd.tools.hotreload.app_ ), _attribute_ ), 621 699 `FocusBehavior` ( _class in_ `exit_manager` ( _kivymd.uix.filemanager.filemanager.MDFileManagerkivymd.uix.behaviors.focus_behavior_ ), 621 _attribute_ ), 260 `follow_system_theme expand()` ( _kivymd.uix.behaviors.motion_behavior.MotionExtendedFabButtonBehavior_ ( _kivymd.theming.ThemeManager attribute_ ), 15 _method_ ), 669 `font_color_down` ( _kivymd.uix.behaviors.toggle_behavior.MDToggleButtonBehavior_ `exponential_scalar` ( _kivymd.uix.scrollview.StretchOverScrollStencilattribute_ ), 624 _attribute_ ), 68 `font_color_normal` ( `export_icon_definitions()` ( _in module attribute_ ), 624 _kivymd.tools.release.update_icons_ ), 713 `font_path` ( _in module_ `ext` ( _kivymd.uix.filemanager.filemanager.MDFileManager kivymd.tools.release.update_icons_ ), 712 _attribute_ ), 260 `font_style` ( _kivymd.uix.label.label.MDLabel attribute_ ), `EXTRA_DEGREES_PER_CYCLE` 463 ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `font_style` ( _kivymd.uix.textfield.textfield.MDTextField attribute_ ), 719 _attribute_ ), 219 `font_styles` ( _kivymd.theming.ThemeManager at-_ F _tribute_ ), 17 `fab_button` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ `font_version` ( _in module attribute_ ), 249 _kivymd.tools.release.update_icons_ ), 712 `fab_button_opacity_value_disabled_container fonts` ( _in module kivymd.font_definitions_ ), 36 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `fonts_path` ( _in module kivymd_ ), 694 _attribute_ ), 665 `FOREGROUND_LOCK` ( _kivymd.tools.hotreload.app.MDApp_ `fab_button_opacity_value_disabled_icon` _attribute_ ), 699 

**Index** 

**740** 

**KivyMD, Release 2.0.1.dev0** 

`format()` ( _kivymd.uix.textfield.textfield.AutoFormatTelephoneNumber_ `get_component()` ( _kivymd.uix.scrollview.StretchOverScrollStencil method_ ), 211 _method_ ), 68 `format_help()` ( _kivymd.tools.argument_parser.ArgumentParserWithHelp_ `get_connect()` ( _in module method_ ), 697 _kivymd.tools.patterns.MVC.Model.database_firebase_ ), `FpsMonitor` ( _class in kivymd.utils.fpsmonitor_ ), 727 709 `full_screen_radius` ( _kivymd.uix.carousel.carousel.MDCarouselItem_ `get_connect()` ( _in module attribute_ ), 282 _kivymd.tools.patterns.MVC.Model.database_restdb_ ), `funbind()` ( _kivymd.tools.patterns.MVC.libs.translation.Translation_ 710 _method_ ), 710 `get_content()` ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 261 G `get_current_date_from_format() generate_list_widgets_days()` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickermethod_ ), 341 _method_ ), 339 `get_current_index() generate_list_widgets_days()` ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ 203 _method_ ), 341 `get_current_item()` ( _kivymd.uix.swiper.swiper.MDSwiper_ `generate_list_widgets_years()` _method_ ), 203 ( _kivymd.uix.pickers.datepicker.datepicker.MDModalDatePicker_ `get_current_related_content()` _method_ ), 340 ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), `generate_menu_month_year_selection()` 141 ( _kivymd.uix.pickers.datepicker.datepicker.MDDockedDatePicker_ `get_current_tab()` ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), 340 _method_ ), 141 `get_access_string() get_data_from_collection()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ ( _kivymd.tools.patterns.MVC.Model.database_firebase.DataBase method_ ), 261 _method_ ), 709 `get_active_item()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationBar_ `get_data_from_collection()` _method_ ), 278 ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBase_ `get_adjusted_pos_helper_text_label()` _method_ ), 710 ( _kivymd.uix.textfield.textfield.MDTextField_ `get_date()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 230 _method_ ), 339 `get_adjusted_pos_hint_text_label() get_date()` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 341 _method_ ), 230 `get_dist_from_side() get_adjusted_pos_leading_icon()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 540 _method_ ), 230 `get_fraction_in_range() get_adjusted_pos_max_length_label()` ( ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 720 _method_ ), 230 `get_fraction_in_range() get_adjusted_pos_trailing_icon()` ( ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 718 _method_ ), 230 `get_fraction_in_range() get_amplitude()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ ( _method_ ), 157 _method_ ), 718 `get_angle()` ( _kivymd.uix.circularlayout.MDCircularLayout_ `get_fraction_in_range()` _method_ ), 74 ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimator_ `get_arc_points()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExCircularProgressIndicatormethod_ ), 717 _method_ ), 158 `get_hero_from_widget() get_checked_row_indices()` ( _kivymd.uix.screenmanager.MDScreenManager_ ( _kivymd.uix.datatables.datatables.MDDataTable method_ ), 55 _method_ ), 184 `get_hook_dirs()` ( _in module_ `get_color()` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimatorkivymd.tools.packaging.pyinstaller_ ), 702 _method_ ), 720 `get_hw()` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ 

**Index** 

**741** 

**KivyMD, Release 2.0.1.dev0** 

_method_ ), 68 _kivymd.tools.release.git_commands_ ), 711 `get_icons_list()` ( _in module_ `git_push()` ( _in module kivymd.tools.release.update_icons_ ), 713 _kivymd.tools.release.git_commands_ ), 711 `get_ids()` ( _kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior_ `git_tag()` ( _in module method_ ), 663 _kivymd.tools.release.git_commands_ ), 711 `get_items()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ `glsl_path` ( _in module kivymd_ ), 694 _method_ ), 249 `grow()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior_ `get_items()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonmethod_ ), 651 _method_ ), 429 `get_items()` ( _kivymd.uix.swiper.swiper.MDSwiper_ H _method_ ), 203 `handle_anim_duration get_last_scroll_x()` ( _kivymd.uix.slider.slider.MDSlider attribute_ ), ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), 544 140 `handle_anim_transition get_marked_items()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton_ ( _kivymd.uix.slider.slider.MDSlider attribute_ ), _method_ ), 429 544 `get_norm_value()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `handle_exception()` ( _kivymd.tools.hotreload.app.ExceptionClass method_ ), 156 _method_ ), 699 `get_previous_version()` ( _in module_ `header_cls` ( _kivymd.uix.menu.menu.MDDropdownMenu kivymd.tools.release.git_commands_ ), 711 _attribute_ ), 400 `get_pyinstaller_tests()` ( _in module_ `headline_text` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker kivymd.tools.packaging.pyinstaller_ ), 702 _attribute_ ), 321 `get_real_device_type() height` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ ( _kivymd.uix.controllers.windowcontroller.WindowControllerattribute_ ), 611 _method_ ), 616 `hero_to` ( _kivymd.uix.screen.MDScreen attribute_ ), 79 `get_rect_instruction() heroes_to` ( _kivymd.uix.screen.MDScreen attribute_ ), 79 ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), `hide_appbar` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ 140 _attribute_ ), 494 `get_root()` ( _kivymd.tools.hotreload.app.MDApp_ `hide_bar()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 700 _method_ ), 513 `get_root_path()` ( _kivymd.tools.hotreload.app.MDApp_ `hide_child()` ( _kivymd.uix.search.search.MDSearchViewContainer method_ ), 700 _method_ ), 477 `get_row_checks()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `hide_duration` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 189 _attribute_ ), 512 `get_segment_coords() hide_duration` ( _kivymd.uix.behaviors.motion_behavior.MotionBase_ ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicatorattribute_ ), 668 _method_ ), 157 `hide_duration` ( `get_shape_names()` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicatorattribute_ ), 669 _method_ ), 145 `hide_duration` ( `get_slides_list()` ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), 267 _method_ ), 141 `hide_transition` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `get_start_and_end()` _attribute_ ), 512 ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExCircularProgressIndicator_ `hide_transition` ( _kivymd.uix.behaviors.motion_behavior.MotionBase method_ ), 158 _attribute_ ), 668 `get_tabs_list()` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `hide_transition` ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior method_ ), 140 _attribute_ ), 669 `get_target_pos()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `hide_transition` ( _method_ ), 404 _attribute_ ), 668 `get_window_width_resizing_direction() hide_transition` ( ( _kivymd.uix.controllers.windowcontroller.WindowControllerattribute_ ), 669 _method_ ), 616 `hide_transition` ( `git_clean()` ( _in module attribute_ ), 267 _kivymd.tools.release.git_commands_ ), 711 `hiding_icon_duration git_commit()` ( _in module_ 

**Index** 

**742** 

**KivyMD, Release 2.0.1.dev0** 

_attribute_ ), 428 `icon_color` ( _kivymd.uix.label.label.MDIcon attribute_ ), `hiding_icon_transition` 465 ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton_ `icon_color` ( _kivymd.uix.list.list.BaseListItemIcon attribute_ ), 428 _attribute_ ), 413 `hooks_path` ( _in module_ `icon_color_active` ( _kivymd.tools.packaging.pyinstaller_ ), 702 _attribute_ ), 277 `hor_growth` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `icon_color_disabled` _attribute_ ), 402 ( _kivymd.uix.button.button.BaseFabButton_ `hour` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker attribute_ ), 303 _attribute_ ), 320 `icon_color_disabled` ( _kivymd.uix.label.label.MDIcon_ `hover_visible` ( _kivymd.uix.behaviors.hover_behavior.HoverBehaviorattribute_ ), 465 _attribute_ ), 654 `icon_color_disabled HoverBehavior` ( _class in_ ( _kivymd.uix.list.list.BaseListItemIcon attribute_ ), _kivymd.uix.behaviors.hover_behavior_ ), 654 413 `hovering` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior_ `icon_color_focus` ( _kivymd.uix.textfield.textfield.BaseTextFieldIcon attribute_ ), 654 _attribute_ ), 217 `icon_color_normal` ( I _attribute_ ), 277 `icon` ( _kivymd.app.MDApp attribute_ ), 26 `icon_color_normal` ( _kivymd.uix.textfield.textfield.BaseTextFieldIcon_ `icon` ( _kivymd.icon_definitions.IconItem attribute_ ), 32 _attribute_ ), 216 `icon` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `icon_definitions_path` ( _in module attribute_ ), 256 _kivymd.tools.release.update_icons_ ), 712 `icon` ( _kivymd.uix.label.label.MDIcon attribute_ ), 465 `icon_folder` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `icon_active` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitchattribute_ ), 259 _attribute_ ), 611 `icon_inactive` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `icon_active_color` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitchattribute_ ), 611 _attribute_ ), 612 `icon_inactive_color icon_button_filled_opacity_value_disabled_container` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 612 _attribute_ ), 665 `icon_selection_button icon_button_filled_opacity_value_disabled_icon` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 256 _attribute_ ), 665 `IconItem` ( _class in kivymd.icon_definitions_ ), 32 `icon_button_outlined_opacity_value_disabled_containerid` ( _kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 660 _attribute_ ), 665 `IDLE_DETECTION` ( _kivymd.tools.hotreload.app.MDApp_ `icon_button_outlined_opacity_value_disabled_icon` _attribute_ ), 700 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `IDLE_TIMEOUT` ( _kivymd.tools.hotreload.app.MDApp atattribute_ ), 665 _tribute_ ), 700 `icon_button_outlined_opacity_value_disabled_lineimages_path` ( _in module kivymd_ ), 694 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `inactive_indicator_color` _attribute_ ), 665 ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerItem_ `icon_button_standard_opacity_value_disabled_icon` _attribute_ ), 535 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `inactive_track_color` _attribute_ ), 665 ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `icon_button_tonal_opacity_value_disabled_container` _attribute_ ), 156 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `indeterminate_animator` _attribute_ ), 665 ( `icon_button_tonal_opacity_value_disabled_icon` _attribute_ ), 157 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `indeterminate_animator` _attribute_ ), 665 ( `icon_color` ( _kivymd.uix.filemanager.filemanager.MDFileManager attribute_ ), 157 _attribute_ ), 259 `index` ( _kivymd.uix.carousel.carousel.MDCarousel attribute_ ), 286 

**Index** 

**743** 

**KivyMD, Release 2.0.1.dev0** 

`indicator` ( _kivymd.uix.tab.tab.MDTabsPrimary at-_ `is_number_valid()` ( _kivymd.uix.textfield.textfield.Validator tribute_ ), 140 _method_ ), 211 `indicator_anim` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `is_open` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel attribute_ ), 139 _attribute_ ), 553 `indicator_color` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem_ `is_open` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 277 _attribute_ ), 339 `indicator_color` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ `is_open` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker attribute_ ), 375 _attribute_ ), 321 `indicator_duration` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem_ `is_row_checked()` ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 277 _method_ ), 184 `indicator_duration` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `is_selected` ( _kivymd.uix.label.label.MDLabel atattribute_ ), 139 _tribute_ ), 464 `indicator_height` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `is_time_valid()` ( _kivymd.uix.textfield.textfield.Validator attribute_ ), 139 _method_ ), 211 `indicator_height` ( _kivymd.uix.tab.tab.MDTabsSecondary_ `is_top_or_bottom()` ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 142 _method_ ), 68 `indicator_radius` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `isnumeric()` ( _kivymd.uix.textfield.textfield.AutoFormatTelephoneNumber attribute_ ), 139 _method_ ), 211 `indicator_radius` ( _kivymd.uix.tab.tab.MDTabsSecondary_ `item_snapping` ( _kivymd.uix.carousel.carousel.MDCarousel attribute_ ), 142 _attribute_ ), 285 `indicator_transition items` ( _kivymd.uix.menu.menu.MDDropdownMenu at-_ ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItemtribute_ ), 400 _attribute_ ), 277 `items_spacing` ( _kivymd.uix.swiper.swiper.MDSwiper_ `indicator_transition` _attribute_ ), 201 ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), 139 K `init_fbos()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `kivymd` _method_ ), 646 `module` , 693 `install_idle()` ( _kivymd.tools.hotreload.app.MDApp_ `kivymd.animation` _method_ ), 701 `module` , 37 `INTERPOLATOR` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimator_ `kivymd.app` _attribute_ ), 719 `module` , 24 `INTERPOLATOR` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateRetreatAnimator_ `kivymd.dynamic_color` _attribute_ ), 718 `module` , 42 `INTERPOLATOR` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateContiguousAnimator_ `kivymd.effects` _attribute_ ), 717 `module` , 695 `INTERPOLATORS` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimator_ `kivymd.effects.stiffscroll` _attribute_ ), 716 `module` , 695 `inverseOnSurfaceColor kivymd.effects.stiffscroll.stiffscroll` ( _kivymd.dynamic_color.DynamicColor at-_ `module` , 674 _tribute_ ), 51 `kivymd.factory_registers inversePrimaryColor module` , 694 ( _kivymd.dynamic_color.DynamicColor at-_ `kivymd.font_definitions` _tribute_ ), 51 `module` , 32 `inverseSurfaceColor kivymd.icon_definitions` ( _kivymd.dynamic_color.DynamicColor at-_ `module` , 27 _tribute_ ), 51 `kivymd.material_resources is_date_valid()` ( _kivymd.uix.textfield.textfield.Validator_ `module` , 694 _method_ ), 211 `kivymd.theming is_email_valid()` ( _kivymd.uix.textfield.textfield.Validator_ `module` , 7 _method_ ), 211 `kivymd.toast is_mouse_inside_widget() module` , 695 ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior_ `kivymd.toast.androidtoast` _method_ ), 655 `module` , 695 

**Index** 

**744** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.tools kivymd.uix.behaviors.backgroundcolor_behavior module` , 696 `module` , 670 `kivymd.tools.argument_parser kivymd.uix.behaviors.declarative_behavior module` , 696 `module` , 655 `kivymd.tools.hotreload kivymd.uix.behaviors.elevation module` , 697 `module` , 625 `kivymd.tools.hotreload.app kivymd.uix.behaviors.focus_behavior module` , 697 `module` , 619 `kivymd.tools.packaging kivymd.uix.behaviors.hover_behavior module` , 701 `module` , 652 `kivymd.tools.packaging.pyinstaller kivymd.uix.behaviors.magic_behavior module` , 701 `module` , 646 `kivymd.tools.packaging.pyinstaller.hook-kivymdkivymd.uix.behaviors.motion_behavior module` , 703 `module` , 667 `kivymd.tools.patterns kivymd.uix.behaviors.ripple_behavior module` , 703 `module` , 641 `kivymd.tools.patterns.add_view kivymd.uix.behaviors.rotate_behavior module` , 703 `module` , 639 `kivymd.tools.patterns.create_project kivymd.uix.behaviors.scale_behavior module` , 704 `module` , 616 `kivymd.tools.patterns.MVC kivymd.uix.behaviors.state_layer_behavior module` , 709 `module` , 664 `kivymd.tools.patterns.MVC.libs kivymd.uix.behaviors.stencil_behavior module` , 710 `module` , 672 `kivymd.tools.patterns.MVC.libs.translation kivymd.uix.behaviors.toggle_behavior module` , 710 `module` , 622 `kivymd.tools.patterns.MVC.Model kivymd.uix.behaviors.touch_behavior module` , 709 `module` , 663 `kivymd.tools.patterns.MVC.Model.database_firebasekivymd.uix.bottomsheet module` , 709 `module` , 714 `kivymd.tools.patterns.MVC.Model.database_restdbkivymd.uix.bottomsheet.bottomsheet module` , 710 `module` , 432 `kivymd.tools.release kivymd.uix.boxlayout module` , 711 `module` , 110 `kivymd.tools.release.git_commands kivymd.uix.button module` , 711 `module` , 714 `kivymd.tools.release.make_release kivymd.uix.button.button module` , 711 `module` , 288 `kivymd.tools.release.update_icons kivymd.uix.card module` , 712 `module` , 714 `kivymd.uix kivymd.uix.card.card module` , 713 `module` , 562 `kivymd.uix.anchorlayout kivymd.uix.carousel module` , 108 `module` , 715 `kivymd.uix.appbar kivymd.uix.carousel.carousel module` , 714 `module` , 279 `kivymd.uix.appbar.appbar kivymd.uix.chip module` , 496 `module` , 715 `kivymd.uix.badge kivymd.uix.chip.chip module` , 714 `module` , 341 `kivymd.uix.badge.badge kivymd.uix.circularlayout module` , 235 `module` , 71 `kivymd.uix.behaviors kivymd.uix.controllers module` , 714 `module` , 715 

**Index** 

**745** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.uix.controllers.windowcontroller kivymd.uix.loadingindicator module` , 615 `module` , 721 `kivymd.uix.datatables kivymd.uix.loadingindicator.loadingindicator module` , 715 `module` , 142 `kivymd.uix.datatables.datatables kivymd.uix.menu module` , 158 `module` , 721 `kivymd.uix.dialog kivymd.uix.menu.menu module` , 715 `module` , 378 `kivymd.uix.dialog.dialog kivymd.uix.navigationbar module` , 577 `module` , 721 `kivymd.uix.divider kivymd.uix.navigationbar.navigationbar module` , 715 `module` , 267 `kivymd.uix.divider.divider kivymd.uix.navigationdrawer module` , 514 `module` , 722 `kivymd.uix.dropdownitem kivymd.uix.navigationdrawer.navigationdrawer module` , 715 `module` , 519 `kivymd.uix.dropdownitem.dropdownitem kivymd.uix.navigationrail module` , 231 `module` , 722 `kivymd.uix.expansionpanel kivymd.uix.navigationrail.navigationrail module` , 716 `module` , 237 `kivymd.uix.expansionpanel.expansionpanel kivymd.uix.pickers module` , 546 `module` , 722 `kivymd.uix.exprogressindicator kivymd.uix.pickers.datepicker module` , 716 `module` , 722 `kivymd.uix.exprogressindicator.animators kivymd.uix.pickers.datepicker.datepicker module` , 716 `module` , 323 `kivymd.uix.exprogressindicator.exprogressindicatorkivymd.uix.pickers.timepicker module` , 145 `module` , 722 `kivymd.uix.filemanager kivymd.uix.pickers.timepicker.timepicker module` , 721 `module` , 308 `kivymd.uix.filemanager.filemanager kivymd.uix.progressindicator module` , 250 `module` , 722 `kivymd.uix.fitimage kivymd.uix.progressindicator.progressindicator module` , 721 `module` , 369 `kivymd.uix.fitimage.fitimage kivymd.uix.recycleboxlayout module` , 554 `module` , 60 `kivymd.uix.floatlayout kivymd.uix.recyclegridlayout module` , 69 `module` , 115 `kivymd.uix.gridlayout kivymd.uix.recycleview module` , 117 `module` , 74 `kivymd.uix.hero kivymd.uix.refreshlayout module` , 84 `module` , 722 `kivymd.uix.imagelist kivymd.uix.refreshlayout.refreshlayout module` , 721 `module` , 262 `kivymd.uix.imagelist.imagelist kivymd.uix.relativelayout module` , 592 `module` , 58 `kivymd.uix.label kivymd.uix.responsivelayout module` , 721 `module` , 79 `kivymd.uix.label.label kivymd.uix.screen module` , 444 `module` , 77 `kivymd.uix.list kivymd.uix.screenmanager module` , 721 `module` , 53 `kivymd.uix.list.list kivymd.uix.scrollview module` , 405 `module` , 62 

**Index** 

**746** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.uix.search module` , 722 `kivymd.uix.search.search module` , 466 `kivymd.uix.segmentedbutton module` , 723 `kivymd.uix.segmentedbutton.segmentedbutton module` , 414 `kivymd.uix.selectioncontrol module` , 723 `kivymd.uix.selectioncontrol.selectioncontrol module` , 600 `kivymd.uix.slider module` , 723 `kivymd.uix.slider.slider module` , 541 `kivymd.uix.sliverappbar module` , 723 `kivymd.uix.sliverappbar.sliverappbar module` , 487 `kivymd.uix.snackbar module` , 723 `kivymd.uix.snackbar.snackbar module` , 479 `kivymd.uix.stacklayout module` , 55 `kivymd.uix.swiper module` , 723 `kivymd.uix.swiper.swiper module` , 198 `kivymd.uix.tab module` , 723 `kivymd.uix.tab.tab module` , 119 `kivymd.uix.textfield module` , 724 `kivymd.uix.textfield.textfield module` , 204 `kivymd.uix.tooltip module` , 724 `kivymd.uix.tooltip.tooltip module` , 190 `kivymd.uix.transition module` , 724 `kivymd.uix.transition.transition module` , 430 `kivymd.uix.widget module` , 112 `kivymd.utils module` , 724 `kivymd.utils.cubic_bezier module` , 724 `kivymd.utils.fpsmonitor module` , 726 

`kivymd.utils.set_bars_colors module` , 727 `kivymd_path` ( _in module kivymd.tools.release.update_icons_ ), 712 `KV_DIRS` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), 699 `KV_FILES` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), 699 

L 

`label_only` ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), 138 `label_opacity_value_disabled_text` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 666 `last_cycle_count` ( _attribute_ ), 717 `last_scroll_x` ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), 139 `last_touch_pos` ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 68 `lay_canvas_instructions()` ( _kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior method_ ), 645 `lay_canvas_instructions()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple method_ ), 644 `lay_canvas_instructions()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple method_ ), 646 `lay_canvas_instructions()` ( _kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior method_ ), 645 `layouts` ( _kivymd.uix.carousel.carousel.MDCarousel attribute_ ), 285 `leading_icon` ( _kivymd.uix.menu.menu.BaseDropdownItem attribute_ ), 398 `leading_icon` ( _kivymd.uix.search.search.MDSearchBar attribute_ ), 477 `leading_icon_color` ( _kivymd.uix.menu.menu.BaseDropdownItem attribute_ ), 399 `len_palette` ( _attribute_ ), 718 `line_color` ( _attribute_ ), 671 `line_color` ( _kivymd.uix.button.button.BaseButton attribute_ ), 304 `line_color_disabled` ( _kivymd.uix.chip.chip.MDChip attribute_ ), 368 `line_color_disabled` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch attribute_ ), 614 `line_color_focus` ( _kivymd.uix.textfield.textfield.MDTextField attribute_ ), 222 

**Index** 

**747** 

**KivyMD, Release 2.0.1.dev0** 

`line_color_normal` ( _kivymd.uix.textfield.textfield.MDTextField_ `mark_today` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 221 _attribute_ ), 339 `line_width` ( _kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavi_ `max` ( _kivymd.effects.stiffscr_ **_o_** _rll.stiffscroll.StiffScrollEffect attribute_ ), 671 _attribute_ ), 674 `line_width` ( _kivymd.uix.button.button.BaseButton at-_ `max` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar tribute_ ), 304 _attribute_ ), 155 `line_width` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator_ `max_date` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 377 _attribute_ ), 338 `LinearIndeterminateContiguousAnimator` ( _class_ `max_degree` ( _kivymd.uix.circularlayout.MDCircularLayout in kivymd.uix.exprogressindicator.animators_ ), _attribute_ ), 73 717 `max_friction` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `LinearIndeterminateDisjointAnimator` ( _class in attribute_ ), 674 _kivymd.uix.exprogressindicator.animators_ ), `max_height` ( _kivymd.uix.menu.menu.MDDropdownMenu_ 716 _attribute_ ), 401 `list_opacity_value_disabled_container max_height` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 493 _attribute_ ), 666 `max_height` ( _kivymd.uix.textfield.textfield.MDTextField_ `list_opacity_value_disabled_leading_avatar` _attribute_ ), 224 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `max_opacity` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar attribute_ ), 666 _attribute_ ), 495 `load_all_kv_files()` ( _kivymd.app.MDApp method_ ), `max_opened_x` ( _kivymd.uix.card.card.MDCardSwipe at-_ 27 _tribute_ ), 575 `load_app_dependencies() max_swipe_x` ( _kivymd.uix.card.card.MDCardSwipe at-_ ( _kivymd.tools.hotreload.app.MDApp method_ ), _tribute_ ), 575 700 `max_text_length` ( _kivymd.uix.textfield.textfield.MDTextFieldMaxLengthText_ `lock_swiping` ( _kivymd.uix.tab.tab.MDTabsCarousel atattribute_ ), 215 _tribute_ ), 137 `max_year` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `lock_swiping` ( _kivymd.uix.tab.tab.MDTabsPrimary atattribute_ ), 338 _tribute_ ), 139 `maximum_velocity` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `LOOP_DELAY` ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateDisjointAnimatorattribute_ ), 67 _attribute_ ), 717 `md_bg_color` ( _attribute_ ), 670 M `md_bg_color` ( _kivymd.uix.button.button.BaseButton at-_ `M3CircularRippleBehavior` ( _class in tribute_ ), 304 _kivymd.uix.behaviors.ripple_behavior_ ), 646 `md_bg_color` ( _kivymd.uix.tab.tab.MDTabsPrimary at-_ `M3CommonRipple` ( _class in tribute_ ), 138 _kivymd.uix.behaviors.ripple_behavior_ ), 645 `md_bg_color_disabled M3RectangularRippleBehavior` ( _class in_ ( _kivymd.uix.appbar.appbar.MDActionTopAppBarButton kivymd.uix.behaviors.ripple_behavior_ ), 646 _attribute_ ), 510 `magic_speed` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior_ `md_bg_color_disabled` _attribute_ ), 651 ( _kivymd.uix.button.button.BaseButton at-_ `MagicBehavior` ( _class in tribute_ ), 304 _kivymd.uix.behaviors.magic_behavior_ ), 651 `md_bg_color_disabled main()` ( _in module kivymd.tools.patterns.add_view_ ), 704 ( _kivymd.uix.button.button.BaseFabButton_ `main()` ( _in module kivymd.tools.patterns.create_project_ ), _attribute_ ), 303 709 `md_bg_color_disabled main()` ( _in module kivymd.tools.release.make_release_ ), ( _kivymd.uix.button.button.MDIconButton_ 712 _attribute_ ), 306 `main()` ( _in module kivymd.tools.release.update_icons_ ), `md_bg_color_disabled` 713 ( _kivymd.uix.card.card.MDCard attribute_ ), `make_icon_definitions()` ( _in module_ 574 _kivymd.tools.release.update_icons_ ), 713 `md_bg_color_disabled mark_item()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton_ ( _kivymd.uix.list.list.BaseListItem attribute_ ), _method_ ), 429 412 

**Index** 

**748** 

**KivyMD, Release 2.0.1.dev0** 

`md_bg_color_disabled MDCheckbox` ( _class in kivymd.uix.selectioncontrol.selectioncontrol_ ), ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailFabButton_ 609 _attribute_ ), 247 `MDChip` ( _class in kivymd.uix.chip.chip_ ), 368 `md_bg_color_disabled MDChipLeadingAvatar` ( _class in kivymd.uix.chip.chip_ ), ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailMenuButton_ 367 _attribute_ ), 247 `MDChipLeadingIcon` ( _class in kivymd.uix.chip.chip_ ), `md_bg_color_disabled` 367 ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItem_ `MDChipText` ( _class in kivymd.uix.chip.chip_ ), 367 _attribute_ ), 427 `MDChipTrailingIcon` ( _class in kivymd.uix.chip.chip_ ), `md_bg_color_disabled` 367 ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `MDCircularLayout` ( _class in kivymd.uix.circularlayout_ ), _attribute_ ), 611 73 `md_icons` ( _in module kivymd.icon_definitions_ ), 32 `MDCircularProgressIndicator` ( _class in_ `MDActionBottomAppBarButton` ( _class in kivymd.uix.progressindicator.progressindicator_ ), _kivymd.uix.appbar.appbar_ ), 510 377 `MDActionTopAppBarButton` ( _class in_ `MDDataTable` ( _class in kivymd.uix.appbar.appbar_ ), 510 _kivymd.uix.datatables.datatables_ ), 159 `MDAdaptiveWidget` ( _class in kivymd.uix_ ), 713 `MDDialog` ( _class in kivymd.uix.dialog.dialog_ ), 590 `MDAnchorLayout` ( _class in kivymd.uix.anchorlayout_ ), `MDDialogButtonContainer` ( _class in_ 110 _kivymd.uix.dialog.dialog_ ), 592 `MDAnimationTransition` ( _class in kivymd.animation_ ), `MDDialogContentContainer` ( _class in_ 41 _kivymd.uix.dialog.dialog_ ), 592 `MDApp` ( _class in kivymd.app_ ), 26 `MDDialogHeadlineText` ( _class in_ `MDApp` ( _class in kivymd.tools.hotreload.app_ ), 699 _kivymd.uix.dialog.dialog_ ), 591 `MDBadge` ( _class in kivymd.uix.badge.badge_ ), 236 `MDDialogIcon` ( _class in kivymd.uix.dialog.dialog_ ), 591 `MDBaseDatePicker` ( _class in_ `MDDialogSupportingText` ( _class in kivymd.uix.pickers.datepicker.datepicker_ ), _kivymd.uix.dialog.dialog_ ), 591 337 `MDDivider` ( _class in kivymd.uix.divider.divider_ ), 518 `MDBaseTimePicker` ( _class in_ `MDDockedDatePicker` ( _class in kivymd.uix.pickers.timepicker.timepicker_ ), _kivymd.uix.pickers.datepicker.datepicker_ ), 320 340 `MDBottomAppBar` ( _class in kivymd.uix.appbar.appbar_ ), `MDDropDownItem` ( _class in_ 512 _kivymd.uix.dropdownitem.dropdownitem_ ), `MDBottomSheet` ( _class in_ 234 _kivymd.uix.bottomsheet.bottomsheet_ ), 443 `MDDropDownItemText` ( _class in_ `MDBottomSheetDragHandle` ( _class in kivymd.uix.dropdownitem.dropdownitem_ ), _kivymd.uix.bottomsheet.bottomsheet_ ), 442 234 `MDBottomSheetDragHandleButton` ( _class in_ `MDDropdownLeadingIconItem` ( _class in kivymd.uix.bottomsheet.bottomsheet_ ), 442 _kivymd.uix.menu.menu_ ), 399 `MDBottomSheetDragHandleTitle` ( _class in_ `MDDropdownLeadingIconTrailingTextItem` ( _class in kivymd.uix.bottomsheet.bottomsheet_ ), 442 _kivymd.uix.menu.menu_ ), 400 `MDBoxLayout` ( _class in kivymd.uix.boxlayout_ ), 112 `MDDropdownLeadingTrailingIconTextItem` ( _class in_ `MDButton` ( _class in kivymd.uix.button.button_ ), 304 _kivymd.uix.menu.menu_ ), 400 `MDButtonIcon` ( _class in kivymd.uix.button.button_ ), 305 `MDDropdownMenu` ( _class in kivymd.uix.menu.menu_ ), 400 `MDButtonText` ( _class in kivymd.uix.button.button_ ), 305 `MDDropdownTextItem` ( _class in kivymd.uix.menu.menu_ ), `MDCard` ( _class in kivymd.uix.card.card_ ), 574 399 `MDCardSwipe` ( _class in kivymd.uix.card.card_ ), 574 `MDDropdownTrailingIconItem` ( _class in_ `MDCardSwipeFrontBox` ( _class in kivymd.uix.card.card_ ), _kivymd.uix.menu.menu_ ), 399 577 `MDDropdownTrailingIconTextItem` ( _class in_ `MDCardSwipeLayerBox` ( _class in kivymd.uix.card.card_ ), _kivymd.uix.menu.menu_ ), 399 577 `MDDropdownTrailingTextItem` ( _class in_ `MDCarousel` ( _class in kivymd.uix.carousel.carousel_ ), 284 284 _kivymd.uix.menu.menu_ ), 400 `MDCarouselItem` ( _class in_ `MDExBaseProgressBar` ( _class in kivymd.uix.carousel.carousel_ ), 282 282 _kivymd.uix.exprogressindicator.exprogressindicator_ ), 

`MDCarousel` ( _class in kivymd.uix.carousel.carousel_ ), 284 284 `MDCarouselItem` ( _class in kivymd.uix.carousel.carousel_ ), 282 282 

**Index** 

**749** 

**KivyMD, Release 2.0.1.dev0** 

155 _kivymd.uix.list.list_ ), 413 `MDExCircularProgressIndicator` ( _class in_ `MDListItemTrailingSupportingText` ( _class in kivymd.uix.exprogressindicator.exprogressindicator_ ), _kivymd.uix.list.list_ ), 413 157 `MDLoadingIndicator` ( _class in_ `MDExLinearProgressIndicator` ( _class in kivymd.uix.loadingindicator.loadingindicator_ ), _kivymd.uix.exprogressindicator.exprogressindicator_ ), 144 157 `MDModalDatePicker` ( _class in_ `MDExpansionPanel` ( _class in kivymd.uix.pickers.datepicker.datepicker_ ), _kivymd.uix.expansionpanel.expansionpanel_ ), 340 553 `MDModalInputDatePicker` ( _class in_ `MDExpansionPanelContent` ( _class in kivymd.uix.pickers.datepicker.datepicker_ ), _kivymd.uix.expansionpanel.expansionpanel_ ), 341 552 `MDNavigationBar` ( _class in_ `MDExpansionPanelHeader` ( _class in kivymd.uix.navigationbar.navigationbar_ ), _kivymd.uix.expansionpanel.expansionpanel_ ), 278 552 `MDNavigationDrawer` ( _class in_ `MDExtendedFabButton` ( _class in kivymd.uix.navigationdrawer.navigationdrawer_ ), _kivymd.uix.button.button_ ), 306 537 `MDExtendedFabButtonIcon` ( _class in_ `MDNavigationDrawerDivider` ( _class in kivymd.uix.button.button_ ), 306 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDExtendedFabButtonText` ( _class in_ 534 _kivymd.uix.button.button_ ), 306 `MDNavigationDrawerHeader` ( _class in_ `MDFabBottomAppBarButton` ( _class in kivymd.uix.navigationdrawer.navigationdrawer_ ), _kivymd.uix.appbar.appbar_ ), 510 535 `MDFabButton` ( _class in kivymd.uix.button.button_ ), 306 `MDNavigationDrawerItem` ( _class in_ `MDFadeSlideTransition` ( _class in kivymd.uix.navigationdrawer.navigationdrawer_ ), _kivymd.uix.transition.transition_ ), 431 535 `MDFileManager` ( _class in_ `MDNavigationDrawerItemLeadingIcon` ( _class in kivymd.uix.filemanager.filemanager_ ), 256 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDFloatLayout` ( _class in kivymd.uix.floatlayout_ ), 71 536 `MDGridLayout` ( _class in kivymd.uix.gridlayout_ ), 119 `MDNavigationDrawerItemText` ( _class in_ `MDHeroFrom` ( _class in kivymd.uix.hero_ ), 107 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDHeroTo` ( _class in kivymd.uix.hero_ ), 108 536 `MDIcon` ( _class in kivymd.uix.label.label_ ), 465 `MDNavigationDrawerItemTrailingText` ( _class in_ `MDIconButton` ( _class in kivymd.uix.button.button_ ), 305 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDLabel` ( _class in kivymd.uix.label.label_ ), 463 536 `MDLinearProgressIndicator` ( _class in_ `MDNavigationDrawerLabel` ( _class in kivymd.uix.progressindicator.progressindicator_ ), _kivymd.uix.navigationdrawer.navigationdrawer_ ), 375 534 `MDList` ( _class in kivymd.uix.list.list_ ), 412 `MDNavigationDrawerMenu` ( _class in_ `MDListItem` ( _class in kivymd.uix.list.list_ ), 413 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDListItemHeadlineText` ( _class in_ 536 _kivymd.uix.list.list_ ), 413 `MDNavigationItem` ( _class in_ `MDListItemLeadingAvatar` ( _class in kivymd.uix.navigationbar.navigationbar_ ), _kivymd.uix.list.list_ ), 413 277 `MDListItemLeadingIcon` ( _class in kivymd.uix.list.list_ ), `MDNavigationItemIcon` ( _class in_ 413 _kivymd.uix.navigationbar.navigationbar_ ), `MDListItemSupportingText` ( _class in_ 277 _kivymd.uix.list.list_ ), 413 `MDNavigationItemLabel` ( _class in_ `MDListItemTertiaryText` ( _class in kivymd.uix.navigationbar.navigationbar_ ), _kivymd.uix.list.list_ ), 413 277 `MDListItemTrailingCheckbox` ( _class in_ `MDNavigationLayout` ( _class in kivymd.uix.list.list_ ), 413 _kivymd.uix.navigationdrawer.navigationdrawer_ ), `MDListItemTrailingIcon` ( _class in_ 534 

**Index** 

**750** 

**KivyMD, Release 2.0.1.dev0** 

`MDNavigationRail` ( _class_ 

_in_ 

_kivymd.uix.navigationrail.navigationrail_ ), 249 

`MDNavigationRailFabButton` ( _class in kivymd.uix.navigationrail.navigationrail_ ), 247 

`MDNavigationRailItem` ( _class in kivymd.uix.navigationrail.navigationrail_ ), 248 

`MDNavigationRailItemIcon` ( _class in_ 

_kivymd.uix.navigationrail.navigationrail_ ), 247 

`MDNavigationRailItemLabel` ( _class in_ 

_kivymd.uix.navigationrail.navigationrail_ ), 248 

`MDNavigationRailMenuButton` ( _class in kivymd.uix.navigationrail.navigationrail_ ), 247 

`MDRecycleBoxLayout` ( _class in kivymd.uix.recycleboxlayout_ ), 62 `MDRecycleGridLayout` ( _class in kivymd.uix.recyclegridlayout_ ), 117 

`MDRecycleView` ( _class in kivymd.uix.recycleview_ ), 76 

`MDRelativeLayout` ( _class in kivymd.uix.relativelayout_ ), 60 

`MDResponsiveLayout` ( _class in kivymd.uix.responsivelayout_ ), 83 

`MDScreen` ( _class in kivymd.uix.screen_ ), 79 `MDScreenManager` ( _class in kivymd.uix.screenmanager_ ), 55 

`MDScrollView` ( _class in kivymd.uix.scrollview_ ), 68 `MDScrollViewRefreshLayout` ( _class in_ 

_kivymd.uix.refreshlayout.refreshlayout_ ), 266 `MDSearchBar` ( _class in kivymd.uix.search.search_ ), 477 `MDSearchBarLeadingContainer` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchBarTrailingContainer` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchLeadingIcon` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchTrailingAvatar` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchTrailingIcon` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchViewContainer` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchViewLeadingContainer` ( _class in kivymd.uix.search.search_ ), 476 `MDSearchViewTrailingContainer` ( _class in kivymd.uix.search.search_ ), 476 `MDSegmentButtonIcon` ( _class in_ 

_kivymd.uix.segmentedbutton.segmentedbutton_ ), 430 

`MDSegmentButtonLabel` ( _class in_ 

_kivymd.uix.segmentedbutton.segmentedbutton_ ), 430 

`MDSegmentedButton` ( _class in kivymd.uix.segmentedbutton.segmentedbutton_ ), 428 

`MDSegmentedButtonItem` ( _class in kivymd.uix.segmentedbutton.segmentedbutton_ ), 427 

`MDSharedAxisTransition` ( _class in kivymd.uix.transition.transition_ ), 431 

`MDSlider` ( _class in kivymd.uix.slider.slider_ ), 542 

`MDSliderHandle` ( _class in kivymd.uix.slider.slider_ ), 545 `MDSliderValueLabel` ( _class in kivymd.uix.slider.slider_ ), 545 

`MDSlideTransition` ( _class in kivymd.uix.transition.transition_ ), 431 `MDSliverAppbar` ( _class in kivymd.uix.sliverappbar.sliverappbar_ ), 493 `MDSliverAppbarContent` ( _class in kivymd.uix.sliverappbar.sliverappbar_ ), 493 `MDSliverAppbarHeader` ( _class in kivymd.uix.sliverappbar.sliverappbar_ ), 493 

`MDSmartTile` ( _class in kivymd.uix.imagelist.imagelist_ ), 598 

`MDSmartTileImage` ( _class in kivymd.uix.imagelist.imagelist_ ), 597 `MDSmartTileOverlayContainer` ( _class in kivymd.uix.imagelist.imagelist_ ), 597 

`MDSnackbar` ( _class in kivymd.uix.snackbar.snackbar_ ), 486 `MDSnackbarActionButton` ( _class in kivymd.uix.snackbar.snackbar_ ), 486 `MDSnackbarActionButtonText` ( _class in kivymd.uix.snackbar.snackbar_ ), 486 `MDSnackbarButtonContainer` ( _class in kivymd.uix.snackbar.snackbar_ ), 485 `MDSnackbarCloseButton` ( _class in kivymd.uix.snackbar.snackbar_ ), 485 `MDSnackbarSupportingText` ( _class in kivymd.uix.snackbar.snackbar_ ), 487 `MDSnackbarText` ( _class in kivymd.uix.snackbar.snackbar_ ), 487 `MDStackLayout` ( _class in kivymd.uix.stacklayout_ ), 57 `MDSwapTransition` ( _class in_ 

_kivymd.uix.transition.transition_ ), 431 

`MDSwiper` ( _class in kivymd.uix.swiper.swiper_ ), 201 `MDSwiperItem` ( _class in kivymd.uix.swiper.swiper_ ), 201 `MDSwitch` ( _class in kivymd.uix.selectioncontrol.selectioncontrol_ ), 611 

`MDTabsBadge` ( _class in kivymd.uix.tab.tab_ ), 137 `MDTabsCarousel` ( _class in kivymd.uix.tab.tab_ ), 137 `MDTabsItem` ( _class in kivymd.uix.tab.tab_ ), 138 `MDTabsItemIcon` ( _class in kivymd.uix.tab.tab_ ), 137 `MDTabsItemSecondary` ( _class in kivymd.uix.tab.tab_ ), 

**Index** 

**751** 

**KivyMD, Release 2.0.1.dev0** 

`min_year` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 338 338 `minimum_absorbed_velocity` 

141 

`MDTabsItemText` ( _class in kivymd.uix.tab.tab_ ), 137 _attribute_ ), 338 338 `MDTabsPrimary` ( _class in kivymd.uix.tab.tab_ ), 138 `minimum_absorbed_velocity MDTabsSecondary` ( _class in kivymd.uix.tab.tab_ ), 142 ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `MDTextField` ( _class in kivymd.uix.textfield.textfield_ ), 219 _attribute_ ), 67 `MDTextFieldHelperText` ( _class in_ `minute` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker kivymd.uix.textfield.textfield_ ), 213 _attribute_ ), 320 `MDTextFieldHintText` ( _class in_ `mobile_view` ( _kivymd.uix.responsivelayout.MDResponsiveLayout kivymd.uix.textfield.textfield_ ), 215 _attribute_ ), 83 `MDTextFieldLeadingIcon` ( _class in_ `mode` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker kivymd.uix.textfield.textfield_ ), 218 _attribute_ ), 338 `MDTextFieldMaxLengthText` ( _class in_ `mode` ( _kivymd.uix.textfield.textfield.MDTextField atkivymd.uix.textfield.textfield_ ), 215 _tribute_ ), 220 `MDTextFieldTrailingIcon` ( _class in_ `mode` ( _kivymd.uix.textfield.textfield.MDTextFieldHelperText kivymd.uix.textfield.textfield_ ), 219 _attribute_ ), 213 `MDTimePickerDialHorizontal` ( _class in_ `module` _kivymd.uix.pickers.timepicker.timepicker_ ), `kivymd` , 693 322 `kivymd.animation` , 37 `MDTimePickerDialVertical` ( _class in_ `kivymd.app` , 24 _kivymd.uix.pickers.timepicker.timepicker_ ), `kivymd.dynamic_color` , 42 322 `kivymd.effects` , 695 `MDTimePickerInput` ( _class in_ `kivymd.effects.stiffscroll` , 695 _kivymd.uix.pickers.timepicker.timepicker_ ), `kivymd.effects.stiffscroll.stiffscroll` , 322 674 `MDToggleButtonBehavior` ( _class in_ `kivymd.factory_registers` , 694 _kivymd.uix.behaviors.toggle_behavior_ ), 624 `kivymd.font_definitions` , 32 `MDTooltip` ( _class in kivymd.uix.tooltip.tooltip_ ), 196 `kivymd.icon_definitions` , 27 `MDTooltipPlain` ( _class in kivymd.uix.tooltip.tooltip_ ), `kivymd.material_resources` , 694 197 `kivymd.theming` , 7 `MDTooltipRich` ( _class in kivymd.uix.tooltip.tooltip_ ), 198 `kivymd.toast` , 695 `MDTooltipRichActionButton` ( _class in_ `kivymd.toast.androidtoast` , 695 _kivymd.uix.tooltip.tooltip_ ), 198 `kivymd.tools` , 696 `MDTooltipRichSubhead` ( _class in_ `kivymd.tools.argument_parser` , 696 _kivymd.uix.tooltip.tooltip_ ), 198 `kivymd.tools.hotreload` , 697 `MDTooltipRichSupportingText` ( _class in_ `kivymd.tools.hotreload.app` , 697 _kivymd.uix.tooltip.tooltip_ ), 197 `kivymd.tools.packaging` , 701 `MDTopAppBar` ( _class in kivymd.uix.appbar.appbar_ ), 511 `kivymd.tools.packaging.pyinstaller` , 701 `MDTopAppBarLeadingButtonContainer` ( _class in_ `kivymd.tools.packaging.pyinstaller.hook-kivymd` , _kivymd.uix.appbar.appbar_ ), 510 703 `MDTopAppBarTitle` ( _class in_ `kivymd.tools.patterns` , 703 _kivymd.uix.appbar.appbar_ ), 510 `kivymd.tools.patterns.add_view` , 703 `MDTopAppBarTrailingButtonContainer` ( _class in_ `kivymd.tools.patterns.create_project` , 704 _kivymd.uix.appbar.appbar_ ), 511 `kivymd.tools.patterns.MVC` , 709 `MDTransitionBase` ( _class in_ `kivymd.tools.patterns.MVC.libs` , 710 _kivymd.uix.transition.transition_ ), 430 `kivymd.tools.patterns.MVC.libs.translation` , `MDWidget` ( _class in kivymd.uix.widget_ ), 114 710 `menu_button` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ `kivymd.tools.patterns.MVC.Model` , 709 _attribute_ ), 249 `kivymd.tools.patterns.MVC.Model.database_firebase` , `min` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ 709 _attribute_ ), 674 `kivymd.tools.patterns.MVC.Model.database_restdb` , `min_date` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ 710 _attribute_ ), 338 `kivymd.tools.release` , 711 711 

`kivymd.tools.patterns.MVC.Model.database_restdb` , 710 `kivymd.tools.release` , 711 711 `kivymd.tools.release.git_commands` , 711 `kivymd.tools.release.make_release` , 711 

`min_height` ( _kivymd.uix.menu.menu.MDDropdownMenu attribute_ ), 401 

**Index** 

**752** 

**KivyMD, Release 2.0.1.dev0** 

`kivymd.tools.release.update_icons` , 712 `kivymd.uix` , 713 `kivymd.uix.anchorlayout` , 108 `kivymd.uix.appbar` , 714 `kivymd.uix.appbar.appbar` , 496 `kivymd.uix.badge` , 714 `kivymd.uix.badge.badge` , 235 `kivymd.uix.behaviors` , 714 `kivymd.uix.behaviors.backgroundcolor_behavior` , 670 

`kivymd.uix.behaviors.declarative_behavior` , 655 

`kivymd.uix.behaviors.elevation` , 625 `kivymd.uix.behaviors.focus_behavior` , 619 `kivymd.uix.behaviors.hover_behavior` , 652 `kivymd.uix.behaviors.magic_behavior` , 646 `kivymd.uix.behaviors.motion_behavior` , 667 `kivymd.uix.behaviors.ripple_behavior` , 641 `kivymd.uix.behaviors.rotate_behavior` , 639 `kivymd.uix.behaviors.scale_behavior` , 616 `kivymd.uix.behaviors.state_layer_behavior` , 664 

`kivymd.uix.behaviors.stencil_behavior` , 672 

`kivymd.uix.behaviors.toggle_behavior` , 622 `kivymd.uix.behaviors.touch_behavior` , 663 `kivymd.uix.bottomsheet` , 714 `kivymd.uix.bottomsheet.bottomsheet` , 432 `kivymd.uix.boxlayout` , 110 `kivymd.uix.button` , 714 `kivymd.uix.button.button` , 288 `kivymd.uix.card` , 714 `kivymd.uix.card.card` , 562 `kivymd.uix.carousel` , 715 `kivymd.uix.carousel.carousel` , 279 `kivymd.uix.chip` , 715 `kivymd.uix.chip.chip` , 341 `kivymd.uix.circularlayout` , 71 `kivymd.uix.controllers` , 715 `kivymd.uix.controllers.windowcontroller` , 615 

`kivymd.uix.datatables` , 715 `kivymd.uix.datatables.datatables` , 158 `kivymd.uix.dialog` , 715 `kivymd.uix.dialog.dialog` , 577 `kivymd.uix.divider` , 715 `kivymd.uix.divider.divider` , 514 `kivymd.uix.dropdownitem` , 715 `kivymd.uix.dropdownitem.dropdownitem` , 231 `kivymd.uix.expansionpanel` , 716 `kivymd.uix.expansionpanel.expansionpanel` , 546 `kivymd.uix.exprogressindicator` , 716 

`kivymd.uix.exprogressindicator.animators` , 716 `kivymd.uix.exprogressindicator.exprogressindicator` , 145 `kivymd.uix.filemanager` , 721 `kivymd.uix.filemanager.filemanager` , 250 `kivymd.uix.fitimage` , 721 `kivymd.uix.fitimage.fitimage` , 554 `kivymd.uix.floatlayout` , 69 `kivymd.uix.gridlayout` , 117 `kivymd.uix.hero` , 84 `kivymd.uix.imagelist` , 721 `kivymd.uix.imagelist.imagelist` , 592 `kivymd.uix.label` , 721 `kivymd.uix.label.label` , 444 `kivymd.uix.list` , 721 `kivymd.uix.list.list` , 405 `kivymd.uix.loadingindicator` , 721 `kivymd.uix.loadingindicator.loadingindicator` , 142 `kivymd.uix.menu` , 721 `kivymd.uix.menu.menu` , 378 `kivymd.uix.navigationbar` , 721 `kivymd.uix.navigationbar.navigationbar` , 267 `kivymd.uix.navigationdrawer` , 722 `kivymd.uix.navigationdrawer.navigationdrawer` , 519 `kivymd.uix.navigationrail` , 722 `kivymd.uix.navigationrail.navigationrail` , 237 `kivymd.uix.pickers` , 722 `kivymd.uix.pickers.datepicker` , 722 `kivymd.uix.pickers.datepicker.datepicker` , 323 `kivymd.uix.pickers.timepicker` , 722 `kivymd.uix.pickers.timepicker.timepicker` , 308 `kivymd.uix.progressindicator` , 722 `kivymd.uix.progressindicator.progressindicator` , 369 `kivymd.uix.recycleboxlayout` , 60 `kivymd.uix.recyclegridlayout` , 115 `kivymd.uix.recycleview` , 74 `kivymd.uix.refreshlayout` , 722 `kivymd.uix.refreshlayout.refreshlayout` , 262 `kivymd.uix.relativelayout` , 58 `kivymd.uix.responsivelayout` , 79 `kivymd.uix.screen` , 77 `kivymd.uix.screenmanager` , 53 `kivymd.uix.scrollview` , 62 `kivymd.uix.search` , 722 `kivymd.uix.search.search` , 466 

**Index** 

**753** 

**KivyMD, Release 2.0.1.dev0** 

N 

`kivymd.uix.segmentedbutton` , 723 `kivymd.uix.segmentedbutton.segmentedbuttonname` , ( _kivymd.tools.patterns.MVC.Model.database_firebase.DataBase_ 414 _attribute_ ), 709 `kivymd.uix.selectioncontrol` , 723 `name` ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBase_ `kivymd.uix.selectioncontrol.selectioncontrol` , _attribute_ ), 710 600 `neutralPaletteKeyColorColor kivymd.uix.slider` , 723 ( _kivymd.dynamic_color.DynamicColor at-_ `kivymd.uix.slider.slider` , 541 _tribute_ ), 52 `kivymd.uix.sliverappbar` , 723 `neutralVariantPaletteKeyColorColor kivymd.uix.sliverappbar.sliverappbar` , 487 ( _kivymd.dynamic_color.DynamicColor at-_ `kivymd.uix.snackbar` , 723 _tribute_ ), 52 `kivymd.uix.snackbar.snackbar` , 479 `next_frame()` ( _in module kivymd.utils_ ), 724 `kivymd.uix.stacklayout` , 55 `NOISE_ANIMATION_DURATION kivymd.uix.swiper` , 723 ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `kivymd.uix.swiper.swiper` , 198 _attribute_ ), 645 `kivymd.uix.tab` , 723 `kivymd.uix.tab.tab` , 119 O `kivymd.uix.textfield` , 724 `observers` ( _kivymd.tools.patterns.MVC.libs.translation.Translation_ `kivymd.uix.textfield.textfield` , 204 _attribute_ ), 710 `kivymd.uix.tooltip` , 724 `on__active()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemLabel_ `kivymd.uix.tooltip.tooltip` , 190 _method_ ), 248 `kivymd.uix.transition` , 724 `on__appbar()` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `kivymd.uix.transition.transition` , 430 _method_ ), 496 `kivymd.uix.widget` , 112 `on__drop_down_text() kivymd.utils` , 724 ( _kivymd.uix.dropdownitem.dropdownitem.MDDropDownItem_ `kivymd.utils.cubic_bezier` , 724 _method_ ), 234 `kivymd.utils.fpsmonitor` , 726 `on__opacity()` ( `kivymd.utils.set_bars_colors` , 727 _method_ ), 668 `monotonic` ( _in module kivymd.tools.hotreload.app_ ), 699 `on__rotation_angle() month` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator attribute_ ), 338 _method_ ), 377 `MotionBase` ( _class in kivymd.uix.behaviors.motion_behavior_ ), `on__scale_x()` ( 668 _method_ ), 668 `MotionDatePickerBehavior` ( _class in_ `on__scale_y()` ( _kivymd.uix.behaviors.motion_behavior_ ), _method_ ), 668 670 `on__x()` ( _kivymd.uix.button.button.MDExtendedFabButton_ `MotionDialogBehavior` ( _class in method_ ), 307 _kivymd.uix.behaviors.motion_behavior_ ), `on_action_items()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ 669 _method_ ), 513 `MotionDropDownMenuBehavior` ( _class in_ `on_active()` ( _kivymd.uix.chip.chip.MDChip method_ ), _kivymd.uix.behaviors.motion_behavior_ ), 368 668 `on_active()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem_ `MotionExtendedFabButtonBehavior` ( _class in method_ ), 278 _kivymd.uix.behaviors.motion_behavior_ ), 668 `on_active()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItem_ `MotionShackBehavior` ( _class in method_ ), 248 _kivymd.uix.behaviors.motion_behavior_ ), `on_active()` ( 670 _method_ ), 378 `MotionTimePickerBehavior` ( _class in_ `on_active()` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItem kivymd.uix.behaviors.motion_behavior_ ), _method_ ), 428 670 `on_active()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `move_changelog()` ( _in module method_ ), 610 _kivymd.tools.release.make_release_ ), 712 `on_active()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `multiselect` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton method_ ), 615 _attribute_ ), 428 

**Index** 

**754** 

**KivyMD, Release 2.0.1.dev0** 

`on_adaptive_height()` 464 ( _kivymd.uix.MDAdaptiveWidget method_ ), `on_current_hero()` ( _kivymd.uix.screenmanager.MDScreenManager_ 713 _method_ ), 55 `on_adaptive_size()` ( _kivymd.uix.MDAdaptiveWidget_ `on_date_interval()` ( _kivymd.uix.textfield.textfield.Validator method_ ), 714 _method_ ), 211 `on_adaptive_width()` ( _kivymd.uix.MDAdaptiveWidget_ `on_detect_visible()` _method_ ), 714 ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior_ `on_allow_selection()` _method_ ), 655 ( _kivymd.uix.label.label.MDLabel method_ ), `on_determinate()` ( 465 _method_ ), 157 `on_am_pm()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `on_determinate_complete()` _method_ ), 322 ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator_ `on_anchor()` ( _kivymd.uix.card.card.MDCardSwipe method_ ), 378 _method_ ), 576 `on_disabled()` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `on_background_color()` _method_ ), 667 ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `on_disabled()` ( _kivymd.uix.button.button.MDButton method_ ), 495 _method_ ), 305 `on_background_color_toolbar() on_disabled()` ( _kivymd.uix.dropdownitem.dropdownitem.MDDropDownItem_ ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 234 _method_ ), 261 `on_disabled()` ( `on_cancel()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickermethod_ ), 428 _method_ ), 340 `on_disabled()` ( _kivymd.uix.textfield.textfield.MDTextField_ `on_cancel()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePickermethod_ ), 231 _method_ ), 322 `on_dismiss()` ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior_ `on_cancel_selection()` _method_ ), 669 ( _kivymd.uix.label.label.MDLabel method_ ), `on_dismiss()` ( 465 _method_ ), 668 `on_carousel_index() on_dismiss()` ( _kivymd.uix.behaviors.motion_behavior.MotionShackBehavior_ ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), _method_ ), 670 141 `on_dismiss()` ( _kivymd.uix.dialog.dialog.MDDialog_ `on_change_screen_type()` _method_ ), 591 ( _kivymd.uix.responsivelayout.MDResponsiveLayout_ `on_dismiss()` ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 83 _method_ ), 262 `on_check_press()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `on_dismiss()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 189 _method_ ), 340 `on_close()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ `on_dismiss()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker method_ ), 553 _method_ ), 322 `on_close()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `on_dismiss()` ( _kivymd.uix.snackbar.snackbar.MDSnackbar method_ ), 540 _method_ ), 487 `on_close()` ( _kivymd.uix.search.search.MDSearchBar_ `on_dismiss()` ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), 479 _method_ ), 197 `on_collapse()` ( _kivymd.uix.button.button.MDExtendedFabButton_ `on_docked()` ( _kivymd.uix.search.search.MDSearchBar method_ ), 307 _method_ ), 478 `on_color_array()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExCircularProgressIndicator_ `on_double_tap()` ( _kivymd.uix.behaviors.touch_behavior.TouchBehavior method_ ), 158 _method_ ), 664 `on_color_array()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicator_ `on_double_tap()` ( _kivymd.uix.label.label.MDLabel method_ ), 157 _method_ ), 464 `on_colors` ( _kivymd.theming.ThemeManager attribute_ ), `on_drawer_type()` ( 19 _method_ ), 540 `on_complete()` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ `on_dynamic_scheme_contrast()` _method_ ), 432 ( _kivymd.theming.ThemeManager method_ ), `on_complete()` ( _kivymd.uix.transition.transition.MDTransitionBase_ 21 _method_ ), 431 `on_dynamic_scheme_name() on_copy()` ( _kivymd.uix.label.label.MDLabel method_ ), ( _kivymd.theming.ThemeManager method_ ), 

**Index** 

**755** 

**KivyMD, Release 2.0.1.dev0** 

21 `on_index()` ( _kivymd.uix.carousel.carousel.MDCarousel_ `on_edit()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickm_ **_e_** _thodr_ ), 287 _method_ ), 340 `on_items()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `on_edit()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePickermethod_ ), 404 _method_ ), 322 `on_leave()` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior_ `on_enter()` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior method_ ), 655 _method_ ), 655 `on_leave()` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `on_enter()` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviormethod_ ), 667 _method_ ), 667 `on_leave()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItem_ `on_enter()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemmethod_ ), 248 _method_ ), 248 `on_leave()` ( _kivymd.uix.slider.slider.MDSliderHandle_ `on_enter()` ( _kivymd.uix.slider.slider.MDSliderHandle method_ ), 545 _method_ ), 545 `on_leave()` ( _kivymd.uix.tooltip.tooltip.MDTooltip_ `on_enter()` ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), 197 _method_ ), 197 `on_leave()` ( _kivymd.uix.tooltip.tooltip.MDTooltipRich_ `on_enter()` ( _kivymd.uix.tooltip.tooltip.MDTooltipRichActionButton method_ ), 198 _method_ ), 198 `on_leave()` ( _kivymd.uix.tooltip.tooltip.MDTooltipRichActionButton_ `on_error()` ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 198 _method_ ), 231 `on_line_color()` ( _kivymd.uix.button.button.MDIconButton_ `on_expand()` ( _kivymd.uix.button.button.MDExtendedFabButton method_ ), 306 _method_ ), 307 `on_line_color()` ( _kivymd.uix.chip.chip.MDChip_ `on_fab_state()` ( _kivymd.uix.button.button.MDExtendedFabButton method_ ), 368 _method_ ), 307 `on_line_color()` ( `on_focus()` ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 428 _method_ ), 231 `on_line_color()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `on_follow_system_theme()` _method_ ), 614 ( _kivymd.theming.ThemeManager method_ ), `on_long_touch()` ( _kivymd.uix.behaviors.touch_behavior.TouchBehavior_ 21 _method_ ), 664 `on_handle_enter()` ( _kivymd.uix.slider.slider.MDSlider_ `on_long_touch()` ( _kivymd.uix.chip.chip.MDChip method_ ), 545 _method_ ), 368 `on_handle_leave()` ( _kivymd.uix.slider.slider.MDSlider_ `on_long_touch()` ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), 545 _method_ ), 197 `on_header_cls()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `on_md_bg_color()` ( _method_ ), 404 _method_ ), 671 `on_height()` ( _kivymd.uix.textfield.textfield.MDTextField_ `on_md_bg_color()` ( _kivymd.uix.label.label.MDLabel method_ ), 231 _method_ ), 465 `on_hero_to()` ( _kivymd.uix.screen.MDScreen method_ ), `on_minute_select()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ 79 _method_ ), 322 `on_hide_appbar()` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `on_mouse_update()` ( _kivymd.uix.behaviors.hover_behavior.HoverBehavior method_ ), 495 _method_ ), 655 `on_hide_bar()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `on_ok()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 513 _method_ ), 340 `on_hour_select()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `on_ok()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker method_ ), 322 _method_ ), 322 `on_icon()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `on_open()` ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior method_ ), 261 _method_ ), 670 `on_icon_color_normal() on_open()` ( _kivymd.uix.behaviors.motion_behavior.MotionDropDownMenuBehavior_ ( _kivymd.uix.textfield.textfield.BaseTextFieldIcon method_ ), 668 _method_ ), 218 `on_open()` ( _kivymd.uix.behaviors.motion_behavior.MotionShackBehavior_ `on_idle()` ( _kivymd.tools.hotreload.app.MDApp method_ ), 670 _method_ ), 701 `on_open()` ( _kivymd.uix.dialog.dialog.MDDialog_ `on_indeterminate_animator()` _method_ ), 591 ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicat_ `on_open()` ( _kivymd.uix.expansi_ **_o_** _npanel.expansionpanel.MDExpansionPanelr method_ ), 157 _method_ ), 553 

**Index** 

**756** 

**KivyMD, Release 2.0.1.dev0** 

`on_open()` ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 304 _method_ ), 262 `on_release()` ( _kivymd.uix.button.button.MDFabButton_ `on_open()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawermethod_ ), 306 _method_ ), 540 `on_release()` ( _kivymd.uix.card.card.MDCard method_ ), `on_open()` ( _kivymd.uix.search.search.MDSearchBar_ 574 _method_ ), 479 `on_release()` ( _kivymd.uix.chip.chip.MDChip method_ ), `on_open()` ( _kivymd.uix.snackbar.snackbar.MDSnackbar_ 369 _method_ ), 487 `on_release()` ( _kivymd.uix.imagelist.imagelist.MDSmartTile_ `on_open()` ( _kivymd.uix.tooltip.tooltip.MDTooltip method_ ), 599 _method_ ), 197 `on_release()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItem_ `on_open_progress()` ( _kivymd.uix.card.card.MDCardSwipe method_ ), 278 _method_ ), 576 `on_release()` ( `on_orientation()` ( _kivymd.uix.divider.divider.MDDivider method_ ), 535 _method_ ), 519 `on_ripple_behavior() on_orientation()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicator_ ( _kivymd.uix.card.card.MDCard method_ ), _method_ ), 157 574 `on_overswipe_left() on_ripple_effect()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), _method_ ), 614 203 `on_row_press()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `on_overswipe_right()` _method_ ), 189 ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), `on_scroll_cls()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ 203 _method_ ), 513 `on_palette()` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator_ `on_scroll_content()` _method_ ), 377 ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar_ `on_path_to_wallpaper()` _method_ ), 495 ( _kivymd.theming.ThemeManager method_ ), `on_scroll_start()` ( _kivymd.uix.swiper.swiper.MDSwiper_ 21 _method_ ), 203 `on_pre_dismiss()` ( _kivymd.uix.dialog.dialog.MDDialog_ `on_select_day()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 591 _method_ ), 340 `on_pre_dismiss()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `on_select_month()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 262 _method_ ), 340 `on_pre_open()` ( _kivymd.uix.dialog.dialog.MDDialog_ `on_select_year()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker method_ ), 591 _method_ ), 340 `on_pre_open()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `on_selected()` ( _method_ ), 262 _method_ ), 536 `on_pre_swipe()` ( _kivymd.uix.swiper.swiper.MDSwiper_ `on_selection()` ( _kivymd.uix.label.label.MDLabel method_ ), 203 _method_ ), 465 `on_press()` ( _kivymd.uix.button.button.BaseButton_ `on_selector_hour()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker method_ ), 304 _method_ ), 322 `on_press()` ( _kivymd.uix.button.button.MDFabButton_ `on_selector_minute()` _method_ ), 306 ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `on_press()` ( _kivymd.uix.card.card.MDCard method_ ), _method_ ), 322 574 `on_sheet_type()` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet_ `on_press()` ( _kivymd.uix.chip.chip.MDChip method_ ), _method_ ), 443 369 `on_show_bar()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `on_press()` ( _kivymd.uix.imagelist.imagelist.MDSmartTile method_ ), 513 _method_ ), 599 `on_size()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `on_progress()` ( _kivymd.uix.transition.transition.MDFadeSlideTransitionmethod_ ), 513 _method_ ), 431 `on_size()` ( _kivymd.uix.controllers.windowcontroller.WindowController_ `on_progress()` ( _kivymd.uix.transition.transition.MDSharedAxisTransitionmethod_ ), 616 _method_ ), 432 `on_size()` ( _kivymd.uix.label.label.MDLabel method_ ), `on_radius()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ 465 _method_ ), 540 `on_size()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ `on_release()` ( _kivymd.uix.button.button.BaseButton method_ ), 249 

**Index** 

**757** 

**KivyMD, Release 2.0.1.dev0** 

`on_size()` ( _kivymd.uix.responsivelayout.MDResponsiveLayout method_ ), 287 _method_ ), 84 `on_touch_down()` ( _kivymd.uix.dialog.dialog.MDDialog_ `on_size()` ( _kivymd.uix.slider.slider.MDSlider method_ ), _method_ ), 591 544 `on_touch_down()` ( _kivymd.uix.imagelist.imagelist.MDSmartTileImage_ `on_size()` ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), 597 _method_ ), 141 `on_touch_down()` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `on_slide_down()` ( _kivymd.uix.carousel.carousel.MDCarousel method_ ), 404 _method_ ), 287 `on_touch_down()` ( `on_slide_left()` ( _kivymd.uix.carousel.carousel.MDCarousel method_ ), 540 _method_ ), 287 `on_touch_down()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `on_slide_progress()` _method_ ), 339 ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), `on_touch_down()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ 141 _method_ ), 321 `on_slide_right()` ( _kivymd.uix.carousel.carousel.MDCarousel_ `on_touch_down()` ( _kivymd.uix.scrollview.StretchOverScrollBehavior method_ ), 287 _method_ ), 68 `on_slide_up()` ( _kivymd.uix.carousel.carousel.MDCarousel_ `on_touch_down()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox method_ ), 287 _method_ ), 611 `on_source()` ( _kivymd.uix.fitimage.fitimage.FitImage_ `on_touch_down()` ( _kivymd.uix.slider.slider.MDSlider method_ ), 561 _method_ ), 544 `on_state()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `on_touch_down()` ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), 610 _method_ ), 203 `on_supporting_text() on_touch_move()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ ( _kivymd.uix.search.search.MDSearchBar method_ ), 644 _method_ ), 478 `on_touch_move()` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet_ `on_swipe()` ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), 444 _method_ ), 203 `on_touch_move()` ( _kivymd.uix.card.card.MDCardSwipe_ `on_swipe_complete()` _method_ ), 576 ( _kivymd.uix.card.card.MDCardSwipe method_ ), `on_touch_move()` ( _kivymd.uix.carousel.carousel.MDCarousel_ 575 _method_ ), 287 `on_swipe_left()` ( _kivymd.uix.swiper.swiper.MDSwiper_ `on_touch_move()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 203 _method_ ), 404 `on_swipe_right()` ( _kivymd.uix.swiper.swiper.MDSwiper_ `on_touch_move()` ( _method_ ), 203 _method_ ), 540 `on_switch_tabs()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationBar_ `on_touch_move()` ( _kivymd.uix.scrollview.StretchOverScrollBehavior method_ ), 279 _method_ ), 68 `on_tab_switch()` ( _kivymd.uix.tab.tab.MDTabsPrimary_ `on_touch_move()` ( _kivymd.uix.slider.slider.MDSlider method_ ), 141 _method_ ), 545 `on_text()` ( _kivymd.uix.search.search.MDSearchBar_ `on_touch_move()` ( _kivymd.uix.tab.tab.MDTabsCarousel method_ ), 479 _method_ ), 137 `on_text_color()` ( _kivymd.uix.label.label.MDLabel_ `on_touch_up()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior method_ ), 465 _method_ ), 651 `on_thumb_down()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `on_touch_up()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple method_ ), 615 _method_ ), 645 `on_time_input()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `on_touch_up()` ( _kivymd.uix.card.card.MDCardSwipe method_ ), 322 _method_ ), 576 `on_touch_down()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `on_touch_up()` ( _kivymd.uix.carousel.carousel.MDCarousel method_ ), 644 _method_ ), 287 `on_touch_down()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `on_touch_up()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 646 _method_ ), 405 `on_touch_down()` ( _kivymd.uix.button.button.BaseButton_ `on_touch_up()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer method_ ), 304 _method_ ), 540 `on_touch_down()` ( _kivymd.uix.card.card.MDCardSwipe_ `on_touch_up()` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout method_ ), 576 _method_ ), 267 `on_touch_down()` ( _kivymd.uix.carousel.carousel.MDCarousel_ `on_touch_up()` ( _kivymd.uix.scrollview.StretchOverScrollBehavior_ 

**Index** 

**758** 

**KivyMD, Release 2.0.1.dev0** 

_method_ ), 68 ( _kivymd.dynamic_color.DynamicColor at-_ `on_touch_up()` ( _kivymd.uix.slider.slider.MDSlider tribute_ ), 49 _method_ ), 545 `onSecondaryFixedVariantColor on_touch_up()` ( _kivymd.uix.swiper.swiper.MDSwiper_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 204 _tribute_ ), 49 `on_transform_in()` ( _kivymd.uix.hero.MDHeroFrom_ `onSurfaceColor` ( _kivymd.dynamic_color.DynamicColor method_ ), 108 _attribute_ ), 50 `on_transform_out()` ( _kivymd.uix.hero.MDHeroFrom_ `onSurfaceLightColor` _method_ ), 108 ( _kivymd.dynamic_color.DynamicColor at-_ `on_triple_tap()` ( _kivymd.uix.behaviors.touch_behavior.TouchBehaviortribute_ ), 50 _method_ ), 664 `onSurfaceVariantColor on_type()` ( _kivymd.uix.chip.chip.MDChip method_ ), 368 ( _kivymd.dynamic_color.DynamicColor at-_ `on_value()` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect tribute_ ), 50 _method_ ), 675 `onTertiaryColor` ( _kivymd.dynamic_color.DynamicColor_ `on_value()` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicatorattribute_ ), 49 _method_ ), 377 `onTertiaryContainerColor on_value()` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 68 _tribute_ ), 49 `on_value_pos()` ( _kivymd.uix.slider.slider.MDSlider_ `onTertiaryFixedColor` _method_ ), 545 ( _kivymd.dynamic_color.DynamicColor at-_ `on_vbar()` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar tribute_ ), 49 _method_ ), 495 `onTertiaryFixedVariantColor on_view_root()` ( _kivymd.uix.search.search.MDSearchBar_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 478 _tribute_ ), 49 `on_wakeup()` ( _kivymd.tools.hotreload.app.MDApp_ `open()` ( _kivymd.uix.dialog.dialog.MDDialog method_ ), _method_ ), 701 591 `on_widgets()` ( _kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior_ `open()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel method_ ), 663 _method_ ), 553 `on_window_touch()` ( _kivymd.uix.label.label.MDLabel_ `open()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 464 _method_ ), 404 `onBackgroundColor` ( _kivymd.dynamic_color.DynamicColor_ `open()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 51 _method_ ), 339 `onErrorColor` ( _kivymd.dynamic_color.DynamicColor_ `open()` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalDatePicker attribute_ ), 51 _method_ ), 340 `onErrorContainerColor open()` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 341 _tribute_ ), 51 `open()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ `onPrimaryColor` ( _kivymd.dynamic_color.DynamicColor method_ ), 321 _attribute_ ), 47 `open()` ( _kivymd.uix.snackbar.snackbar.MDSnackbar_ `onPrimaryContainerColor` _method_ ), 486 ( _kivymd.dynamic_color.DynamicColor at-_ `open_card()` ( _kivymd.uix.card.card.MDCardSwipe tribute_ ), 48 _method_ ), 576 `onPrimaryFixedColor open_close_menu_month_year_selection()` ( _kivymd.dynamic_color.DynamicColor at-_ ( _kivymd.uix.pickers.datepicker.datepicker.MDDockedDatePicker tribute_ ), 48 _method_ ), 340 `onPrimaryFixedVariantColor open_menu_year_selection()` ( _kivymd.dynamic_color.DynamicColor at-_ ( _kivymd.uix.pickers.datepicker.datepicker.MDModalDatePicker tribute_ ), 48 _method_ ), 340 `onSecondaryColor` ( _kivymd.dynamic_color.DynamicColor_ `open_progress` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), 48 _attribute_ ), 574 `onSecondaryContainerColor open_progress` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 538 _tribute_ ), 48 `open_view()` ( _kivymd.uix.search.search.MDSearchBar_ `onSecondaryFixedColor` _method_ ), 479 

**Index** 

**759** 

**KivyMD, Release 2.0.1.dev0** 

`opening_icon_duration parse_args()` ( _kivymd.tools.argument_parser.ArgumentParserWithHelp_ ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonmethod_ ), 697 _attribute_ ), 428 `patch_builder()` ( _kivymd.tools.hotreload.app.MDApp_ `opening_icon_transition` _method_ ), 701 ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedB_ `path` ( _in mod_ **_u_** _ttonle kivymd_ ), 694 _attribute_ ), 428 `path_to_wallpaper` ( _kivymd.theming.ThemeManager_ `opening_time` ( _kivymd.uix.card.card.MDCardSwipe atattribute_ ), 12 _tribute_ ), 575 `PHASE_DIVISOR` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `opening_time` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanelattribute_ ), 645 _attribute_ ), 553 `phone_mask` ( _kivymd.uix.textfield.textfield.MDTextField_ `opening_time` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDN_ **_a_** _ttributevigationDrawer_ ), 225 _attribute_ ), 539 `position` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `opening_transition` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), 403 _attribute_ ), 575 `prepare_foreground_lock() opening_transition` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ ( _kivymd.tools.hotreload.app.MDApp method_ ), _attribute_ ), 553 701 `opening_transition` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `preview` ( _kivymd.uix.filemanager.filemanager.MDFileManager attribute_ ), 539 _attribute_ ), 260 `opposite` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ `primary_palette` ( _kivymd.theming.ThemeManager atattribute_ ), 431 _tribute_ ), 7 `orientation` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExLinearProgressIndicator_ `primaryColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 157 _attribute_ ), 47 `orientation` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ `primaryContainerColor` _attribute_ ), 375 ( _kivymd.dynamic_color.DynamicColor at-_ `original_argv` ( _in module kivymd.tools.hotreload.app_ ), _tribute_ ), 47 699 `primaryDimColor` ( _kivymd.dynamic_color.DynamicColor_ `outlineColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 47 _attribute_ ), 51 `primaryFixedColor` ( _kivymd.dynamic_color.DynamicColor_ `outlineVariantColor` _attribute_ ), 48 ( _kivymd.dynamic_color.DynamicColor at-_ `primaryFixedDimColor` _tribute_ ), 51 ( _kivymd.dynamic_color.DynamicColor at-_ `overlap` ( _kivymd.uix.imagelist.imagelist.MDSmartTile tribute_ ), 48 _attribute_ ), 599 `primaryPaletteKeyColorColor overlay_mode` ( _kivymd.uix.imagelist.imagelist.MDSmartTile_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 598 _tribute_ ), 52 `PY3` ( _in module kivymd.tools.hotreload.app_ ), 699 P `p0` ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 725 R `p1` ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 725 `radio_icon_down` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `p2` ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 725 _attribute_ ), 609 `p3` ( _kivymd.utils.cubic_bezier.CubicBezier attribute_ ), 725 `radio_icon_normal` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `padding` ( _kivymd.uix.carousel.carousel.MDCarousel atattribute_ ), 609 _tribute_ ), 284 `radius` ( _kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior_ `padding` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerattribute_ ), 670 _attribute_ ), 537 `radius` ( _kivymd.uix.behaviors.stencil_behavior.StencilBehavior_ `pagination_menu_height` _attribute_ ), 673 ( _kivymd.uix.datatables.datatables.MDDataTable_ `radius` ( _kivymd.uix.button.button.BaseFabButton atattribute_ ), 178 _tribute_ ), 303 `pagination_menu_pos radius` ( _kivymd.uix.button.button.MDButton attribute_ ), ( _kivymd.uix.datatables.datatables.MDDataTable_ 304 _attribute_ ), 177 `radius` ( _kivymd.uix.card.card.MDCard attribute_ ), 574 `palette` ( _kivymd.uix.progressindicator.progressindicator.MDCircularProgressIndicator_ `radius` ( _kivymd.uix.carousel.carousel.MDCarouselItem attribute_ ), 377 _attribute_ ), 283 `radius` ( _kivymd.uix.chip.chip.MDChip attribute_ ), 368 

**Index** 

**760** 

**KivyMD, Release 2.0.1.dev0** 

`radius` ( _kivymd.uix.datatables.datatables.MDDataTable_ `refresh_lines()` ( _attribute_ ), 177 _method_ ), 156 `radius` ( _kivymd.uix.dialog.dialog.MDDialog attribute_ ), `register` ( _in module kivymd.factory_registers_ ), 694 590 `remove_marked_icon_from_chip() radius` ( _kivymd.uix.label.label.MDLabel attribute_ ), 464 ( _kivymd.uix.chip.chip.MDChip method_ ), `radius` ( _kivymd.uix.menu.menu.MDDropdownMenu at-_ 368 _tribute_ ), 404 `remove_row()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `radius` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail method_ ), 188 _attribute_ ), 249 `remove_tooltip()` ( _kivymd.uix.tooltip.tooltip.MDTooltip_ `radius` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemmethod_ ), 197 _attribute_ ), 248 `remove_widget()` ( _kivymd.theming.ThemableBehavior_ `radius` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickermethod_ ), 24 _attribute_ ), 338 `remove_widget()` ( _kivymd.uix.circularlayout.MDCircularLayout_ `radius` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePickermethod_ ), 74 _attribute_ ), 321 `remove_widget()` ( _kivymd.uix.search.search.MDSearchViewContainer_ `radius` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicatormethod_ ), 477 _attribute_ ), 375 `remove_widget()` ( `radius` ( _kivymd.uix.slider.slider.MDSliderHandle atmethod_ ), 429 _tribute_ ), 545 `remove_widget()` ( _kivymd.uix.swiper.swiper.MDSwiper_ `radius` ( _kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar method_ ), 203 _attribute_ ), 494 `render_advanced_wave() radius` ( _kivymd.uix.snackbar.snackbar.MDSnackbar at-_ ( _tribute_ ), 486 _method_ ), 158 `radius` ( _kivymd.uix.textfield.textfield.MDTextField_ `render_cont_wave()` ( _attribute_ ), 221 _method_ ), 157 `RAISE_ERROR` ( _kivymd.tools.hotreload.app.MDApp at-_ `render_determinate_wave()` _tribute_ ), 700 ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `re_additional_icons` ( _in module method_ ), 156 _kivymd.tools.release.update_icons_ ), 713 `render_determinate_wave() re_icon_definitions` ( _in module_ ( _kivymd.tools.release.update_icons_ ), 713 _method_ ), 158 `re_icons_json` ( _in module_ `render_determinate_wave()` _kivymd.tools.release.update_icons_ ), 713 ( `re_quote_keys` ( _in module method_ ), 157 _kivymd.tools.release.update_icons_ ), 713 `render_discts_wave() re_version` ( _in module_ ( _kivymd.tools.release.update_icons_ ), 713 _method_ ), 157 `re_version_in_file` ( _in module_ `render_indeterminate_wave()` _kivymd.tools.release.update_icons_ ), 713 ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `rearm_idle()` ( _kivymd.tools.hotreload.app.MDApp method_ ), 156 _method_ ), 701 `render_indeterminate_wave() rebuild()` ( _kivymd.tools.hotreload.app.MDApp_ ( _method_ ), 700 _method_ ), 158 `recalculate_tab_widths() render_indeterminate_wave()` ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), ( 141 _method_ ), 157 `RectangularRippleBehavior` ( _class in_ `render_retreat_wave()` _kivymd.uix.behaviors.ripple_behavior_ ), 645 ( `RectangularRippleBehavior` ( _in module method_ ), 158 _kivymd.uix.behaviors.ripple_behavior_ ), 646 `replace_in_file()` ( _in module_ `refresh_callback` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayoutkivymd.tools.release.make_release_ ), 712 _attribute_ ), 266 `required` ( _kivymd.uix.textfield.textfield.MDTextField at-_ `refresh_done()` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayouttribute_ ), 221 

_method_ ), 267 

**Index** 

**761** 

**KivyMD, Release 2.0.1.dev0** 

_method_ ), 156 `role` ( _kivymd.uix.textfield.textfield.MDTextField at-_ `reset_scale()` ( _kivymd.uix.scrollview.StretchOverScrollStencil tribute_ ), 220 _method_ ), 68 `root_layout` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout_ `restore_calendar_layout_properties()` _attribute_ ), 266 ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `rotate_value` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior method_ ), 339 _attribute_ ), 651 `reversed` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ `rotate_value_angle` ( _attribute_ ), 375 _attribute_ ), 638 `ripple_alpha` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `rotate_value_angle` ( _kivymd.uix.behaviors.rotate_behavior.RotateBehavior attribute_ ), 642 _attribute_ ), 640 `ripple_alpha` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `rotate_value_axis` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior attribute_ ), 645 _attribute_ ), 638 `ripple_behavior` ( _kivymd.uix.card.card.MDCard at-_ `rotate_value_axis` ( _kivymd.uix.behaviors.rotate_behavior.RotateBehavior tribute_ ), 574 _attribute_ ), 640 `ripple_canvas_after RotateBehavior` ( _class in_ ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple kivymd.uix.behaviors.rotate_behavior_ ), 640 _attribute_ ), 643 `row_data` ( _kivymd.uix.datatables.datatables.MDDataTable_ `ripple_color` ( _kivymd.uix.behaviors.ripple_behavior.CommonRippleattribute_ ), 164 _attribute_ ), 642 `row_spacing` ( _kivymd.uix.circularlayout.MDCircularLayout_ `ripple_duration_in_fast` _attribute_ ), 74 ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `rows_num` ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 643 _attribute_ ), 177 `ripple_duration_in_slow run_pre_commit()` ( _in module_ ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple kivymd.tools.release.make_release_ ), 712 _attribute_ ), 643 `running_away()` ( `ripple_duration_out` _method_ ), 377 ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `running_determinate_duration` _attribute_ ), 643 ( `ripple_effect` ( _kivymd.uix.behaviors.ripple_behavior.CommonRippleattribute_ ), 376 _attribute_ ), 644 `running_determinate_transition ripple_effect` ( _kivymd.uix.imagelist.imagelist.MDSmartTile_ ( _attribute_ ), 599 _attribute_ ), 376 `ripple_effect` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `running_indeterminate_duration` _attribute_ ), 611 ( `ripple_func` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRippleattribute_ ), 376 _attribute_ ), 645 `running_indeterminate_transition ripple_func_in` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ ( _attribute_ ), 644 _attribute_ ), 376 `ripple_func_out` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple attribute_ ), 644 S `ripple_origin_to_center save_frame_context()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ ( _attribute_ ), 645 _method_ ), 157 `ripple_rad_default` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ `save_frame_context()` _attribute_ ), 642 ( `ripple_scale` ( _kivymd.uix.behaviors.ripple_behavior.CircularRippleBehaviormethod_ ), 158 _attribute_ ), 645 `save_frame_context() ripple_scale` ( _kivymd.uix.behaviors.ripple_behavior.CommonRipple_ ( _attribute_ ), 643 _method_ ), 157 `ripple_scale` ( _kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior_ `scale_axis` ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 645 _attribute_ ), 68 `rippleColor` ( _kivymd.dynamic_color.DynamicColor at-_ `scale_value` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior tribute_ ), 52 _attribute_ ), 651 `role` ( _kivymd.uix.label.label.MDLabel attribute_ ), 463 

**Index** 

**762** 

**KivyMD, Release 2.0.1.dev0** 

`scale_value_center` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior_ `secondaryFixedColor` _attribute_ ), 638 ( _kivymd.dynamic_color.DynamicColor at-_ `scale_value_center` ( _kivymd.uix.behaviors.scale_behavior.ScaleBehaviortribute_ ), 48 _attribute_ ), 618 `secondaryFixedDimColor scale_value_x` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavior_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 638 _tribute_ ), 48 `scale_value_x` ( _kivymd.uix.behaviors.scale_behavior.ScaleBehavior_ `secondaryPaletteKeyColorColor` _attribute_ ), 618 ( _kivymd.dynamic_color.DynamicColor at-_ `scale_value_y` ( _kivymd.uix.behaviors.elevation.CommonElevationBehaviortribute_ ), 52 _attribute_ ), 638 `segmented_button_opacity_value_disabled_container scale_value_y` ( _kivymd.uix.behaviors.scale_behavior.ScaleBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 618 _attribute_ ), 666 `scale_value_y` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailItemLabel_ `segmented_button_opacity_value_disabled_container_active` _attribute_ ), 248 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `scale_value_z` ( _kivymd.uix.behaviors.elevation.CommonElevationBehaviorattribute_ ), 666 _attribute_ ), 638 `segmented_button_opacity_value_disabled_icon scale_value_z` ( _kivymd.uix.behaviors.scale_behavior.ScaleBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 618 _attribute_ ), 666 `ScaleBehavior` ( _class in_ `segmented_button_opacity_value_disabled_line` _kivymd.uix.behaviors.scale_behavior_ ), 618 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `scrim_alpha_transition` _attribute_ ), 666 ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `segmented_button_opacity_value_disabled_text` _attribute_ ), 539 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `scrim_color` ( _kivymd.uix.dialog.dialog.MDDialog atattribute_ ), 666 _tribute_ ), 590 `sel_day` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `scrim_color` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerattribute_ ), 339 _attribute_ ), 537 `sel_month` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `scrim_color` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePickerattribute_ ), 339 _attribute_ ), 338 `sel_year` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `scrim_color` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePickerattribute_ ), 339 _attribute_ ), 321 `select_dir_or_file() scrimColor` ( _kivymd.dynamic_color.DynamicColor at-_ ( _kivymd.uix.filemanager.filemanager.MDFileManager tribute_ ), 52 _method_ ), 261 `scroll` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `select_directory_on_press_button()` _attribute_ ), 674 ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `scroll_cls` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 261 _attribute_ ), 513 `select_path` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `scroll_friction` ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 260 _attribute_ ), 68 `selected` ( _kivymd.uix.navigationdrawer.navigationdrawer.BaseNavigationDrawerItem_ `scroll_offset` ( _kivymd.uix.carousel.carousel.MDCarousel attribute_ ), 534 _attribute_ ), 285 `selected_color` ( _kivymd.uix.chip.chip.MDChip at-_ `scroll_scale` ( _kivymd.uix.scrollview.StretchOverScrollStencil tribute_ ), 368 _attribute_ ), 68 `selected_color` ( `scroll_view` ( _kivymd.uix.scrollview.StretchOverScrollStencil attribute_ ), 427 _attribute_ ), 68 `selected_color` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `search` ( _kivymd.uix.filemanager.filemanager.MDFileManager attribute_ ), 610 _attribute_ ), 260 `selected_icon_color secondaryColor` ( _kivymd.dynamic_color.DynamicColor_ ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton attribute_ ), 48 _attribute_ ), 428 `secondaryContainerColor selected_segments` ( ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 428 _tribute_ ), 48 `selection` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `secondaryDimColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 261 _attribute_ ), 48 `selection_button` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ 

**Index** 

**763** 

**KivyMD, Release 2.0.1.dev0** 

_attribute_ ), 261 ( _kivymd.uix.menu.menu.MDDropdownMenu_ `selector` ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 404 _attribute_ ), 261 `set_norm_value()` ( `set_active_item()` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationBarmethod_ ), 156 _method_ ), 279 `set_opacity()` ( `set_active_item()` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRailmethod_ ), 668 _method_ ), 249 `set_opacity_text_button() set_active_item()` ( _kivymd.uix.tab.tab.MDTabsPrimary_ ( _kivymd.uix.behaviors.motion_behavior.MotionExtendedFabButtonBehavior method_ ), 140 _method_ ), 669 `set_all_rows_checked() set_pos_hint_text()` ( _kivymd.uix.datatables.datatables.MDDataTable_ ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 184 _method_ ), 231 `set_bars_color` ( _kivymd.uix.appbar.appbar.MDTopAppBar_ `set_properties()` ( _kivymd.uix.behaviors.toggle_behavior.MDToggleButtonBehavior attribute_ ), 511 _method_ ), 624 `set_bars_color` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationBar_ `set_properties_widget()` _attribute_ ), 278 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `set_bars_colors()` ( _in module method_ ), 667 _kivymd.utils.set_bars_colors_ ), 727 `set_properties_widget() set_calendar_layout_properties()` ( _kivymd.uix.button.button.MDButton method_ ), ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ 305 _method_ ), 339 `set_properties_widget() set_chevron_down()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ ( _kivymd.uix.button.button.MDFabButton method_ ), 553 _method_ ), 306 `set_chevron_up()` ( _kivymd.uix.expansionpanel.expansionpanel.MDExpansionPanel_ `set_properties_widget()` _method_ ), 553 ( _kivymd.uix.card.card.MDCard method_ ), `set_child_active()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ 574 _method_ ), 610 `set_properties_widget() set_chip_bg_color()` ( _kivymd.uix.chip.chip.MDChip_ ( _kivymd.uix.dialog.dialog.MDDialog method_ ), _method_ ), 369 591 `set_colors()` ( _kivymd.theming.ThemeManager_ `set_properties_widget()` _method_ ), 21 ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `set_current()` ( _kivymd.uix.swiper.swiper.MDSwiper method_ ), 540 _method_ ), 203 `set_root_active()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `set_dark_mode_listener` ( _in module kivymd.theming_ ), _method_ ), 610 7 `set_row_checked()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `set_error()` ( _kivymd.tools.hotreload.app.MDApp method_ ), 181 _method_ ), 700 `set_rows_checked()` ( _kivymd.uix.datatables.datatables.MDDataTable_ `set_fab_icon()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 184 _method_ ), 514 `set_scale()` ( _kivymd.uix.behaviors.motion_behavior.MotionDropDownMenuBehavior_ `set_fab_opacity()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar method_ ), 668 _method_ ), 513 `set_scale_origin()` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `set_hint_text_font_size()` _method_ ), 68 ( _kivymd.uix.textfield.textfield.MDTextField_ `set_screen()` ( _kivymd.uix.responsivelayout.MDResponsiveLayout method_ ), 231 _method_ ), 84 `set_icon()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `set_selected_widget()` _method_ ), 614 ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `set_input_date()` ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePickermethod_ ), 339 _method_ ), 341 `set_shader()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `set_max_text_length()` _method_ ), 646 ( _kivymd.uix.textfield.textfield.MDTextField_ `set_space_in_line()` _method_ ), 231 ( _kivymd.uix.textfield.textfield.MDTextField_ `set_menu_pos()` ( _kivymd.uix.menu.menu.MDDropdownMenu method_ ), 231 _method_ ), 404 `set_state()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `set_menu_properties()` _method_ ), 540 

**Index** 

**764** 

**KivyMD, Release 2.0.1.dev0** 

`set_status_bar_color() show()` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ ( _kivymd.uix.navigationbar.navigationbar.MDNavigationBarmethod_ ), 261 _method_ ), 279 `show_bar()` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `set_target_height()` _method_ ), 513 ( _kivymd.uix.menu.menu.MDDropdownMenu_ `show_button_container_transition` _method_ ), 404 ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior_ `set_text()` ( _kivymd.uix.textfield.textfield.MDTextField attribute_ ), 669 _method_ ), 231 `show_child()` ( _kivymd.uix.search.search.MDSearchViewContainer_ `set_text_full_date()` _method_ ), 477 ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `show_disks()` ( _kivymd.uix.filemanager.filemanager.MDFileManager method_ ), 339 _method_ ), 261 `set_texture_color() show_duration` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ ( _kivymd.uix.textfield.textfield.MDTextField attribute_ ), 512 _method_ ), 230 `show_duration` ( _kivymd.uix.behaviors.motion_behavior.MotionBase_ `set_time()` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePickerattribute_ ), 668 _method_ ), 321 `show_duration` ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior_ `set_widget()` ( _kivymd.tools.hotreload.app.MDApp attribute_ ), 669 _method_ ), 701 `show_duration` ( `setup_lines()` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBarattribute_ ), 668 _method_ ), 156 `show_duration` ( `shadow_color` ( _kivymd.uix.behaviors.elevation.CommonElevationBehavattr bute_ **_i_** _or_ ), 669 _attribute_ ), 637 `show_duration` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout_ `shadow_offset` ( _kivymd.uix.behaviors.elevation.CommonElevationBehaviorattribute_ ), 266 _attribute_ ), 635 `show_hidden_files` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `shadow_radius` ( _kivymd.uix.behaviors.elevation.CommonElevationBehaviorattribute_ ), 260 _attribute_ ), 632 `show_transition` ( _kivymd.uix.appbar.appbar.MDBottomAppBar_ `shadow_radius` ( _kivymd.uix.button.button.BaseButton attribute_ ), 512 _attribute_ ), 304 `show_transition` ( _kivymd.uix.behaviors.motion_behavior.MotionBase_ `shadow_softness` ( _kivymd.uix.behaviors.elevation.CommonElevationBehaviorattribute_ ), 668 _attribute_ ), 634 `show_transition` ( _kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior_ `shadowColor` ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 669 _tribute_ ), 52 `show_transition` ( `shake()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior attribute_ ), 668 _method_ ), 651 `show_transition` ( `shape` ( _kivymd.uix.fitimage.fitimage.FitImage attribute_ ), _attribute_ ), 669 556 `show_transition` ( `shape` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicatorattribute_ ), 266 _attribute_ ), 144 `shrink()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior_ `shape_index` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingInmetho_ **_d_** _icator_ ), 651 _attribute_ ), 145 `shrink_extent` ( _kivymd.uix.carousel.carousel.MDCarousel_ `shape_sequence` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicatorattribute_ ), 285 _attribute_ ), 144 `size` ( _kivymd.uix.slider.slider.MDSliderHandle at-_ `shape_size` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicatortribute_ ), 545 _attribute_ ), 144 `size` ( _kivymd.uix.slider.slider.MDSliderValueLabel at-_ `sheet_type` ( _kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet tribute_ ), 546 _attribute_ ), 443 `size_duration` ( _kivymd.uix.swiper.swiper.MDSwiper_ `shift_left` ( _kivymd.uix.tooltip.tooltip.MDTooltip attribute_ ), 202 _attribute_ ), 197 `size_transition` ( _kivymd.uix.swiper.swiper.MDSwiper_ `shift_right` ( _kivymd.uix.tooltip.tooltip.MDTooltip atattribute_ ), 202 _tribute_ ), 196 `slide_distance` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ `shift_transition` ( _kivymd.uix.behaviors.motion_behavior.MotionExa tribute_ **_t_** _endedFabButtonBehavior_ ), 431 _attribute_ ), 669 `sort_by` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ `shift_y` ( _kivymd.uix.tooltip.tooltip.MDTooltip attribute_ ), _attribute_ ), 261 196 `sort_by_desc` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ 

**Index** 

**765** 

**KivyMD, Release 2.0.1.dev0** 

_attribute_ ), 261 _attribute_ ), 665 `sorted_on` ( _kivymd.uix.datatables.datatables.MDDataTable_ `StateFocusBehavior` ( _class in attribute_ ), 175 _kivymd.uix.behaviors.focus_behavior_ ), 621 `sorted_order` ( _kivymd.uix.datatables.datatables.MDDataTable_ `StateLayerBehavior` ( _class in attribute_ ), 175 _kivymd.uix.behaviors.state_layer_behavior_ ), `source` ( _kivymd.uix.label.label.MDIcon attribute_ ), 465 665 `spacing` ( _kivymd.uix.carousel.carousel.MDCarousel at-_ `status` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer tribute_ ), 285 _attribute_ ), 538 `spacing` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `StencilBehavior` ( _class in attribute_ ), 156 _kivymd.uix.behaviors.stencil_behavior_ ), 673 `spacing` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerMenu_ `step_point_size` ( _kivymd.uix.slider.slider.MDSlider attribute_ ), 536 _attribute_ ), 543 `sparkle_color` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRipple_ `StiffScrollEffect` ( _class in attribute_ ), 645 _kivymd.effects.stiffscroll.stiffscroll_ ), 674 `SPIN_ROTATION_DEGREES stop()` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateRetreatAnimatormethod_ ), 675 _attribute_ ), 718 `stop()` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicator_ `spinner_color` ( _kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayoutmethod_ ), 145 _attribute_ ), 266 `stop()` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ `start()` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect method_ ), 377 _method_ ), 675 `stretch_intensity` ( _kivymd.uix.scrollview.StretchOverScrollStencil_ `start()` ( _kivymd.uix.loadingindicator.loadingindicator.MDLoadingIndicatorattribute_ ), 67 _method_ ), 145 `StretchOverScrollBehavior` ( _class in_ `start()` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicatkivymd.uix.scr_ **_o_** _llviewr_ ), 68 _method_ ), 376 `StretchOverScrollStencil` ( _class in_ `start()` ( _kivymd.uix.transition.transition.MDFadeSlideTransition kivymd.uix.scrollview_ ), 67 _method_ ), 431 `style` ( _kivymd.uix.button.button.BaseFabButton at-_ `start()` ( _kivymd.uix.transition.transition.MDSharedAxisTransition tribute_ ), 303 _method_ ), 432 `style` ( _kivymd.uix.button.button.MDButton attribute_ ), `start()` ( _kivymd.uix.transition.transition.MDTransitionBase_ 304 _method_ ), 430 `style` ( _kivymd.uix.button.button.MDIconButton at-_ `start()` ( _kivymd.utils.fpsmonitor.FpsMonitor method_ ), _tribute_ ), 305 727 `style` ( _kivymd.uix.card.card.MDCard attribute_ ), 574 `start_from` ( _kivymd.uix.circularlayout.MDCircularLayout_ `supporting_input_text` _attribute_ ), 73 ( _kivymd.uix.pickers.datepicker.datepicker.MDModalInputDatePicker_ `start_ripple()` ( _kivymd.uix.behaviors.ripple_behavior.CommonRippleattribute_ ), 341 _method_ ), 644 `supporting_text` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ `start_ripple()` ( _kivymd.uix.behaviors.ripple_behavior.M3CommonRippleattribute_ ), 338 _method_ ), 646 `supporting_text` ( _kivymd.uix.search.search.MDSearchBar_ `state` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), _attribute_ ), 477 575 `surfaceBrightColor` ( _kivymd.dynamic_color.DynamicColor_ `state` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerattribute_ ), 50 _attribute_ ), 538 `surfaceColor` ( _kivymd.dynamic_color.DynamicColor_ `state_drag` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 49 _attribute_ ), 665 `surfaceContainerColor state_hover` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 665 _tribute_ ), 50 `state_layer_color` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `surfaceContainerHighColor` _attribute_ ), 665 ( _kivymd.dynamic_color.DynamicColor at-_ `state_layer_color` ( _kivymd.uix.slider.slider.MDSliderHandle tribute_ ), 50 _attribute_ ), 545 `surfaceContainerHighestColor state_layer_size` ( _kivymd.uix.slider.slider.MDSliderHandle_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 545 _tribute_ ), 50 `state_press` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `surfaceContainerLowColor` 

**Index** 

**766** 

**KivyMD, Release 2.0.1.dev0** 

###### T 

( _kivymd.dynamic_color.DynamicColor attribute_ ), 50 `surfaceContainerLowestColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 50 50 `surfaceDimColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 50 50 

`t()` ( _kivymd.utils.cubic_bezier.CubicBezier method_ ), 726 `surfaceContainerLowestColor tablet_view` ( _kivymd.uix.responsivelayout.MDResponsiveLayout_ ( _kivymd.dynamic_color.DynamicColor atattribute_ ), 83 _tribute_ ), 50 50 `tag` ( _kivymd.uix.hero.MDHeroFrom attribute_ ), 107 `surfaceDimColor` ( _kivymd.dynamic_color.DynamicColor_ `tag` ( _kivymd.uix.hero.MDHeroTo attribute_ ), 108 _attribute_ ), 50 50 `TAIL_DEGREES_OFFSET surfaceTintColor` ( _kivymd.dynamic_color.DynamicColor_ ( _attribute_ ), 50 _attribute_ ), 719 `surfaceVariantColor target` ( _kivymd.uix.tab.tab.MDTabsPrimary attribute_ ), ( _kivymd.dynamic_color.DynamicColor at-_ 139 _tribute_ ), 50 `target_widget` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `swipe_distance` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), 675 _attribute_ ), 575 `temp_font_path` ( _in module_ `swipe_distance` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerkivymd.tools.release.update_icons_ ), 712 _attribute_ ), 539 `temp_path` ( _in module_ `swipe_distance` ( _kivymd.uix.swiper.swiper.MDSwiper kivymd.tools.release.update_icons_ ), 712 _attribute_ ), 202 `temp_preview_path` ( _in module_ `swipe_edge_width` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerkivymd.tools.release.update_icons_ ), 712 _attribute_ ), 539 `temp_repo_path` ( _in module_ `swipe_left()` ( _kivymd.uix.swiper.swiper.MDSwiper kivymd.tools.release.update_icons_ ), 712 _method_ ), 203 `tertiaryColor` ( _kivymd.dynamic_color.DynamicColor_ `swipe_on_scroll` ( _kivymd.uix.swiper.swiper.MDSwiper attribute_ ), 49 _attribute_ ), 202 `tertiaryContainerColor swipe_right()` ( _kivymd.uix.swiper.swiper.MDSwiper_ ( _kivymd.dynamic_color.DynamicColor atmethod_ ), 203 _tribute_ ), 49 `swipe_transition` ( _kivymd.uix.swiper.swiper.MDSwiper_ `tertiaryDimColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 202 _attribute_ ), 49 `switch_animation` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ `tertiaryFixedColor` ( _kivymd.dynamic_color.DynamicColor attribute_ ), 431 _attribute_ ), 49 `switch_lang()` ( _kivymd.tools.patterns.MVC.libs.translation.Translation_ `tertiaryFixedDimColor` _method_ ), 710 ( _kivymd.dynamic_color.DynamicColor at-_ `switch_opacity_value_disabled_container` _tribute_ ), 49 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `tertiaryPaletteKeyColorColor` _attribute_ ), 666 666 ( _kivymd.dynamic_color.DynamicColor at-_ `switch_opacity_value_disabled_icon` _tribute_ ), 52 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `text` ( _kivymd.icon_definitions.IconItem attribute_ ), 32 _attribute_ ), 666 `text` ( _kivymd.uix.label.label.MDLabel attribute_ ), 463 `switch_opacity_value_disabled_line text` ( _kivymd.uix.menu.menu.BaseDropdownItem at-_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviortribute_ ), 398 _attribute_ ), 666 `text` ( _kivymd.uix.search.search.MDSearchBar attribute_ ), `switch_tab()` ( _kivymd.uix.tab.tab.MDTabsPrimary_ 478 _method_ ), 140 140 `text_button_cancel` ( `switch_theme()` ( _kivymd.theming.ThemeManager attribute_ ), 339 _method_ ), 21 21 `text_button_cancel` ( `switch_theme_system()` _attribute_ ), 321 ( _kivymd.theming.ThemeManager method_ ), `text_button_ok` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker_ 21 _attribute_ ), 338 `switch_thumb_opacity_value_disabled_container text_button_ok` ( ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 321 _attribute_ ), 666 `text_color` ( _kivymd.uix.label.label.MDLabel attribute_ ), `sync_theme_styles()` 464 

`switch_opacity_value_disabled_container` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior attribute_ ), 666 666 

`switch_tab()` ( _kivymd.uix.tab.tab.MDTabsPrimary method_ ), 140 140 `switch_theme()` ( _kivymd.theming.ThemeManager method_ ), 21 21 `switch_theme_system()` ( _kivymd.theming.ThemeManager method_ ), 21 

`sync_theme_styles()` ( _kivymd.theming.ThemeManager method_ ), 21 

`text_color` ( _kivymd.uix.menu.menu.BaseDropdownItem attribute_ ), 399 

**Index** 

**767** 

**KivyMD, Release 2.0.1.dev0** 

`text_color_active` ( _kivymd.uix.navigationbar.navigationbar.MDNavigationItemLabel_ `theme_focus_color` ( _kivymd.theming.ThemableBehavior attribute_ ), 277 _attribute_ ), 23 `text_color_disabled theme_font_name` ( _kivymd.theming.ThemableBehavior_ ( _kivymd.uix.chip.chip.MDChipText attribute_ ), _attribute_ ), 23 367 `theme_font_size` ( _kivymd.theming.ThemableBehavior_ `text_color_focus` ( _kivymd.uix.textfield.textfield.BaseTextFieldLabelattribute_ ), 22 _attribute_ ), 212 `theme_font_styles` ( _in module_ `text_color_focus` ( _kivymd.uix.textfield.textfield.MDTextField kivymd.font_definitions_ ), 36 _attribute_ ), 221 `theme_height` ( _kivymd.theming.ThemableBehavior at-_ `text_color_normal` ( _kivymd.uix.navigationbar.navigationbar.MDNavtr bu e_ **_i_** _ga_ **_t_** _ionItemLabel_ ), 23 _attribute_ ), 277 `theme_icon_color` ( _kivymd.theming.ThemableBehavior_ `text_color_normal` ( _kivymd.uix.textfield.textfield.BaseTextFieldLabelattribute_ ), 24 _attribute_ ), 212 `theme_line_color` ( _kivymd.theming.ThemableBehavior_ `text_color_normal` ( _kivymd.uix.textfield.textfield.MDTextField attribute_ ), 22 _attribute_ ), 220 `theme_line_height` ( _kivymd.theming.ThemableBehavior_ `text_field_filled_opacity_value_disabled_state_container` _attribute_ ), 23 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `theme_shadow_color` ( _kivymd.theming.ThemableBehavior attribute_ ), 666 _attribute_ ), 22 `text_field_opacity_value_disabled_helper_text_labeltheme_shadow_offset` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ ( _kivymd.theming.ThemableBehavior attribute_ ), _attribute_ ), 667 22 `text_field_opacity_value_disabled_hint_text_labeltheme_shadow_softness` ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ ( _kivymd.theming.ThemableBehavior attribute_ ), _attribute_ ), 667 23 `text_field_opacity_value_disabled_leading_icontheme_style` ( _kivymd.theming.ThemeManager at-_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviortribute_ ), 16 _attribute_ ), 667 `theme_style_switch_animation text_field_opacity_value_disabled_line` ( _kivymd.theming.ThemeManager attribute_ ), 12 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `theme_style_switch_animation_duration` _attribute_ ), 667 ( _kivymd.theming.ThemeManager attribute_ ), 14 `text_field_opacity_value_disabled_max_length_labeltheme_text_color` ( _kivymd.theming.ThemableBehavior_ ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehaviorattribute_ ), 23 _attribute_ ), 667 `theme_width` ( _kivymd.theming.ThemableBehavior_ `text_field_opacity_value_disabled_trailing_icon` _attribute_ ), 22 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `ThemeManager` ( _class in kivymd.theming_ ), 7 _attribute_ ), 667 `thickness` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar_ `text_field_outlined_opacity_value_disabled_state_container` _attribute_ ), 156 ( _kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior_ `thumb_color_active` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch attribute_ ), 667 _attribute_ ), 612 `ThemableBehavior` ( _class in kivymd.theming_ ), 21 `thumb_color_disabled theme_bg_color` ( _kivymd.theming.ThemableBehavior_ ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch attribute_ ), 22 _attribute_ ), 613 `theme_cls` ( _kivymd.app.MDApp attribute_ ), 26 `thumb_color_inactive theme_cls` ( _kivymd.theming.ThemableBehavior at-_ ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch tribute_ ), 21 _attribute_ ), 613 `theme_divider_color time` ( _kivymd.uix.pickers.timepicker.timepicker.MDBaseTimePicker_ ( _kivymd.theming.ThemableBehavior attribute_ ), _attribute_ ), 321 23 `toast()` ( _in module kivymd.toast.androidtoast_ ), 696 `theme_elevation_level toggle_row_checked()` ( _kivymd.theming.ThemableBehavior attribute_ ), ( _kivymd.uix.datatables.datatables.MDDataTable_ 22 _method_ ), 184 `theme_elevation_level tooltip_display_delay` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ ( _kivymd.uix.tooltip.tooltip.MDTooltip atattribute_ ), 539 _tribute_ ), 196 

**Index** 

**768** 

**KivyMD, Release 2.0.1.dev0** 

`TOTAL_CYCLES` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimatortribute_ ), 201 _attribute_ ), 719 `transition_max` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect_ `TOTAL_DURATION_IN_MS` _attribute_ ), 675 ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminateContiguousAnima_ `transition_min` ( _kivymd.effec s.stiffscroll.stiffscroll.StiffScrollEffect_ **_t_** _or attribute_ ), 717 _attribute_ ), 674 `TOTAL_DURATION_IN_MS translate_value` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior_ ( _kivymd.uix.exprogressindicator.animators.LinearIndeterminaat ribute_ **_t_** _eDisjointAnimator_ ), 651 _attribute_ ), 716 `Translation` ( _class in_ `TOTAL_DURATION_MS` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterminateAdvancedAnimkivymd.tools.patterns.MVC.libs.tr_ **_a_** _nslationtor_ ), _attribute_ ), 719 710 `TOTAL_DURATION_MS` ( _kivymd.uix.exprogressindicator.animators.CircularIndeterm_ `transparentColor` ( _k vymd.dynamic_col_ **_i_** _nateRetreatAnimat_ **_or_** _.DynamicColor attribute_ ), 718 _attribute_ ), 52 `TouchBehavior` ( _class in_ `twist()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior kivymd.uix.behaviors.touch_behavior_ ), 664 _method_ ), 651 `track_active_color` ( _kivymd.uix.slider.slider.MDSlider_ `type` ( _kivymd.uix.appbar.appbar.MDTopAppBar atattribute_ ), 543 _tribute_ ), 511 `track_active_step_point_color type` ( _kivymd.uix.chip.chip.MDChip attribute_ ), 368 ( _kivymd.uix.slider.slider.MDSlider attribute_ ), `type` ( _kivymd.uix.navigationrail.navigationrail.MDNavigationRail_ 543 _attribute_ ), 249 `track_active_width` ( _kivymd.uix.slider.slider.MDSlider_ `type` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator attribute_ ), 542 _attribute_ ), 376 `track_color` ( _kivymd.uix.progressindicator.progressindicator.MDLinearProgressIndicator_ `type` ( _kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton attribute_ ), 376 _attribute_ ), 428 `track_color_active` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `type_swipe` ( _kivymd.uix.card.card.MDCardSwipe attribute_ ), 613 _attribute_ ), 575 `track_color_disabled` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ U _attribute_ ), 614 `uix_path` ( _in module kivymd_ ), 694 `track_color_inactive uncontained_item_width` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ ( _kivymd.uix.carousel.carousel.MDCarousel attribute_ ), 613 _attribute_ ), 286 `track_inactive_color unfocus_color` ( _kivymd.uix.behaviors.focus_behavior.StateFocusBehavior_ ( _kivymd.uix.slider.slider.MDSlider attribute_ ), _attribute_ ), 621 543 `unload_app_dependencies() track_inactive_step_point_color` ( _kivymd.tools.hotreload.app.MDApp method_ ), ( _kivymd.uix.slider.slider.MDSlider attribute_ ), 700 543 `unselected_color` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `track_inactive_width` _attribute_ ), 610 ( _kivymd.uix.slider.slider.MDSlider attribute_ ), `unzip_archive()` ( _in module_ 542 _kivymd.tools.release.update_icons_ ), 713 `trailing_icon` ( _kivymd.uix.menu.menu.BaseDropdownItem_ `update()` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffect attribute_ ), 399 _method_ ), 675 `trailing_icon_color update_background_origin()` ( _kivymd.uix.menu.menu.BaseDropdownItem_ ( _kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior attribute_ ), 399 _method_ ), 671 `trailing_text` ( _kivymd.uix.menu.menu.BaseDropdownItem_ `update_calendar()` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 399 _method_ ), 339 `trailing_text_color update_calendar()` ( ( _kivymd.uix.menu.menu.BaseDropdownItem method_ ), 341 _attribute_ ), 399 `update_canvas_bg_pos() transition_axis` ( _kivymd.uix.transition.transition.MDSharedAxisTransition_ ( _kivymd.uix.label.label.MDLabel method_ ), _attribute_ ), 431 465 `transition_duration update_colors()` ( _kivymd.uix.textfield.textfield.MDTextField_ ( _kivymd.uix.swiper.swiper.MDSwiper atmethod_ ), 230 

**Index** 

**769** 

**KivyMD, Release 2.0.1.dev0** 

`update_fps()` ( _kivymd.utils.fpsmonitor.FpsMonitor_ `validator` ( _kivymd.uix.textfield.textfield.MDTextField method_ ), 727 _attribute_ ), 225 `update_icon()` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox_ `value` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExBaseProgressBar method_ ), 610 _attribute_ ), 155 `update_icons()` ( _in module_ `value_container_hide_anim_duration` _kivymd.tools.release.update_icons_ ), 713 ( _kivymd.uix.slider.slider.MDSlider attribute_ ), `update_indicator()` ( _kivymd.uix.tab.tab.MDTabsPrimary_ 543 _method_ ), 140 `value_container_hide_anim_transition update_items_color()` ( _kivymd.uix.slider.slider.MDSlider attribute_ ), ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawerMenu_ 543 _method_ ), 537 `value_container_show_anim_duration update_points()` ( _kivymd.uix.slider.slider.MDSlider_ ( _kivymd.uix.slider.slider.MDSlider attribute_ ), _method_ ), 544 543 `update_pos()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationLayout_ `value_container_show_anim_transition` _method_ ), 534 ( _kivymd.uix.slider.slider.MDSlider attribute_ ), `update_readme()` ( _in module_ 543 _kivymd.tools.release.make_release_ ), 712 `value_normalized` ( `update_row()` ( _kivymd.uix.datatables.datatables.MDDataTable attribute_ ), 155 _method_ ), 188 `ver_growth` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `update_row_data()` ( _kivymd.uix.datatables.datatables.MDDataTableattribute_ ), 401 _method_ ), 185 `view_root` ( _kivymd.uix.search.search.MDSearchBar at-_ `update_scrim_rectangle()` _tribute_ ), 477 ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationLayout method_ ), 534 W `update_status()` ( _kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer_ `w_seg()` ( _method_ ), 540 _method_ ), 158 `update_text_item()` ( _kivymd.uix.dropdownitem.dropdownitem.MDDropDownItem_ `w_seg()` ( _method_ ), 234 _method_ ), 157 `update_texture()` ( _kivymd.uix.fitimage.fitimage.FitImage_ `wave_length` ( _method_ ), 561 _attribute_ ), 156 `update_theme_colors() wave_speed` ( ( _kivymd.theming.ThemeManager method_ ), _attribute_ ), 156 21 `widgets` ( _kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior_ `update_velocity()` ( _kivymd.effects.stiffscroll.stiffscroll.StiffScrollEffectattribute_ ), 660 _method_ ), 675 `width` ( _kivymd.uix.selectioncontrol.selectioncontrol.MDSwitch_ `update_version_py()` ( _in module attribute_ ), 611 _kivymd.tools.release.make_release_ ), 712 `width_mult` ( _kivymd.uix.menu.menu.MDDropdownMenu_ `update_width()` ( _kivymd.uix.dialog.dialog.MDDialog attribute_ ), 400 _method_ ), 590 `width_mult` ( _kivymd.uix.swiper.swiper.MDSwiper_ `updated_interval` ( _kivymd.utils.fpsmonitor.FpsMonitor attribute_ ), 202 _attribute_ ), 727 `width_offset` ( _kivymd.uix.dialog.dialog.MDDialog at-_ `upload_file()` ( _kivymd.tools.patterns.MVC.Model.database_restdb.DataBasetribute_ ), 590 _method_ ), 710 `WindowController` ( _class in_ `url` ( _in module kivymd.tools.release.update_icons_ ), 712 _kivymd.uix.controllers.windowcontroller_ ), `use_access` ( _kivymd.uix.filemanager.filemanager.MDFileManager_ 616 _attribute_ ), 260 `wobble()` ( _kivymd.uix.behaviors.magic_behavior.MagicBehavior_ `use_color_array` ( _kivymd.uix.exprogressindicator.exprogressindicator.MDExCircularProgressIndicatormethod_ ), 651 _attribute_ ), 157 `use_pagination` ( _kivymd.uix.datatables.datatables.MDDataTable_ Y _attribute_ ), 176 `year` ( _kivymd.uix.pickers.datepicker.datepicker.MDBaseDatePicker attribute_ ), 338 

###### V 

`Validator` ( _class in kivymd.uix.textfield.textfield_ ), 211 

**Index** 

**770** 

