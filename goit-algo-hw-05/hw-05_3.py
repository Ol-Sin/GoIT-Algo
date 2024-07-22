import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0
    
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - last.get(text[s + j], -1))
    
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    
    return -1

# Читання файлів
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Вимірювання часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)

def main():
    text1 = read_file('article1.txt')
    text2 = read_file('article2.txt')
    
    existing_substring = "структури даних"  # підрядок для пошуку наявний у файлах
    non_existing_substring = "notinthetext"
    
    algorithms = {
        'Boyer-Moore': boyer_moore,
        'KMP': kmp_search,
        'Rabin-Karp': rabin_karp
    }
    
    for name, algorithm in algorithms.items():
        print(f"Testing {name} algorithm")
        
        print("Article 1 - existing substring:")
        time_existing = measure_time(algorithm, text1, existing_substring)
        print(f"Time: {time_existing:.6f} seconds")
        
        print("Article 1 - non-existing substring:")
        time_non_existing = measure_time(algorithm, text1, non_existing_substring)
        print(f"Time: {time_non_existing:.6f} seconds")
        
        print("Article 2 - existing substring:")
        time_existing = measure_time(algorithm, text2, existing_substring)
        print(f"Time: {time_existing:.6f} seconds")
        
        print("Article 2 - non-existing substring:")
        time_non_existing = measure_time(algorithm, text2, non_existing_substring)
        print(f"Time: {time_non_existing:.6f} seconds")
        
        print("")

if __name__ == "__main__":
    main()
