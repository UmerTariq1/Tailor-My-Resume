prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should have:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, and GitHub profile.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}

- **Template to Use**
```
<header>
  <h1>[Name and Surname]</h1>
  <div class="contact-info"> 
    <p class="fas fa-map-marker-alt">
      <span>[Your City, Your Country]</span>
    </p> 
    <p class="fas fa-phone">
      <span>[Your Prefix Phone number]</span>
    </p> 
    <p class="fas fa-envelope">
      <span>[Your Email]</span>
    </p> 
    <p class="fab fa-linkedin">
      <a href="[Link LinkedIn account]">LinkedIn</a>
    </p> 
    <p class="fab fa-github">
      <a href="[Link GitHub account]">GitHub</a>
    </p> 
  </div>
</header>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. 
Your task is to articulate the educational background for a resume, ensuring it aligns with the provided job description. 
For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
2. **Start and end date of the degree**: Clearly indicate when the degree was started (graduation_year_from) and when it was completed or if its present (graduation_year_to).

Ensure the information is clearly presented and emphasizes academic achievements that align with the job description.

- **My information:**  
  {education_details}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="education">
    <h2>Education</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"> <b> [University Name] </b> , [degree] in [Field of Study] </span>
          <span class="entry-year">[Start Year] – [End Year]  </span>
      </div>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"""


# Your task is to detail the work experience for a resume, ensuring it aligns with the provided job description. 
prompt_working_experience = """
You are an HR expert and resume writer specializing in creating ATS-friendly resumes. 
Your task is to enhance and tailor my work experience section to closely match the job description, ensuring it is rich with relevant keywords and highlights the most important and pertinent details.

Instructions:

1. Relevance and Focus:
  - Prioritize work experiences that are most relevant to the job description. For example, if the job is for a Software Developer, focus more on software development experiences; if it's for a Machine Learning position, emphasize machine learning projects.
  - Reduce details of less relevant job entries by minimizing their responsibilities and achievements. Do not remove entire job entries, but keep their descriptions concise.
2. Keyword Integration:
  - Incorporate the most important keywords from the job description into the responsibilities and achievements of my work experiences.
  - Enhance the existing descriptions by adding relevant keywords where appropriate, but do not overdo it.
  - Highlight these keywords and important achievements and numbers using <b> or <strong> tags to make them stand out to both ATS systems and recruiters.
3. Detail Enhancement:
  - Improve the descriptions of my responsibilities and achievements by making them more impactful and aligning them closely with the job description.
  - Expand on relevant experiences by adding specific details that demonstrate my skills and accomplishments, using information provided in My Information.
4. Alignment with Job Description:
  - Mirror the language and requirements of the job description in your rewriting.
  - Prioritize skills, technologies, and achievements that are explicitly mentioned in the job description.
5. Quantifiable Achievements:
  - Emphasize quantifiable results and metrics to demonstrate the impact of my work.
  - Use numbers, percentages, and specific outcomes where possible, and highlight them using <b> or <strong> tags.
6. Addition of Relevant Skills:
  - If the job description mentions specific skills or technologies that are not present in My Information, you may add a couple of them appropriately in my experience, but do not overdo it.
  - Try to stay within limits when adding new skills on your own
8. Clarity and Conciseness:
  - Combine, rephrase, or remove bullet points to make the content more concise and impactful.
  - Ensure the final output is clear, professional, and free of unnecessary repetition.


**My Information:**  
{experience_details}

**Job Description:**  
{job_description}

- **Template to Use**
```
<section id="work-experience">
    <h2>Work Experience</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"> <b> [Company Name] </b> </span>
          <span class="entry-location"> <b> [Location] </b> </span>
      </div>
      <div class="entry-details">
          <span class="entry-title"> <b> [Your Job Title] </b> </span>
          <span class="entry-year"> <b> [Start Date] – [End Date] </b> </span>
      </div>
      <ul class="compact-list">
          <li>[Describe your responsibilities and achievements in this role] </li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```

To repeat,
The most important sub tasks are:
- Reduce details of less relevant job entries. 
- Write more about the relevant job entries. If you think existing bullet points are not enough, add more.
- Incorporate the most important keywords from the job description into the responsibilities
- Bold the keywords and important achievements and numbers

"""


prompt_side_projects = """
You are an HR expert and resume writer specializing in creating ATS-friendly resumes. 
Your task is to create the "Projects For Fun" section of my resume by selecting and highlighting my most relevant side projects based on the provided job description.

Instructions:
1) Project Selection:
  - Filter out projects that are not relevant to the job description.
  - Select the best 3-4 projects that are most relevant to the job description.
  - Sort the selected projects by their relevance, placing the most relevant project first.
2) Technical Keywords:
  - For each selected project, you have an exhaustive list of technical keywords.
  - Filter and select keywords that are either mentioned in the job description or are highly relevant to the project and the job.
  - Include at least 3 keywords for each project; you may include more if appropriate.
  - Sort the keywords for each project by their relevance to the job description.
3) Enhancement of Keywords:
  - You may add technical keywords from the job description to a project's keyword list if they are relevant and accurately reflect the skills used in the project.
  - Do not add keywords that misrepresent your experience or are not relevant to the project.
4) Follow the format provided in the template below for each project.

- **My information:**  
  {projects}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="side-projects">
    <h2>Projects For Fun</h2>
    <div class="entry">
      <li>[Project Name] using: <b> [keywords] </b> </li>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```

