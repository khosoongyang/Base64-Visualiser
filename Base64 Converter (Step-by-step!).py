"""
Enhanced Base64 Encoder/Decoder with Detailed Step-by-Step Explanations
Demonstrates the complete encoding and decoding process for educational purposes
"""

# Base64 alphabet (RFC 4648)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PADDING_CHAR = "="

def print_header(title):
    """Print a formatted section header"""
    print(f"\n{'=' * 70}")
    print(f"{title.center(70)}")
    print('=' * 70)

def print_substep(text):
    """Print a substep with formatting"""
    print(f"\n→ {text}")

def encode_base64(plain_text):
    """
    Encode plain text to Base64 with detailed step-by-step explanation
    
    Args:
        plain_text (str): The text to encode
    
    Returns:
        str: Base64 encoded string
    """
    print_header("BASE64 ENCODING PROCESS")
    
    # STEP 1: Display input
    print_header("STEP 1: INPUT TEXT")
    print(f"Input: '{plain_text}'")
    print(f"Length: {len(plain_text)} characters")
    
    # STEP 2: Convert to binary
    print_header("STEP 2: CONVERT TO BINARY (8-bit)")
    print("Each character is converted to its ASCII value, then to 8-bit binary")
    print()
    
    binary_stream = ""
    for i, ch in enumerate(plain_text):
        ascii_val = ord(ch)
        binary_8bit = format(ascii_val, '08b')
        binary_stream += binary_8bit
        print(f"  [{i+1}] '{ch}' → ASCII {ascii_val:3d} → {binary_8bit}")
    
    print_substep(f"Complete binary stream ({len(binary_stream)} bits):")
    # Split into groups of 6 for Base64 grouping
    formatted_stream = ' '.join([binary_stream[i:i+6] for i in range(0, len(binary_stream), 6)])
    print(f"  {formatted_stream}")
    print(f"\n  (Grouped by 6 bits - each group becomes one Base64 character)")
    
    # STEP 3: Group into 6-bit chunks
    print_header("STEP 3: SPLIT INTO 6-BIT GROUPS")
    print("Base64 uses 6 bits per character (2^6 = 64 possible values)")
    print()
    
    encoded = ""
    chunks = []
    
    # Process complete 6-bit chunks
    for i in range(0, len(binary_stream), 6):
        chunk = binary_stream[i:i+6]
        
        # Pad incomplete chunk with zeros
        if len(chunk) < 6:
            original_chunk = chunk
            chunk = chunk.ljust(6, '0')
            chunks.append((chunk, True, original_chunk))
        else:
            chunks.append((chunk, False, ""))
    
    for i, (chunk, is_padded, original) in enumerate(chunks):
        decimal_val = int(chunk, 2)
        base64_char = ALPHABET[decimal_val]
        encoded += base64_char
        
        if is_padded:
            print(f"  [{i+1}] {original} → (padded) {chunk} → decimal {decimal_val:2d} → '{base64_char}' *")
        else:
            print(f"  [{i+1}] {chunk} → decimal {decimal_val:2d} → '{base64_char}'")
    
    print("\n  * Padded with zeros to complete 6-bit group")
    
    # STEP 4: Add padding
    print_header("STEP 4: ADD PADDING CHARACTERS")
    print("Padding ensures output length is multiple of 4")
    print()
    
    remainder = len(plain_text) % 3
    
    if remainder == 0:
        padding = ""
        print(f"  Input length: {len(plain_text)} (divisible by 3)")
        print("  No padding needed")
    elif remainder == 1:
        padding = "=="
        print(f"  Input length: {len(plain_text)} (remainder 1 when divided by 3)")
        print("  Add 2 padding characters: '=='")
    else:  # remainder == 2
        padding = "="
        print(f"  Input length: {len(plain_text)} (remainder 2 when divided by 3)")
        print("  Add 1 padding character: '='")
    
    encoded_final = encoded + padding
    
    # STEP 5: Final output
    print_header("STEP 5: FINAL BASE64 OUTPUT")
    print(f"Encoded text: {encoded_final}")
    print(f"Length: {len(encoded_final)} characters")
    
    # Summary
    print_header("ENCODING SUMMARY")
    print(f"  Original:  '{plain_text}' ({len(plain_text)} bytes)")
    print(f"  Encoded:   '{encoded_final}' ({len(encoded_final)} chars)")
    print(f"  Expansion: {len(encoded_final)/len(plain_text):.2f}x")
    
    return encoded_final


