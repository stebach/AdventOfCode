package li.ste.adventofcode.year2021.day16;

public class Message {
    private final MessagePackage messagePackage;
    private int index;

    public Message(String s) {
        short[] binData = stringToBin(s);

        index = 0;

        messagePackage = new MessagePackage(binData, this);

    }

    public static short[] stringToBin(String s) {
        short[] binData = new short[s.length() * 4];
        for (int i=0; i<s.length(); i++) {
            int nr = Integer.parseInt(s.substring(i,i+1), 16);
            for (int j=0; j<4; j++) {
                binData[i*4 + j] = (short)((nr & (int)Math.pow(2,3d-j)) > 0 ? 1: 0);
            }
        }
        return binData;
    }

    public int getIndex() {
        return index;
    }

    public void incrementIndex(int len) {
        index += len;
    }

    public int getPackageVersionSum() {
        return messagePackage.getPackageVersionSum();
    }

    public long getPackageSum() {
        return messagePackage.getPackageSum();
    }
}
