package org.example;

public class LoadBanlancer {
    private IDGenerator[] genMap;
    private int genPartitionNum;
    public LoadBanlancer(String generatorName) {
        switch (generatorName) {
            case "Snowflake":
                this.genPartitionNum = Snowflake.getPartitionNum();
                this.genMap = new Snowflake[this.genPartitionNum];
                for (int i = 0; i < this.genPartitionNum; ++i) {
                    this.genMap[i] = new Snowflake(i);
                }
                break;
            default:
                throw new UnsupportedOperationException(generatorName + " not supported yet");
        }
    }

    public long getID(String identifier) {
        int id = identifier.hashCode()%this.genPartitionNum;
        if (id < 0) {
            id = -id;
        }
        return this.genMap[id].getID();
    }
}
