@0x934efea7f017ffa1;

struct Credentials(Key, Value) {
    entries @0 :List(Entry);
    struct Entry {
        key @0 :Key;
        value @1 :Value;
    }
}

struct Properties {
    data @0 :Data;
}

struct Inputs {
    pdf @0 :Data;
}

struct Outputs {
    ocrJson @0 :Text;
    rawText @1 :Text;
}