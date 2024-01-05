import capnp
import io_capnp
import asyncio
import argparse
import json
from service import OCRTask

async def runner(stream):
    message_properties = await io_capnp.Properties.read_async(stream)
    message_credentails = await io_capnp.Credentials.read_async(stream)

    credentails = dict([(entry.key.as_text(), entry.value.as_text()) for entry in message_credentails.entries])
    properties = json.loads(message_properties.data)

    kclass = OCRTask(
        properties,
        credentails,
        logger=None
    )

    # Run the object
    message_inputs = await io_capnp.Inputs.read_async(stream)
    outputs = kclass.run(**message_inputs.to_dict())

    message_outputs = io_capnp.Outputs.new_message()
    message_outputs.from_dict(outputs)
    await message_outputs.write_async(stream)

def parse_args():
    parser = argparse.ArgumentParser(
        usage="""Runs the server bound to the given address/port ADDRESS. """
    )

    parser.add_argument("address", help="ADDRESS:PORT")

    return parser.parse_args()

async def main():
    host, port = parse_args().address.split(":")
    server = await capnp.AsyncIoStream.create_server(runner, host, port)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(capnp.run(main()))
