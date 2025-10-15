# prognum.py

def fibonacci(n):
    """
    再帰的にフィボナッチ数列の n 番目の値を求める関数
    
    ルール：
    1番目の値 → 1
    2番目の値 → 1
    3番目以降 → 直前2つの値の和
    """
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        # 再帰呼び出し：自分自身を使って計算
        return fibonacci(n - 1) + fibonacci(n - 2)