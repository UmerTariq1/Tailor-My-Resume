
### **Project Overview**

This project is a specialized extension of the `lib_resume_builder_AIHawk` package ([https://github.com/feder-cr/lib_resume_builder_AIHawk](https://github.com/feder-cr/lib_resume_builder_AIHawk)). While the original package focuses on generating resumes from scratch, this application prioritizes tailoring your existing resume to specific job descriptions, ensuring optimal relevance and impact.

### **Key Features**

* **Enhanced Customization:** Provide your existing resume as input for highly personalized tailoring.
* **Focus on Relevance:**  Filter out irrelevant details and highlight the most pertinent experiences based on the job description.
* **Keyword Optimization:**  Strategically include keywords from the job description to boost visibility in Applicant Tracking Systems (ATS).
* **Simplified Workflow:**  A user-friendly Gradio interface streamlines the process for users of all technical backgrounds.

### **Getting Started**

1. **Prerequisites:**
   * **`lib_resume_builder_AIHawk` Library:** Follow the installation instructions on the official project page ([https://github.com/feder-cr/lib_resume_builder_AIHawk](https://github.com/feder-cr/lib_resume_builder_AIHawk)) to install the `lib_resume_builder_AIHawk` library. This provides the core functionality for interacting with OpenAI's GPT models.
   * **YAML Configuration:**  For configuration details related to OpenAI API keys and other settings, refer to the well-documented YAML setup instructions in the  `Auto_Jobs_Applier_AIHawk` project ([https://github.com/feder-cr/Auto_Jobs_Applier_AIHawk](https://github.com/feder-cr/Auto_Jobs_Applier_AIHawk)). This project provides a solid foundation for understanding YAML configuration in this context.

2. **Installation:**
   * Clone this repository: `git clone https://github.com/your_username/tailored_resume_generator`
   * Get the location of the installed library using "pip show lib_resume_builder_AIHawk" command.
   * **Replace the `lib_resume_builder_AIHawk` Library:** Replace the `lib_resume_builder_AIHawk` library folder that is just installed with the folder from this repository.
   * Install the additional project dependencies: `pip install -r requirements.txt` from this repo


4. **Usage:**
   * After the repo replication work is done and libraries are installed and YAML configurations are also set then: 
   * Run the application: `python main.py`
   * The Gradio interface will open, prompting you to:
     * Upload your existing resume
     * Enter the job description
     * Choose an output file name
   * Click "Generate Resume" to create the tailored resume.

### **Why Keep the Same Name?**

Maintaining the same name as the original `lib_resume_builder_AIHawk` package demonstrates a clear connection and respect for the original project. It also helps users recognize the core functionality and understand that this project is a specialized extension, rather than a completely new concept.

### **How it Works**

1. **Resume Upload:** Share your existing resume as input, providing the foundation for personalization. Put as much detail as you want in the resume.yaml file. The file is supposed to be an exhaustive list of your skills, experience and etc.
2. **Job Description Analysis:** The application extracts key requirements and keywords from the provided job description.
3. **Resume Enhancement:** Relevant sections within your resume are identified, and the content is tailored to match the extracted keywords and specific job description criteria.
4. **Output:** The enhanced and personalized resume is saved to your chosen output file name.



### **Contributing**

We welcome contributions to this project! Please feel free to submit issues or pull requests.

### **Acknowledgements**

This project builds upon the excellent work of the `lib_resume_builder_AIHawk` package. We also acknowledge the valuable insights provided by the `Auto_Jobs_Applier_AIHawk` project for understanding YAML configuration within this context.
