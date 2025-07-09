import json

def xor_encrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data))

def export_to_op(data, filepath='translator.op', password='secret'):
    raw_json = json.dumps(data).encode('utf-8')
    encrypted = xor_encrypt(raw_json, password)
    with open(filepath, 'wb') as f:
        f.write(encrypted)
    print(f"Exported to {filepath} (encrypted)")

def import_from_op(filepath='translator.op', password='secret'):
    with open(filepath, 'rb') as f:
        encrypted = f.read()
    decrypted = xor_encrypt(encrypted, password)
    try:
        return json.loads(decrypted.decode('utf-8'))
    except json.JSONDecodeError:
        print("❌ Incorrect password or corrupted .op file")
        return {}