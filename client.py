import os
import capnp
import io_capnp
import asyncio
import json

async def callService(stream):
    message_properties = io_capnp.Properties.new_message()
    message_credentails = io_capnp.Credentials.new_message()
    message_inputs = io_capnp.Inputs.new_message()

    message_properties.data = json.dumps("{}")

    credentials = {"a": "apple", "b": "ball"}
    # Create a list of Entry messages and add them to the Map
    entry_list = message_credentails.init('entries', len(credentials))
    for i, (key, value) in enumerate(credentials.items()):
        entry = entry_list[i]
        entry.key = key
        entry.value = value

    with open("testdata/single_pdf.pdf", "rb") as fr:
        message_inputs.pdf = fr.read()

    print("write prop")
    await message_properties.write_async(stream)
    print("write credentilas")
    await message_credentails.write_async(stream)
    print("write inputs")
    await message_inputs.write_async(stream)

    message_outputs = await io_capnp.Outputs.read_async(stream)
    print(type(message_outputs.ocrJson))
    print(type(message_outputs.rawText))

async def main(host):
    host, port = host.split(":")
    stream = await capnp.AsyncIoStream.create_connection(host=host, port=port)
    await callService(stream)

if __name__ == '__main__':
    asyncio.run(capnp.run(main('localhost:8091')))