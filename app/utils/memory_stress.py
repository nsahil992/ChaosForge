memory_chunks = []

def leak_memory(size_mb=50):

    print("[WARNING] Memory leak simulation started")

    chunk = "A" * (1024 * 1024 * size_mb)

    memory_chunks.append(chunk)

    print(f"[INFO] Allocated {size_mb}MB memory")

    return len(memory_chunks)