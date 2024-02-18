pieces = list(map(int, input().split()))
chessBoard = [1, 1, 2, 2, 2, 8]
requirement = [req - found for req, found in zip(chessBoard, pieces)]
print(" ".join(map(str, requirement)))