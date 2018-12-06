import java.util.Scanner;

public class get_news_in_json 
{
	public static String top_hdl(String url,String country_code,String sources,String category_,String keyword_hdl)
	{
		String new_url = "";
		int count = 0;
		String country = country_code;
		if(country.equals("None"))
		{
		  country = "";
		}else
		{
		  country = "country=" + country; 
		  count += 1; 
		}

		String source = sources;
                if(source.equals("None"))
                {
                  source = "";
                }else
                {
                  source = "source=" + source;
                  count += 1;
                }
		
		if(count > 1)
		{
		  source = "&" + source;
		}

                String category = category_;
                if(category.equals("None"))
                {
                  category = "";
                }else
                {
                  category = "category=" + category;
                  count += 1;
                }
        
                if(count > 1)
                {
                  category = "&" + category;
                }

                String q = keyword_hdl;
                if(q.equals("None"))
                {
                  q = "";
                }else
                {
		  q = q.replaceAll("^\"|\"$", "");
		  q = q.replaceAll("\\s","%20");
                  q = "q=" + q;
		  System.out.println(q);
		  count += 1;
                }

                if(count > 1)
                {
                  q = "&" + q;
                }
		new_url += url + country + source + category + q;
		return new_url;	
	}
	
	public static String everything(String url,String start_,String end_, String domains_,String keyword_every)
	{
		String new_url = "";
                int count = 0;
                String start = start_;
                if(start.equals("None"))
                {
                  start = "";
                }else
                {
                  start = "from=" + start;
                  count += 1;
                }

                String end = end_;
                if(end.equals("None"))
                {
                  end = "";
                }else
                {
                  end = "to=" + end;
                  count += 1;
                }

                if(count > 1)
                {
                  end = "&" + end;
                }

                String domains = domains_;
                if(domains.equals("None"))
                {
                  domains = "";
                }else
                {
                  domains = "domains=" + domains;
                  count += 1;
                }

                if(count > 1)
                {
                  domains = "&" + domains;
                }

                String q = keyword_every;
                if(q.equals("None"))
                {
                  q = "";
                }else
                {
		  q = q.replaceAll("^\"|\"$", "");
                  q = q.replaceAll("\\s","%20");
                  q = "q=" + q;
                }

                if(count > 1)
                {
                  q = "&" + q;
                }
                new_url += url + start + end + domains + q;
                return new_url;

	}

	public static String request(String top_hd_or_everything, String country_code, String sources, String category, String keyword_hdl, String start, String end, String domains, String keyword_every)
	{
          String url = "";
	  String apiKey = "&apiKey=e44a626eab9342729e116d265a287ef0";
	  String hl_or_every = top_hd_or_everything;
	  
	  if(hl_or_every.equals("Top Headlines"))
	  {
		url = "https://newsapi.org/v2/top-headlines?";
		url = top_hdl(url,country_code,sources,category,keyword_hdl);
		url += "&pageSize=100";
		url += apiKey;

	  }else if (hl_or_every.equals("Everything"))
	  {
		url = "https://newsapi.org/v2/everything?";
		url = everything(url,start,end,domains,keyword_every);
		url += "&pageSize=100";
		url += apiKey;
	  }else
	  {
		System.out.println("You will get an error!!!!");
	  }

	  return url;
	}
	public static void main(String[] args)
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
        System.out.println(request(top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every));
	}



}
