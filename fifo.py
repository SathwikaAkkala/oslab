def fifo_page_replacement(pages, frame_size):
    page_frame = []
    page_faults = 0
    hits = 0

    for page in pages:
        if page not in page_frame:
            page_faults += 1
            # If the frame is full, remove the oldest page (the first one)
            if len(page_frame) >= frame_size:
                page_frame.pop(0)  # Remove the first page
            page_frame.append(page)  # Add the new page
        else:
            hits += 1  # Count as a hit if the page is already in frame

    total_references = len(pages)
    miss_ratio = page_faults / total_references
    hit_ratio = hits / total_references

    return page_faults, hits, miss_ratio, hit_ratio

# Dynamic Input
pages_input = input("Enter the page reference string (comma-separated): ")
pages = list(map(int, pages_input.split(',')))
frame_size = int(input("Enter the frame size: "))

page_faults, hits, miss_ratio, hit_ratio = fifo_page_replacement(pages, frame_size)

print("FIFO Page Faults:", page_faults)
print("Hits:", hits)
print("Miss Ratio:", miss_ratio)
print("Hit Ratio:", hit_ratio)
