import os
import nfc

def write_nfc_data_to_file(data):
    with open("nfc-data.txt", "w") as file:
        file.write(data)
    print("NFC data saved to nfc-data.txt")

def connected(tag):
    # Read data from NFC tag
    data = str(tag.dump())
    # Write data to file
    write_nfc_data_to_file(data)

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
while True:
    # Attempt to connect to tag
    tag = nfc.initiator_select_dep_target(nfc_device)
    if tag is not None:
        connected(tag)
        break

# Cleanup and exit
nfc.close(nfc_device)
nfc.exit(nfc_context)
