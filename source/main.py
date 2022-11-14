from get_urls import get_urls


def main():
    urls = get_urls("US Dollar", "20")
    print(urls)
    print(len(urls))
    return


if __name__ == "__main__":
    main()
