"""
Tests para data/totp.py - Autenticación 2FA TOTP
"""
import pytest
import time
from data import totp


class TestGenerateSecret:
    """Tests para generación de secretos TOTP"""
    
    def test_generate_secret_returns_base32(self):
        """El secreto está en formato Base32"""
        secret = totp.generate_secret()
        # Base32 solo contiene A-Z y 2-7
        valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567")
        assert all(c in valid_chars for c in secret)
    
    def test_generate_secret_length(self):
        """Secretos tienen longitud adecuada (20 bytes = 32 chars Base32)"""
        secret = totp.generate_secret()
        assert len(secret) == 32  # 20 bytes en Base32
    
    def test_generate_secret_unique(self):
        """Cada secreto generado es único"""
        secrets = [totp.generate_secret() for _ in range(100)]
        assert len(set(secrets)) == 100  # Todos únicos
    
    def test_generate_secret_custom_length(self):
        """Se puede especificar longitud personalizada"""
        secret = totp.generate_secret(length_bytes=32)
        # 32 bytes en Base32 = ~52 caracteres
        assert len(secret) >= 50


class TestCurrentCode:
    """Tests para generación de códigos TOTP"""
    
    def test_current_code_format(self):
        """Código tiene 6 dígitos numéricos"""
        secret = totp.generate_secret()
        code = totp.current_code(secret)
        
        assert len(code) == 6
        assert code.isdigit()
    
    def test_current_code_deterministic(self):
        """Mismo tiempo + mismo secreto = mismo código"""
        secret = "TESTSECRET123456"
        fixed_time = 1700000000
        
        code1 = totp.current_code(secret, for_time=fixed_time)
        code2 = totp.current_code(secret, for_time=fixed_time)
        
        assert code1 == code2
    
    def test_current_code_changes_with_time(self):
        """Código cambia cada 30 segundos"""
        secret = totp.generate_secret()
        
        code1 = totp.current_code(secret, for_time=1700000000)
        code2 = totp.current_code(secret, for_time=1700000030)  # 30s después
        
        # Pueden ser iguales si estamos en el borde, pero generalmente diferentes
        # Probamos con 60s de diferencia para asegurar
        code3 = totp.current_code(secret, for_time=1700000060)
        
        assert code1 != code3 or code2 != code3


class TestVerify:
    """Tests para verificación de códigos TOTP"""
    
    def test_verify_valid_code(self):
        """Código válido dentro de ventana se verifica"""
        secret = totp.generate_secret()
        current_time = time.time()
        code = totp.current_code(secret, for_time=current_time)
        
        assert totp.verify(secret, code, for_time=current_time) is True
    
    def test_verify_invalid_code(self):
        """Código inválido no se verifica"""
        secret = totp.generate_secret()
        
        assert totp.verify(secret, "000000", for_time=time.time()) is False
        assert totp.verify(secret, "abcdef", for_time=time.time()) is False
    
    def test_verify_window_past(self):
        """Acepta código de hace 30s (ventana -1)"""
        secret = totp.generate_secret()
        current_time = 1700000060
        past_time = current_time - 30
        
        code_past = totp.current_code(secret, for_time=past_time)
        
        # Verificar en tiempo actual acepta código del periodo anterior
        assert totp.verify(secret, code_past, window=1, for_time=current_time) is True
    
    def test_verify_window_future(self):
        """Acepta código de dentro de 30s (ventana +1) por desfase de reloj"""
        secret = totp.generate_secret()
        current_time = 1700000000
        future_time = current_time + 30
        
        code_future = totp.current_code(secret, for_time=future_time)
        
        # Verificar en tiempo actual acepta código del periodo siguiente
        assert totp.verify(secret, code_future, window=1, for_time=current_time) is True
    
    def test_verify_outside_window(self):
        """Rechaza código fuera de ventana ±1"""
        secret = totp.generate_secret()
        current_time = 1700000120
        old_time = current_time - 90  # 3 periodos atrás
        
        code_old = totp.current_code(secret, for_time=old_time)
        
        # Con ventana=1, no debería aceptar código de hace 90s
        assert totp.verify(secret, code_old, window=1, for_time=current_time) is False
    
    def test_verify_empty_code(self):
        """Código vacío retorna False"""
        secret = totp.generate_secret()
        
        assert totp.verify(secret, "", for_time=time.time()) is False
        assert totp.verify(secret, None, for_time=time.time()) is False
    
    def test_verify_wrong_length(self):
        """Código con longitud incorrecta retorna False"""
        secret = totp.generate_secret()
        
        assert totp.verify(secret, "12345", for_time=time.time()) is False  # 5 dígitos
        assert totp.verify(secret, "1234567", for_time=time.time()) is False  # 7 dígitos
    
    def test_verify_non_numeric(self):
        """Código no numérico retorna False"""
        secret = totp.generate_secret()
        
        assert totp.verify(secret, "abcdef", for_time=time.time()) is False
        assert totp.verify(secret, "12345a", for_time=time.time()) is False
    
    def test_verify_with_spaces(self):
        """Código con espacios se limpia y verifica"""
        secret = totp.generate_secret()
        current_time = time.time()
        code = totp.current_code(secret, for_time=current_time)
        
        # Añadir espacios
        code_spaced = f"{code[:3]} {code[3:]}"
        
        assert totp.verify(secret, code_spaced, for_time=current_time) is True