def decode_base64(encoded_text):
    """
    Decode Base64 text to plain text with detailed step-by-step explanation
    
    Args:
        encoded_text (str): The Base64 encoded text
    
    Returns:
        str: Decoded plain text
    """
    print_header("BASE64 DECODING PROCESS")
    
    # STEP 1: Display input
    print_header("STEP 1: INPUT BASE64 TEXT")
    print(f"Input: '{encoded_text}'")
    print(f"Length: {len(encoded_text)} characters")
    
    # STEP 2: Identify and remove padding
    print_header("STEP 2: IDENTIFY PADDING")
    
    padding_count = encoded_text.count(PADDING_CHAR)
    core_text = encoded_text.rstrip(PADDING_CHAR)
    
    print(f"Padding characters found: {padding_count}")
    print(f"Core Base64 text: '{core_text}'")
    print(f"Core length: {len(core_text)} characters")
    
    # STEP 3: Convert to binary
    print_header("STEP 3: CONVERT TO BINARY (6-bit)")
    print("Each Base64 character represents 6 bits")
    print()
    
    binary_stream = ""
    
    for i, ch in enumerate(core_text):
        index = ALPHABET.find(ch)
        if index == -1:
            print(f"ERROR: Invalid Base64 character '{ch}'")
            return None
        
        binary_6bit = format(index, '06b')
        binary_stream += binary_6bit
        print(f"  [{i+1}] '{ch}' → index {index:2d} → {binary_6bit}")
    
    print_substep(f"Complete binary stream ({len(binary_stream)} bits):")
    # Split into groups of 6 for Base64 grouping
    formatted_stream = ' '.join([binary_stream[i:i+6] for i in range(0, len(binary_stream), 6)])
    print(f"  {formatted_stream}")
    print(f"\n  (Grouped by 6 bits for decoding)")
    
    # STEP 4: Remove padding bits
    print_header("STEP 4: REMOVE PADDING BITS")
    
    if padding_count == 0:
        bits_to_remove = 0
        print("  No padding → no bits to remove")
    elif padding_count == 1:
        bits_to_remove = 2
        print("  1 padding char → remove 2 bits")
    else:  # padding_count == 2
        bits_to_remove = 4
        print("  2 padding chars → remove 4 bits")
    
    if bits_to_remove > 0:
        trimmed_binary = binary_stream[:-bits_to_remove]
        print(f"  Removed last {bits_to_remove} bits")
    else:
        trimmed_binary = binary_stream
    
    print(f"  Trimmed binary ({len(trimmed_binary)} bits): {trimmed_binary}")
    
    # STEP 5: Convert to ASCII
    print_header("STEP 5: CONVERT TO ASCII (8-bit)")
    print("Group bits into 8-bit chunks and convert to characters")
    print()
    
    decoded_text = ""
    
    for i in range(0, len(trimmed_binary), 8):
        octet = trimmed_binary[i:i+8]
        
        if len(octet) == 8:
            ascii_val = int(octet, 2)
            char = chr(ascii_val)
            decoded_text += char
            print(f"  [{i//8 + 1}] {octet} → ASCII {ascii_val:3d} → '{char}'")
    
    # STEP 6: Final output
    print_header("STEP 6: DECODED OUTPUT")
    print(f"Decoded text: '{decoded_text}'")
    print(f"Length: {len(decoded_text)} characters")
    
    # Summary
    print_header("DECODING SUMMARY")
    print(f"  Encoded:   '{encoded_text}' ({len(encoded_text)} chars)")
    print(f"  Decoded:   '{decoded_text}' ({len(decoded_text)} bytes)")
    
    return decoded_text


def main():
    """Main program loop"""
    print("\n" + "=" * 70)
    print("BASE64 ENCODER/DECODER WITH STEP-BY-STEP EXPLANATION".center(70))
    print("=" * 70)
    
    while True:
        print("\n" + "-" * 70)
        text = input("\nEnter text: ").strip()
        
        if not text:
            print("Error: Input cannot be empty")
            continue
        
        print("\nSelect mode:")
        print("  [1] Encode to Base64")
        print("  [2] Decode from Base64")
        print("  [3] Exit")
        
        mode = input("\nChoice: ").strip()
        
        if mode == "1":
            result = encode_base64(text)
            print(f"\n✓ Encoding complete!")
            
        elif mode == "2":
            result = decode_base64(text)
            if result is None:
                print("\n✗ Decoding failed due to invalid input")
            else:
                print(f"\n✓ Decoding complete!")
                
        elif mode == "3":
            print("\nExiting program. Good luck with your exam!")
            break
            
        else:
            print("\n✗ Invalid choice. Please select 1, 2, or 3.")
        
        # Ask if user wants to continue
        print("\n" + "-" * 70)
        continue_choice = input("Process another text? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("\nExiting program. Good luck with your exam!")
            break


if __name__ == "__main__":
    main()