def lru_page_replacement(pages, frame_size):
    page_frame = []
    page_faults = 0
    hits = 0

    for page in pages:
        if page in page_frame:
            hits += 1  # Page hit
            page_frame.remove(page)  # Remove the page to reinsert it at the end
            page_frame.append(page)   # Move it to the end to mark it as recently used
        else:
            page_faults += 1  # Page fault
            if len(page_frame) >= frame_size:
                page_frame.pop(0)  # Remove the oldest page
            page_frame.append(page)  # Add the new page

    total_references = len(pages)
    miss_ratio = page_faults / total_references
    hit_ratio = hits / total_references

    return page_faults, hit_ratio, miss_ratio

# Dynamic Input
pages_input = input("Enter the page reference string (comma-separated): ")
pages = list(map(int, pages_input.split(',')))
frame_size = int(input("Enter the frame size: "))

page_faults, hit_ratio, miss_ratio = lru_page_replacement(pages, frame_size)

print("LRU Page Faults:", page_faults)
print("Hit Ratio:", hit_ratio)
print("Miss Ratio:", miss_ratio)
