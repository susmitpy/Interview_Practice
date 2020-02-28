import logging
logging.basicConfig(level=logging.ERROR)

def log(prev,hfc,hf,cf):
    logging.info(f"prev: {prev}")
    logging.info(f"hfc: {hfc}")
    logging.info(f"hf: {hf}")
    logging.info(f"cf: {cf}")

    
def highest_freq_info(s : str):
    prev = None
    highest_freq_char = None
    highest_freq = 0
    curr_freq = 0
    for c in s:
        if prev is None:
            prev = c
            highest_freq_char = c
            highest_freq = 1
            curr_freq=1
            log(prev,highest_freq_char,highest_freq,curr_freq)
        else:
            if c == prev:
                curr_freq += 1
            else:
                log(prev,highest_freq_char,highest_freq,curr_freq)
                if curr_freq > highest_freq:
                    highest_freq = curr_freq
                    highest_freq_char = prev
                prev = c
                curr_freq = 1
    return (highest_freq_char, highest_freq)


assert highest_freq_info("AABCDDBBBEA")==("B",3), "Incorrect"
assert highest_freq_info("AAABBCCDDE")==("A",3), "Incorrect"

print("All OK")
