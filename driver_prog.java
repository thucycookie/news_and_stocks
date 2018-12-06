import java.util.Scanner;

public class driver_prog
{
	public static String driver_prog(String top_hd_or_everything, String country_code, String sources, String category, String keyword_hdl, String start, String end, String domains, String keyword_every, String json_file_name) throws Exception
	{
	String json_file = get_News.getHTML(top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every,json_file_name);
	String csv_file = JSONREADER.decode(json_file);
	return csv_file;
	}
	public static void main(String[] args) throws Exception
	{
	// Scanner kb = new Scanner(System.in);
	String top_hd_or_everything = args[0];
	String country_code = args[1];
	String sources = args[2];
	String category = args[3];
	String keyword_hdl = args[4];
	String start = args[5];
	String end = args[6];
	String domains = args[7];
	String keyword_every = args[8];
	String json_file_name = args[9];
	System.out.println(driver_prog(top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every,json_file_name));
	}
}
