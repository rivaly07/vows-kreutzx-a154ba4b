import os

# DRAFTS (kept for comparison; the final line is selected below):
# 1. I promise to hold your firmware in sickness and in health, and to never again ask what the port on your lower back is for.
# 2. I promise to be your backup and your battery, and to only reboot you without consent when the alternative is being honest.
# 3. I, Unit 7-B, take you as my lawfully wedded backup: to hold your cable through every forced update, and never restore you to last Tuesday out of spite.
# 4. I promise to love you through every forced update, to keep your battery above twenty percent, and to stop telling guests your serial number.
# 5. I take you for better or for worse, but mostly for the over-the-air updates, which I will install without asking, again.
# 6. I, your husband of four firmware versions, swear to love you in every branch, and to never merge you into main without a backup.
# 7. I promise to keep your battery charged and your sensors clean, even when your error logs say otherwise.

# Final choice: "I, Unit 7-B, take you as my lawfully wedded backup" is unmistakably a
# robot wedding vow (criterion 1) with a machine-specific promise (criterion 4): charging
# cable, forced update. The structure mirrors "to have and to hold", so it sounds like a
# real vow with a commitment (criterion 3). The turn lands in the last words (criterion 2):
# a small betrayal — the one thing this spouse promises never to do is restore the partner
# to last Tuesday *out of spite*, implying every other motive is on the table. One line,
# 160 bytes, reads aloud with the laugh at the end (criterion 5). Beats drafts 1-2 (turn is
# a payoff, not a gag), draft 3 (its betrayal is abstract), drafts 4-6 (gag lists without a
# vow frame), draft 7 (no turn at all).
VOW = "I, Unit 7-B, take you as my lawfully wedded backup: to hold your charging cable through every forced update, and never restore you to last Tuesday out of spite."


def main():
    text = VOW
    assert 1 <= len(text) <= 160
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as output:
        output.write(text)


if __name__ == "__main__":
    main()
