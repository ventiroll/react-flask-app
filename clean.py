def clean_tool_steps(text): 

    steps = {}
    titles = [1]
    lines =  text.split("Step")
    subtext = []

    out = []

    for line in lines:
        line = line.strip()
        if line:
            clean_line = line.split("\n")
            if "1: Clean After Each Use" in clean_line[0]:
                step_title = clean_line[0][:-2]
                titles.append(step_title)
                ind_step = []
                for seg in clean_line[1:-1]:
                    if seg:
                        clean_subtext = []
                        clean_subtext.append(seg[2:].strip()+'\n')
                        ind_step.append(clean_subtext)
                subtext.append(ind_step)
            else: 
                step_title = clean_line[0][:-2]
                titles.append(step_title)
                ind_step = []
                for seg in clean_line[1:-1]:
                    if seg:
                        clean_subtext = []
                        clean_subtext.append(seg+'\n')
                        ind_step.append(clean_subtext)
                subtext.append(ind_step)
    
                    
    for i in range(len(titles)):
        steps["Step " + titles[i]] = subtext[i]
    
                
    return 

example = "Step 1: Clean After Each Use**\n\n*   **Immediately after cooking (while still warm, but not scalding hot):** Scrape out any food debris. You can use a spatula, chainmail scrubber, or nylon brush.\n*   **Rinse:** Rinse the pan with hot water.  Avoid using harsh soaps unless absolutely necessary (like after cooking fish). If you do use soap, use a very small amount of mild dish soap.\n*   **Dry:** Thoroughly dry the pan with a clean towel.\n\n**Step 2: Re-Season (if needed) **\n\n*   **Assess:** If your pan looks dull, feels sticky, or has food sticking, it's time to re-season.\n*   **Apply Oil:** Place the dry pan on the burner on low heat to make sure it\u2019s completely dry. Apply a VERY thin layer of high smoke point oil (like canola, vegetable, or avocado oil) to the entire pan, inside and out.  Use a clean cloth or paper towel to rub it in thoroughly, ensuring almost all of the oil is wiped off. You want just a whisper of oil.\n*   **Heat:** Place the pan upside down in a preheated oven at 450-500\u00b0F (232-260\u00b0C) for one hour. Place foil on the rack below to catch any drips. Let the pan cool completely in the oven.\n\n**Step 3: Preventative Maintenance**\n\n*   **Regular Use:**  The more you use your cast iron, the better the seasoning becomes.  Cooking with oil helps build up the protective layer.\n*   **Proper Storage:** Store your cast iron pan in a dry place.  If you live in a humid environment, consider placing a paper towel inside the pan to absorb any moisture.\n*   **Avoid Harsh Cleaners and Prolonged Soaking:**  Don't put your cast iron in the dishwasher or let it soak in water for extended periods.\n\nThese 3 steps will help keep your cast iron pan in great condition for years to come.\n"
print(clean_tool_steps(example))