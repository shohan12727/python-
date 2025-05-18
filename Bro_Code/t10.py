import time

# List of tuples: (delay in seconds from start, lyric line)
lyrics = [
    (0,  "Pretty little baby (Yah, yah)"),
    (2,  "Pretty little baby (Yah, yah)"),
    
    # Verse 1
    (5,  "[Verse 1]"),
    (6,  "Pretty little baby, you say that maybe"),
    (9,  "You'll be thinkin' of me, and try to love me"),
    (12, "Pretty little baby, I'm hoping that you do"),
    (15, "Ooh-ooh-ooh-ooh-ooh-ooh"),

    # Verse 2
    (18, "[Verse 2]"),
    (19, "You can ask the flowers, I sit for hours"),
    (22, "Tellin' all the bluebirds, the bill and coo birds"),
    (25, "Pretty little baby, I'm so in love with you"),
    (28, "Ooh-ooh-ooh"),

    # Chorus
    (30, "[Chorus]"),
    (31, "Now is just the time, while both of us are young"),
    (34, "Puppy love must have its day"),
    (37, "Don't you know it's much more fun to love"),
    (40, "While the heart is young and gay?"),

    # Verse 3
    (43, "[Verse 3]"),
    (44, "Meet me at the car hop or at the pop shop"),
    (47, "Meet me in the moonlight or in the daylight"),
    (50, "Pretty little baby, I'm so in love with you"),

    # Chorus again
    (53, "[Chorus]"),
    (54, "Now is just the time, while both of us are young"),
    (57, "Puppy love must have its day"),
    (60, "Don't you know it's much more fun to love"),
    (63, "While the heart is young and gay?"),

    # Verse 4
    (66, "[Verse 4]"),
    (67, "Meet me at the car hop or at the pop shop"),
    (70, "Meet me in the moonlight or in the daylight"),
    (73, "Pretty little baby, I'm so in love with you"),
    (76, "Ooh-ooh-ooh"),

    # Outro
    (79, "[Outro]"),
    (80, "Pretty little baby"),
    (82, "I said pretty little baby"),
    (84, "Oh, now, pretty little baby"),
]

# Store the starting time
start_time = time.time()

# Display each line at the scheduled time
for delay, line in lyrics:
    time_to_wait = delay - (time.time() - start_time)
    if time_to_wait > 0:
        time.sleep(time_to_wait)
    print(line)
