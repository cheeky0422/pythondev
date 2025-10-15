# prognum.py

def fibonacci(n: int) -> int:
    """n番目のフィボナッチ数を返す（1始まり）"""
    if n == 1 or n == 2:   # 1番目と2番目は1
        return 1
    else:                  # 3番目以降は直前2つの和
        return fibonacci(n - 1) + fibonacci(n - 2)
    