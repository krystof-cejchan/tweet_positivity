import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;


public class csv_fix {

    public static void main(String[] args) {
        String filePath = "./newCSV-without quotes copy.txt";
        String fileContent = "";

        try {
            fileContent = new String(Files.readAllBytes(Paths.get(filePath)), StandardCharsets.UTF_8);
        } catch (Exception e) {
            e.printStackTrace();
        }
        String regex = "\\+00:00,[\\s\\S]*?(POSITIVE|NEGATIVE|NEUTRAL)";
        String output = fileContent.replaceAll(regex, ",$1");
        
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter("d.txt"));
            writer.write(output);
            writer.close();


        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