class TestProvisioningURI:
    """Tests para URI de aprovisionamiento"""
    
    def test_provisioning_uri_format(self):
        """URI sigue formato otpauth://"""
        secret = "TESTSECRET"
        uri = totp.provisioning_uri(secret, "user@example.com")
        
        assert uri.startswith("otpauth://totp/")
        assert "secret=TESTSECRET" in uri
    
    def test_provisioning_uri_includes_issuer(self):
        """URI incluye issuer por defecto"""
        secret = "TESTSECRET"
        uri = totp.provisioning_uri(secret, "user@example.com")
        
        assert "issuer=SistemaVentas" in uri
    
    def test_provisioning_uri_custom_issuer(self):
        """URI respeta issuer personalizado"""
        secret = "TESTSECRET"
        uri = totp.provisioning_uri(secret, "user@example.com", issuer="MiEmpresa")
        
        assert "issuer=MiEmpresa" in uri
        assert "MiEmpresa:user@example.com" in uri
    
    def test_provisioning_uri_includes_params(self):
        """URI incluye parámetros requeridos"""
        secret = "TESTSECRET"
        uri = totp.provisioning_uri(secret, "user@example.com")
        
        assert "digits=6" in uri
        assert "period=30" in uri


class TestRecoveryCodes:
    """Tests para códigos de recuperación"""
    
    def test_generate_recovery_codes_count(self):
        """Genera cantidad correcta de códigos"""
        codes = totp.generate_recovery_codes(n=8)
        assert len(codes) == 8
        
        codes = totp.generate_recovery_codes(n=10)
        assert len(codes) == 10
    
    def test_generate_recovery_codes_format(self):
        """Códigos tienen formato XXXX-XXXX"""
        codes = totp.generate_recovery_codes(n=5)
        
        for code in codes:
            parts = code.split("-")
            assert len(parts) == 2
            assert len(parts[0]) == 4
            assert len(parts[1]) == 4
            assert all(c.isalnum() for c in parts[0] + parts[1])
    
    def test_generate_recovery_codes_uppercase(self):
        """Códigos están en mayúsculas"""
        codes = totp.generate_recovery_codes(n=5)
        
        for code in codes:
            assert code == code.upper()
    
    def test_generate_recovery_codes_unique(self):
        """Todos los códigos son únicos"""
        codes = totp.generate_recovery_codes(n=20)
        assert len(set(codes)) == len(codes)


class TestHashCode:
    """Tests para hash de códigos de recuperación"""
    
    def test_hash_code_deterministic(self):
        """Mismo código produce mismo hash"""
        code = "ABCD-1234"
        hash1 = totp.hash_code(code)
        hash2 = totp.hash_code(code)
        
        assert hash1 == hash2
        assert len(hash1) == 64  # SHA256 hex
    
    def test_hash_code_case_insensitive(self):
        """Hash ignora mayúsculas/minúsculas"""
        code_lower = "abcd-1234"
        code_upper = "ABCD-1234"
        
        assert totp.hash_code(code_lower) == totp.hash_code(code_upper)
    
    def test_hash_code_strips_whitespace(self):
        """Hash ignora espacios en blanco"""
        code1 = "ABCD-1234"
        code2 = " ABCD-1234 "
        
        assert totp.hash_code(code1) == totp.hash_code(code2)
    
    def test_hash_code_different_codes_different_hash(self):
        """Códigos diferentes producen hashes diferentes"""
        hash1 = totp.hash_code("ABCD-1234")
        hash2 = totp.hash_code("EFGH-5678")
        
        assert hash1 != hash2
