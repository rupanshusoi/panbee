#!/usr/bin/env python3

def analyze_wordlist():
    pangram_sets = {}
    
    with open('3of6game.txt', 'r') as f:
        words = [line.strip().replace('$', '').lower() for line in f if len(line.strip().replace('$', '')) >= 7]
    
    for word in words:
        unique_letters = set(word)
        if len(unique_letters) == 7:
            key = ''.join(sorted(unique_letters))
            if key not in pangram_sets:
                pangram_sets[key] = {
                    'letters': list(unique_letters),
                    'pangrams': []
                }
            pangram_sets[key]['pangrams'].append(word)
    
    valid_puzzles = [(letters, data) for letters, data in pangram_sets.items() 
                     if len(data['pangrams']) >= 1]
    
    valid_puzzles.sort(key=lambda x: len(x[1]['pangrams']), reverse=True)
    
    print(f"Total unique letter sets with pangrams: {len(valid_puzzles)}")
    print("\nTop 20 letter sets with most pangrams:")
    print("-" * 60)
    
    for i, (letters, data) in enumerate(valid_puzzles[:20], 1):
        print(f"{i}. Letters: {', '.join(sorted(data['letters']))}")
        print(f"   Pangrams ({len(data['pangrams'])}): {', '.join(data['pangrams'][:5])}")
        if len(data['pangrams']) > 5:
            print(f"   ... and {len(data['pangrams']) - 5} more")
        print()
    
    print(f"\nLetter sets with only 1 pangram: {sum(1 for _, data in valid_puzzles if len(data['pangrams']) == 1)}")
    print(f"Letter sets with 2+ pangrams: {sum(1 for _, data in valid_puzzles if len(data['pangrams']) >= 2)}")
    print(f"Letter sets with 5+ pangrams: {sum(1 for _, data in valid_puzzles if len(data['pangrams']) >= 5)}")

if __name__ == "__main__":
    analyze_wordlist()
