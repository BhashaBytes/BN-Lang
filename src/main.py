import subprocess

mapping = {
    "প্রিন্ট": "print", "dekhao": "print",
    "ইনপুট": "input", "inpuṭ": "input",
    "যদি": "if", "jodi": "if",
    "নতুবা": "elif", "notuba": "elif",
    "অন্যথায়": "else", "onyothay": "else",
    "জন্য": "for", "jonno": "for",
    "যখন": "while", "jokhon": "while",
    "ফাংশন": "def", "fankshan": "def",
    "শ্রেণী": "class", "shreni": "class",
    "ফিরিয়ে_দাও": "return", "phiriye_dao": "return",
    "ভাঙো": "break", "bhango": "break",
    "চালিয়ে_যাও": "continue", "chaliye_jao": "continue",
    "ইমপোর্ট": "import", "importo": "import",
    "থেকে": "from", "theke": "from",
    "হিসেবে": "as", "hisebe": "as",
    "সহ": "with", "shoho": "with",
    "চেষ্টা": "try", "cheshta": "try",
    "ব্যতিক্রম": "except", "byatikrom": "except",
    "অবশেষে": "finally", "oboshese": "finally",
    "সত্য": "True", "shotto": "True",
    "মিথ্যা": "False", "mithya": "False",
    "কিছুই_না": "None", "kichui_na": "None",
    "অথবা": "or", "othoba": "or",
}

def translate(code: str) -> str:
    for bn, eng in mapping.items():
        code = code.replace(bn, eng)
    return code

def run_blang_file(filename="test.bl"):
    with open(filename, "r", encoding="utf-8") as f:
        bengali_code = f.read()
    python_code = translate(bengali_code)
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)
    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_blang_file()
