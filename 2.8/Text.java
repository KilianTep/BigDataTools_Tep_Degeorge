package cs.bigdata.Tutorial2_8;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

public class Text {

    public static void main(String[] args) throws IOException {

        String txtFile = "/Users/Jean/Desktop/text.txt";
    
        Configuration conf = new Configuration();
        
        FileSystem fs = FileSystem.get(conf);
        InputStream in = new BufferedInputStream(new FileInputStream(txtFile));
 

        BufferedReader br = null;
        String line = "";
        String station_name = "";
        String fips_code = "";
		String altitude = "";
        
        try {

            br = new BufferedReader(new FileReader(txtFile));
            
            // skip lines
            for(int i=1;i<=22;i++)
    			{
    				br.readLine();
    			}	

            while ((line = br.readLine()) != null) {
            	  
            	    		station_name = line.substring(13,42);
            	    		fips_code = line.substring(43,45);
            	    		altitude = line.substring(74,81);
            	    		
            	    		System.out.println(station_name + " " + fips_code + " " + altitude);
            	    
            	    
            }

            	    

            } catch (FileNotFoundException exc) {
            exc.printStackTrace();
            } catch (IOException exc) {
            exc.printStackTrace();
            } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException exc) {
                    exc.printStackTrace();
                }
                
            fs.close();
    		    in.close();
            }
        }

    }

}