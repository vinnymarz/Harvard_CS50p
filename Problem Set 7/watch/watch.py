import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"[^>]*>'
    if matches := re.search(pattern, s, re.IGNORECASE):
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()

#<iframe: This part of the pattern matches the literal string <iframe.
#[^>]*: The [^>] part is a character set that matches any character except the > character.
#The * quantifier means zero or more occurrences of the preceding character set.
#So, [^>]* matches any sequence of characters that are not >, allowing you to skip over any attributes before the src attribute.

#src="https?://(?:www\.)?youtube\.com/embed/: This part of the pattern matches the src attribute value of the iframe tag. See below:
#src=": This matches the literal string src=".
#https?: This matches either http or https. The ? quantifier makes the s optional.
#://: This matches the literal ://.
#(?:www\.)?: This is a non-capturing group (?:...) that matches an optional www.. The ? quantifier makes the group optional.
#youtube\.com/embed/: This matches the literal string youtube.com/embed/.

#([^"]+): This is a capturing group that matches any sequence of characters that are not double quotes (").
#The + quantifier means one or more occurrences. This group captures the video ID from the URL.
