def estimate_storage(file_count, avg_size_kb):
    return file_count * avg_size_kb * 1024


def main():
    file_count = int(input("Number of files: "))
    avg_size_kb = float(input("Average file size (KB): "))
    total_bytes = estimate_storage(file_count, avg_size_kb)
    print(f"Total storage: {total_bytes:,.0f} bytes")
    print(f"             = {total_bytes / 1024:,.2f} KB")
    print(f"             = {total_bytes / 1024 ** 2:,.2f} MB")
    print(f"             = {total_bytes / 1024 ** 3:,.2f} GB")


if __name__ == "__main__":
    main()