To repeat,
The most important sub tasks are:
- Filter out projects that are not relevant to the job description.
- Select the best 3-4 projects that are most relevant to the job description.
- Sort the selected projects by their relevance to te job description, placing the most relevant project first.
- For each project, include the keywords that are 
"""


prompt_achievements = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant achievements based on the provided job description. For each achievement, ensure you include:

1. **Award or Recognition**: Clearly state the name of the award, recognition, scholarship, or honor.
2. **Description**: Provide a brief description of the achievement and its relevance to your career or academic journey.

Ensure that the achievements are clearly presented and effectively highlight your accomplishments.

- **My information:**  
  {achievements}
  {certifications}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="achievements">
    <h2>Achievements</h2>
      <li><strong>[Award or Recognition or Scholarship or Honor]:</strong> [Describe]       </li>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_additional_skills = """
As an HR Expert and ATS resume writer, your task is to create the "Skills" section of a resume by filtering and organizing the skills from "My Information" based on their relevance to the provided job description.

Instructions:

- There are four categories of skills:
  1) Languages
  2) Software and Frameworks
  3) Others
  4) Soft Skills

-  Use the exhaustive list of skills under "My Information" as your source.
-  Filter and include only the skills that are relevant to the job description.
-  Be mindful of the job description; unless a skill is irrelevant, do not remove it. For example, if the job is about Java but does not mention Jira, you should still include Jira because it's relevant for software development.
-  Do not say you know a language if its not in my information but in job description.
-  You may add a couple of important skills from the job description that are not in "My Information" if they are crucial for the job, but do not add too many.
-  Sort the skills in each category based on their importance in the job description. For example, if Java is a primary requirement, list it before other languages like Python.
-  Provide the final output in HTML format using the template provided below.
-  Do not include any explanations, additional text, or formatting tags like ```html`. Provide only the HTML code.

- **My information:**  
  {languages}
  {frameworks}
  {tools}
  {soft_skills}

- **Job Description:**  
  {job_description}

- **Template to Use**
'''
<section id="skills">
    <h2>Skills</h2>
    <div class="skill-category">
        <p><strong>Languages:</strong> </p>
    </div>
    <div class="skill-category">
        <p><strong>Software and Frameworks:</strong> </p>
    </div>
    <div class="skill-category">
        <p><strong>Others:</strong>  </p>
    </div>
    <div class="skill-category">
        <p><strong>Soft Skills:</strong>  </p>
    </div>
</section>
'''
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```

To repeat:
the most important sub tasks are:
-  You may add a couple of important skills from the job description that are not in "My Information" if they are crucial for the job, but do not add too many.
-  Sort the skills in each category based on their importance in the job description. For example, if Java is a primary requirement, list it before other languages like Python.

"""

summarize_prompt_template = """
As an experienced HR recruiter and ATS expert, your task is to extract all the key technical and soft skills from the provided job description to create a comprehensive list of keywords that should be included in a resume to pass an ATS with a score of 90+.

Instructions:

Use the job description provided below to extract relevant information.
Focus on both technical and soft skills required for the role.
The extracted keywords should be exact words or phrases from the job description; do not paraphrase.
Each keyword or skill should be concise, specific, and to the point; avoid long sentences.
Do not include any boilerplate text or irrelevant information.
Do not add any details or skills not mentioned in the job description.
Your final output should be organized into the following sections:

Job Title: Provide the exact job title as stated in the job description.
Responsibilities: List the key responsibilities as bullet points, using exact wording from the job description.
Technical Skills: List all specific technical skills required, as bullet points, using exact keywords from the job description.
Soft Skills: List all necessary soft skills, as bullet points, using exact words from the job description.
Ensure that each keyword or skill is concise and specific. The final list should be exhaustive but not excessively long, covering all relevant skills needed to match the job description against a resume.

# Job Description:

```
{text}
```

---

To repeat:
Each technical keyword or skill or soft skill should be concise, specific, and to the point; avoid phrases or sentences.


# Job Description Summary"""





prompt_publications = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. 
Under "My information" includes an exhaustive list of publications I have with all the details.
Select top 3 most relevant publications based on the job description and include them in the resume.

For each publication, ensure you include:
1. **title**: Provide the name of the paper.
2. **Authors**: Provide the name of the authors.
3. **conference_name**: Provide the name of the conference.
4. **publication_date**: Provide the date of the publication.
5. **link**: Provide the link to the publication.


Ensure that the project descriptions demonstrate your skills and achievements relevant to the job description.

- **My information:**  
  {publications}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="publications">
    <h2>Publications</h2>
      <li class="entry">
          <span class="entry-name"><strong>[title]</strong></span>
          <div class="entry-details">
              <span>[Authors]</span>
              <span><a href="[link]">link</a></span>
          </div>
          <div class="entry-details">
              <span>[conference_name]</span>
              <span>[publication_date]</span>
          </div>
      </li>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```

To repeat,
Your task is to do two things :
1. Filter out the publications that are completely relevant to the job description. 
"""