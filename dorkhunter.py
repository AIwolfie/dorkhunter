#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import random
import time

try:
    from googlesearch import search as google_search
except ImportError:
    print("\033[91m[!] Missing googlesearch-python → pip install googlesearch-python\033[0m")
    sys.exit(1)

# try:
#     from duckduckgo_search import ddg
# except ImportError:
#     print("\033[91m[!] Missing duckduckgo-search → pip install duckduckgo-search\033[0m")
#     sys.exit(1)

# ----------------- Colors --------------------
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

# ----------------- Banner --------------------
def banner():
    print(f"""{Color.CYAN}
{Color.BOLD}
 ╔════════════════════════════════════════════╗
 ║         🔎 DorkHunter - CLI Tool           ║
 ║    Search with Google + DuckDuckGo Power   ║
 ╚════════════════════════════════════════════╝
{Color.RESET}""")

# ----------------- Save Output --------------------
def save_results(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for res in results:
            file.write(res + "\n")

# ----------------- Search --------------------
def search_google(query, limit):
    print(f"\n{Color.YELLOW}[GOOGLE]{Color.RESET} Searching...")
    results = []
    try:
        for link in google_search(query, stop=limit, pause=random.uniform(1.5, 2.5)):
            results.append(link)
    except Exception as e:
        print(f"{Color.RED}[!] Google Error: {e}{Color.RESET}")
    return results

def search_duckduckgo(query, limit):
    print(f"\n{Color.YELLOW}[DUCKDUCKGO]{Color.RESET} Searching...")
    results = []
    try:
        data = ddg(query, max_results=limit)
        if data:
            for item in data:
                results.append(item['href'])
    except Exception as e:
        print(f"{Color.RED}[!] DuckDuckGo Error: {e}{Color.RESET}")
    return results

# ----------------- Main Logic --------------------
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="Search dorks using Google & DuckDuckGo",
        usage="python3 dorkHunter.py -q '<dork>' [-l 20] [-o output.txt]"
    )
    parser.add_argument("-q", "--query", help="Dork search query", required=True)
    parser.add_argument("-l", "--limit", help="Number of results per engine (default: 10)", type=int, default=10)
    parser.add_argument("-o", "--output", help="Save results to a file")

    args = parser.parse_args()

    query = args.query.strip()
    limit = args.limit
    output_file = args.output

    all_results = []

    # Google
    google_results = search_google(query, limit)
    if google_results:
        for idx, url in enumerate(google_results, 1):
            print(f"{Color.GREEN}[{idx}] {Color.RESET}{url}")
            all_results.append(url)
    else:
        print(f"{Color.RED}[!] No results from Google.{Color.RESET}")

    # DuckDuckGo
    time.sleep(1.5)
    ddg_results = search_duckduckgo(query, limit)
    offset = len(all_results)
    if ddg_results:
        for idx, url in enumerate(ddg_results, offset + 1):
            print(f"{Color.CYAN}[{idx}] {Color.RESET}{url}")
            all_results.append(url)
    else:
        print(f"{Color.RED}[!] No results from DuckDuckGo.{Color.RESET}")

    # Save results if requested
    if output_file:
        output_file = output_file if output_file.endswith('.txt') else output_file + ".txt"
        save_results(all_results, output_file)
        print(f"{Color.GREEN}\n[✓] Results saved to: {output_file}{Color.RESET}")

    print(f"\n{Color.BOLD}{Color.GREEN}[✔] Total unique results: {len(set(all_results))}{Color.RESET}")

# ----------------- Entry --------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}[X] Interrupted by user. Exiting...{Color.RESET}")
