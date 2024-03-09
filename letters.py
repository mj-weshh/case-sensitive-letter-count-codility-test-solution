#you are given a string letters made of N English letters.
#Count the number of different letters that appear in both uppercase and lowercase occurence of the given letter appear before any uppercase occurrence.
#For example, for letters = "aaAbcCABBc" the answer is 2. 
#The condition is met for letters 'a' and 'b', but not for 'c'.
#Write a finction:
#def solution(letters)
#that, given a string letters, returns the number of different letters fulfilling the condition above.
#Examples:
#1. Given letters = "aaAbcCABBc", the function should return 2, as explained above.
#2. Given letters = "xyzXYZabcABC", the function should return 6.
#3. Given letters = "ABCabcAefG", the function should return 0.
#Write an efficient algorithm for the following assumptions:
#    -N is an integer within the range [1..100,000];
#    -string letters is made only of letters(a-z and/or A-Z)


def solution(letters):
    seen_lowercase_letters = set()
    seen_uppercase_letters = set()
    count = 0

    for letter in letters:
        if letter.islower():
            seen_lowercase_letters.add(letter)

        elif letter.isupper():
            if letter not in seen_uppercase_letters and letter.lower() in seen_lowercase_letters:
                count += 1
                seen_uppercase_letters.add(letter)
            elif letter in seen_uppercase_letters:
                continue
            else:
                seen_uppercase_letters.add(letter)
    return count
            

#testing
print(solution("aaAbcCABBc"))  # Output: 3
print(solution("xyzXYZabcABC"))  # Output: 6
print(solution("ABCabcAefG"))  # Output: 0
