import java.io.*; 
import java.util.Iterator; 
import java.util.Map; 
  
import org.json.simple.JSONArray; 
import org.json.simple.JSONObject; 
import org.json.simple.parser.*; 
  
public class JSONREADER  
{ 
    public static String decode(String json_file) throws Exception  
    { 
	Object obj = new JSONParser().parse(new FileReader(json_file));        
	JSONObject jo = (JSONObject) obj; 
	String status = (String) jo.get("status"); 
        long totalResults = (long) jo.get("totalResults");  
 	Iterator<Map.Entry> itr1 = null; 
        JSONArray articles = (JSONArray) jo.get("articles"); 
	Iterator articles_itr = articles.iterator(); 
	String write_me = "";
	String key, value = null;
	String csv_file = json_file.substring(0,json_file.length()-3-1) + "csv";

	BufferedWriter writer = new BufferedWriter(new FileWriter(csv_file));

	while (articles_itr.hasNext())  
        { 
            itr1 = ((Map) articles_itr.next()).entrySet().iterator(); 
            while (itr1.hasNext()) { 
                Map.Entry pair = itr1.next(); 
                System.out.println(pair.getKey() + " : " + pair.getValue());
		
			write_me += "\"" + pair.getValue() + "\"@";
		 
            }
		writer.write(write_me.substring(0,write_me.length()-1)+"\n");
		write_me = ""; 
        }
	writer.close();
	return csv_file;
	}
	public static void main(String[] args) throws Exception
	{
		String json_file = args[0];
		System.out.println(decode(json_file));
	}
}
