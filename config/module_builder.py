import hashlib
import sys

def modbuild(file):
    # Check if hash exists, if so - remove
    with open(file, "r") as f:
        lines = f.readlines()
        f.close()
    with open(file, "w") as f:
        for line in lines:
            if "SHA256" not in line:
                print(line)
                f.write(line)
        f.close()

    with open(file, "rb") as f:
       bytes = f.read()  # read entire file as bytes
       readable_hash = hashlib.sha256(bytes).hexdigest();
       f.close()
    with open(file, "a") as f:
        f.write("SHA256 {}".format(readable_hash))



if __name__ == "__main__":
    modbuild(sys.argv[1])