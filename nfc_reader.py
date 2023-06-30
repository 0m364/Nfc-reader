import os
import nfc

def write_nfc_data_to_file(data):
    try:
        with open("nfc-data.txt", "a") as file:
            file.write(data)
        print("NFC data saved to nfc-data.txt")
    except Exception as e:
        print(f"An error occurred when writing to the file: {str(e)}")

def connected(tag):
    # Read data from NFC tag
    data = str(tag.dump())
    # Write data to file
    write_nfc_data_to_file(data)

def read_nfc_tags():
    # Initialize NFC context
    nfc_context = nfc.init()
    if nfc_context is None:
        print("Failed to initialize NFC context")
        os._exit(1)

    # Open NFC device
    nfc_device = nfc.open(nfc_context, None)
    if nfc_device is None:
        print("Failed to open NFC device")
        nfc.exit(nfc_context)
        os._exit(1)

    # Initialize NFC reader
    nfc.initiator_init(nfc_device)

    # Wait for NFC tag
    print("Place an NFC tag near the reader...")
    try:
        while True:
            # Attempt to connect to tag
            tag = nfc.initiator_select_dep_target(nfc_device)
            if tag is not None:
                connected(tag)
    except KeyboardInterrupt:
        print("Stopped reading NFC tags.")

    # Cleanup and exit
    nfc.close(nfc_device)
    nfc.exit(nfc_context)

if __name__ == "__main__":
    read_nfc_tags()
