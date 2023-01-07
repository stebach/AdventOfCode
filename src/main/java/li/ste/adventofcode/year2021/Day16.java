package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;

public class Day16 extends Day {
    public static void main(String[] args) {
        Day day = new Day16(new InputProvider());
        day.solvePuzzles();
    }

    public Day16(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Message message = new Message(getData().get(0));

        setSolution1(message.getPackageVersionSum());
        setSolution2(message.getPackageSum());
    }

    protected class Message {
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

    private class MessagePackage {
        private static final int TYPE_LITERAL = 4;
        private static final int SUMTYPE_ADDITION = 0;
        private static final int SUMTYPE_MULTIPLICATION = 1;
        private static final int SUMTYPE_MIN = 2;
        private static final int SUMTYPE_MAX = 3;
        private static final int SUMTYPE_RETURN = 4;
        private static final int SUMTYPE_GT = 5;
        private static final int SUMTYPE_LT = 6;
        private static final int SUMTYPE_EQ = 7;
        private final Message message;
        private final int version;
        private final int type;
        private final long intValue;
        private int packageSize;
        private final List<MessagePackage> packages = new ArrayList<>();

        public MessagePackage(short[] binData, Message message) {
            this.message = message;
            this.version = getIntData(binData, 3);
            this.type = getIntData(binData, 3);

            long longValueToSet = 0;

            if (type == TYPE_LITERAL) {
                StringBuilder sb = new StringBuilder();
                while (getIntData(binData, 1) == 1) {
                    sb.append(getStringData(binData, 4));
                }
                sb.append(getStringData(binData, 4));

                longValueToSet = Long.parseLong(sb.toString(), 2);

            } else {
                int lengthTypeId = getIntData(binData, 1);
                if (lengthTypeId == 0) {
                    // next 15
                    int bitLength = getIntData(binData, 15);

                    int targetIndex = message.getIndex() + bitLength;
                    while (message.getIndex() < targetIndex) {
                        packages.add(new MessagePackage(binData, message));
                    }


                } else {
                    // next 11
                    int packetLength = getIntData(binData, 11);

                    for (int i=0; i<packetLength; i++) {
                        packages.add(new MessagePackage(binData, message));
                    }

                }

            }

            intValue = longValueToSet;
        }

        private void increaseMessageIndex(int num) {
            message.incrementIndex(num);
            packageSize += num;
        }

        private String getStringData(short[] binData, int len) {
            StringBuilder sb = new StringBuilder();
            for (int i=0; i<len; i++) {
                sb.append(String.valueOf(binData[message.getIndex() + i]));
            }
            increaseMessageIndex(len);
            return sb.toString();
        }

        private int getIntData(short[] binData, int len) {
            return Integer.parseInt(getStringData(binData, len), 2);
        }

        public int getSize() {
            return packageSize;
        }

        public int getPackageVersionSum() {
            int retVal = version;
            for (MessagePackage aPackage : packages) {
                retVal += aPackage.getPackageVersionSum();
            }
            return retVal;
        }

        public long getPackageSum() {
            switch (type) {
                case MessagePackage.SUMTYPE_ADDITION:
                    return getPackageSumAddition();
                case MessagePackage.SUMTYPE_MULTIPLICATION:
                    return getPackageSumMultiplication();
                case MessagePackage.SUMTYPE_MIN:
                    return getPackageSumMinimum();
                case MessagePackage.SUMTYPE_MAX:
                    return getPackageSumMaximum();
                case MessagePackage.SUMTYPE_RETURN:
                    return intValue;
                case MessagePackage.SUMTYPE_GT:
                    if (packages.get(0).getPackageSum() > packages.get(1).getPackageSum()) {
                        return 1;
                    }
                    return 0;
                case MessagePackage.SUMTYPE_LT:
                    if (packages.get(0).getPackageSum() < packages.get(1).getPackageSum()) {
                        return 1;
                    }
                    return 0;
                case MessagePackage.SUMTYPE_EQ:
                    if (packages.get(0).getPackageSum() == packages.get(1).getPackageSum()) {
                        return 1;
                    }
                    return 0;
                default:
                    throw new AdventOfCodeException("UNKOWN VERSION : " + version);
            }
        }

        private long getPackageSumMaximum() {
            long max = Long.MIN_VALUE;
            for (MessagePackage aPackage : packages) {
                if (aPackage.getPackageSum() > max) {
                    max = aPackage.getPackageSum();
                }
            }
            return max;
        }

        private long getPackageSumMinimum() {
            long min = Long.MAX_VALUE;
            for (MessagePackage aPackage : packages) {
                if (aPackage.getPackageSum() < min) {
                    min = aPackage.getPackageSum();
                }
            }
            return min;
        }

        private long getPackageSumMultiplication() {
            long retValProd = 1;
            for (MessagePackage aPackage : packages) {
                retValProd *= aPackage.getPackageSum();
            }
            return retValProd;
        }

        private long getPackageSumAddition() {
            long retVal = 0;
            for (MessagePackage aPackage : packages) {
                retVal += aPackage.getPackageSum();
            }
            return retVal;
        }
    }
}
