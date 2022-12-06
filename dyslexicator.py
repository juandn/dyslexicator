import sys, random

def dyslexicate_word(word, opts):
    size = len(word)
    if size == 2 and '-f2' in opts:
        return word[::-1]
    if size == 3 and '-f3' in opts:
        return word[0]+word[1:][::-1]
    
    inside_orig = word[1:len(word)-1]
    if size == 4 and '-f4' in opts:
        return word.replace(inside_orig,inside_orig[::-1])
    
    l = list(inside_orig)
    random.shuffle(l)
    inside_dyslexed = ''.join(l)
    return word.replace(inside_orig,inside_dyslexed )

def show_usage():
    print(f"Usage: {sys.argv[0]} FILE ... (-f2 | -f3 | -f4 )")
    print(f"Usage: {sys.argv[0]} -h")
    print(f"\t-h|--help\tShow this help.")
    print(f"\t-f2\t\tForce swaping two letters words.")
    print(f"\t-f3\t\tForce swaping las two letters in three letters words.")
    print(f"\t-f4\t\tForce swaping the two letters inside four letters words.")



if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    
    if "-h" in opts or '--help' in opts or len(args) == 0: 
        show_usage()
    
    for file in args:
        print("Dyslexing" + ' ' + file + "...")
        with open(file,'r', encoding='utf-8') as i_file:
            with open ('dyslexed_'+file, 'w', encoding='utf-8') as o_file:
                # reading each line	
                for line in i_file:        
                    # reading each word		
                    for word in line.split():
                        o_file.write(dyslexicate_word(word,opts)+' ')
                    o_file.write('\n')

