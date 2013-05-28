desc "Generate splash page from HAML template"
task :generate_splash_page do
  sh "haml aperature\\splash-page.haml > aperature\\splash-page.html"
end

task :run => :generate_splash_page do
  sh "python aperature\\gui.py"
end
