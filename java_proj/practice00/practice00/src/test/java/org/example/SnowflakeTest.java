package org.example;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class SnowflakeTest
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public SnowflakeTest(String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( SnowflakeTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
        Snowflake sf = new Snowflake(1);
        long id = sf.getID();
        long id2 = sf.getID();

        assertTrue(id2 > id);

        assertEquals((id2&(~(-(1L<<26))))-1,  id&(~(-(1L<<26))));
        assertEquals((id &(~(-(1L << 39)))) >> 34, 1);
    }
}
