import random
from collections import defaultdict
def match(a, b):
    """Count exact position matches between two equal-length strings."""
    return sum(c1 == c2 for c1, c2 in zip(a, b))
class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        candidates = words[:]
        while candidates:
            guess = self._pick_best_guess(candidates)
            matches = master.guess(guess)
            if matches == 6:
                return
            candidates = [
                w for w in candidates if match(w, guess) == matches
            ]
    def _pick_best_guess(self, candidates):
        best_word = None
        best_worst_case = float('inf')
        for w1 in candidates:
            buckets = defaultdict(int)
            for w2 in candidates:
                if w1 != w2:
                    buckets[match(w1, w2)] += 1
            worst_case = max(buckets.values()) if buckets else 0
            if worst_case < best_worst_case:
                best_worst_case = worst_case
                best_word = w1
        return best_word
class Master(object):
    def __init__(self, secret, words, allowed_guesses):
        self.secret = secret
        self.words = set(words)
        self.allowed_guesses = allowed_guesses
        self.guess_count = 0
        self.found = False
    def guess(self, word):
        if self.guess_count >= self.allowed_guesses:
            raise Exception(
                "Either you took too many guesses, or you did not find the secret word."
            )
        if word not in self.words:
            self.guess_count += 1
            return -1
        self.guess_count += 1
        matches = match(word, self.secret)
        if matches == 6:
            self.found = True
        return matches
    def check(self):
        if self.found and self.guess_count <= self.allowed_guesses:
            return "You guessed the secret word correctly."
        return "Either you took too many guesses, or you did not find the secret word."
if __name__ == "__main__":
    solution = Solution()
    secret1 = "acckzz"
    words1 = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    allowedGuesses1 = 10
    master1 = Master(secret1, words1, allowedGuesses1)
    solution.findSecretWord(words1, master1)
    print(master1.check()) 
    secret2 = "hamada"
    words2 = ["hamada", "khaled"]
    allowedGuesses2 = 10
    master2 = Master(secret2, words2, allowedGuesses2)
    solution.findSecretWord(words2, master2)
    print(master2.check())  
    secret3 = "aaaata"
    words3 = ["aaaaga", "aaaaka", "aaauaa", "aaaaoa", "aafaaa", "aaaaza",
              "aaaava", "agaaaa", "aaagaa", "aaaaqa", "aaaaca", "aaaaua",
              "apaaaa", "aawaaa", "aaaaba", "aaaqaa", "aayaaa", "aaaaja",
              "aaacaa", "aaayaa", "aaaeaa", "aavaaa", "aasaaa", "aaaapa",
              "aaaaxa", "aeaaaa", "aaxaaa", "akaaaa", "aaaoaa", "aazaaa",
              "anaaaa", "aaaala", "aaraaa", "aaaata", "aaaaia", "ajaaaa",
              "aaaaaa", "ahaaaa", "aaaraa", "aaaiaa", "aanaaa", "alaaaa",
              "aakaaa", "aiaaaa", "aajaaa", "aaakaa", "axaaaa", "aaqaaa",
              "aaamaa", "aapaaa", "aaafaa", "aaasaa", "aadaaa", "amaaaa",
              "aaaaea", "aabaaa", "aaaama", "asaaaa", "acaaaa", "aaiaaa",
              "avaaaa", "afaaaa", "aoaaaa", "aamaaa", "aaaasa", "aawaaa",
              "azaaaa", "aataaa"]
    allowedGuesses3 = 30
    master3 = Master(secret3, words3, allowedGuesses3)
    solution.findSecretWord(words3, master3)
    print(master3.check()) 
    import string
    success = 0
    trials = 50
    for _ in range(trials):
        pool = set()
        while len(pool) < 100:
            pool.add(''.join(random.choice(string.ascii_lowercase) for _ in range(6)))
        words4 = list(pool)
        secret4 = random.choice(words4)
        master4 = Master(secret4, words4, 10)
        solution.findSecretWord(words4, master4)
        if master4.check() == "You guessed the secret word correctly.":
            success += 1
    print("Stress test success rate: {}/{}".format(success, trials))
print(__name__)