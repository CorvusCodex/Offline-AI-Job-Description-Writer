from utils import run_llama

def job_description(role, skills):
    prompt = f"Write a job description for the role {role} requiring these skills: {skills}"
    return run_llama(prompt)

if __name__ == "__main__":
    role = input("Role: ")
    skills = input("Skills: ")
    print(job_description(role, skills))
