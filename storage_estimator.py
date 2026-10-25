def estimate_storage(file_count, avg_size_kb):
    return file_count * avg_size_kb * 1024


def main():
    file_count = int(input("Number of files: "))
    avg_size_kb = float(input("Average file size (KB): "))
    total_bytes = estimate_storage(file_count, avg_size_kb)
    print("Total storage:", total_bytes, "bytes")


if __name__ == "__main__":
    main()
