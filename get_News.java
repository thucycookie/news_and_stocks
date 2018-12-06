import java.io.*;
import java.net.*;
import java.util.Scanner;

public class get_News {

   public static String getHTML(String top_hd_or_everything, String country_code, String sources, String category, String keyword_hdl, String start, String end, String domains, String keyword_every,String json_file_name) throws Exception {
      String urlToRead = get_news_in_json.request(top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every);
      StringBuilder result = new StringBuilder();
      URL url = new URL(urlToRead);
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setRequestMethod("GET");
      BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      String line;
      while ((line = rd.readLine()) != null) {
         result.append(line);
      }
      rd.close();
      String fileName = json_file_name;
      BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
      writer.write(result.toString());
      writer.close();
      return fileName;
   }

   public static void main(String[] args) throws Exception
   {
     Scanner kb = new Scanner(System.in);
        String top_hd_or_everything = kb.nextLine();
        String country_code = kb.nextLine();
        String sources = kb.nextLine();
        String category = kb.nextLine();
        String keyword_hdl = kb.nextLine();
        String start = kb.nextLine();
        String end = kb.nextLine();
        String domains = kb.nextLine();
        String keyword_every = kb.nextLine();
        String json_file_name = kb.nextLine();
        System.out.println(getHTML(top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every,json_file_name));
   }
}
