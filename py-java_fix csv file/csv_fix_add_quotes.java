import java.io.*;

public class csv_fix_add_quotes {
    public static void main(String[] args) {
        String inputFileName = "./tweets_modified_cut_text.txt";
        String outputFileName = "tweets_modified_cut_text w q.txt";

        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputFileName));
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFileName));

            String line = null;
            while ((line = reader.readLine()) != null) {
                // Insert a double quote (") at the beginning and at the twentieth column of
                // each line
                if (line.length() < 19)
                    continue;
                String modifiedLine = "\"" + line.substring(0, 19) + "\"" + line.substring(19);
                writer.write(modifiedLine);
                writer.newLine();
            }

            reader.close();
            writer.close();

            System.out.println("File modified successfully.");
        } catch (IOException e) {
            System.out.println("An error occurred while modifying the file.");
            e.printStackTrace();
        }
    }
}