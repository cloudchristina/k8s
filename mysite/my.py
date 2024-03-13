def generate_blog_post():
    title = "My Journey: From Nursing to Tech Enthusiast"
    date = "March 13, 2024"

    who_am_i_section = '''
    <section class="blog-section">
        <h2>Who Am I?</h2>
        <p>I'm Christina Chen, and I'm thrilled to share a bit about myself and my journey with you. I've always been an adventurous spirit, whether it's hiking in the great outdoors, playing tennis, or indulging in my love for interstellar-type movies and being a super fan of The Big Bang Theory.</p>
    </section>
    '''

    my_passion_section = '''
    <section class="blog-section">
        <h2>My Passion</h2>
        <p>What drives me the most is my passion for technology. I'm deeply fascinated by its potential to transform and improve lives. That's why I've set my sights on becoming an outstanding DevOps Engineer and AI Ops Engineer. I believe these roles are at the forefront of leveraging technology to enhance human life and make our world a better place.</p>
    </section>
    '''

    special_things_about_me_section = '''
    <section class="blog-section">
        <h2>Special Things About Me</h2>
        <p>One thing that sets me apart is my unconventional career path. I spent over a decade working as a nurse, caring for others and making a difference in their lives. However, I couldn't shake the feeling that tech was my true calling. So, I made the bold decision to pivot my career and dive headfirst into the world of technology.</p>
        <p>This transition wasn't easy, but it was incredibly rewarding. It's taught me the value of perseverance, adaptability, and never being afraid to pursue my passions.</p>
    </section>
    '''

    blog_content = f'''
    <article class="blog-post">
        <h1>{title}</h1>
        <p class="date">Published on {date}</p>
        {who_am_i_section}
        {my_passion_section}
        {special_things_about_me_section}
    </article>
    '''

    html_template = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="styles.css"> <!-- Link to the CSS file -->
    </head>
    <body>
        <header class="header">
            <h1>My Personal Blog</h1>
        </header>
        <main class="content">
            {blog_content}
        </main>
        <footer class="footer">
            <p>&copy; 2024 Christina Chen</p>
        </footer>
    </body>
    </html>
    '''

    with open('personal_blog.html', 'w') as file:
        file.write(html_template)


if __name__ == "__main__":
    generate_blog_post()
