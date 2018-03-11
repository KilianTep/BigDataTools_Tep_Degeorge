package cs.bigdata.Tutorial2_7;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

public class Tree {

    public static void main(String[] args) throws IOException {

        String csvFile = "/Users/Jean/Downloads/arbres.csv";
        
        Configuration conf = new Configuration();
        
        FileSystem fs = FileSystem.get(conf);
        InputStream in = new BufferedInputStream(new FileInputStream(csvFile));
        
        
        BufferedReader br = null;
        String line = "";
        String csvSplitBy = ";";

        try {

            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {

                String[] tree = line.split(csvSplitBy);

                System.out.println("Tree: year=" + tree[5] + ", height=" + tree[6]);

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