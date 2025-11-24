import pyshorteners
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: shortify <link>")
        sys.exit()

    raw_link = sys.argv[1]
    link = raw_link.strip('"').strip("'")
    
    s = pyshorteners.Shortener(timeout=20)

    print(f"Shortening: {link} ...")

    try:
        short_url = s.isgd.short(link)
        print("-" * 30)
        print(f"Shortened URL: {short_url}")
        print("-" * 30)
    except Exception as e:
        print("Error shortening URL.")
        print("Tip: Use quotes for complex URLs.")
        print(f"Details: {e}")

if __name__ == "__main__":
    main()