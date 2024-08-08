import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE HTML>
<html>
<head>
<title>Movie Store | Recent Movies</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
<!-- start plugins -->
<script type="text/javascript" src="js/jquery-1.11.1.min.js"></script>
<link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:100,200,300,400,500,600,700,800,900' rel='stylesheet' type='text/css'>
<script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
<style type="text/css" media="screen">
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
<script src="js/responsiveslides.min.js"></script>
<script>
    $(function () {
      $("#slider").responsiveSlides({
        auto: true,
        nav: true,
        speed: 500,
        namespace: "callbacks",
        pager: true,
      });
    });

    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tile', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });
</script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>
<!-- Trailer Video Modal -->
<div class="modal" id="trailer">
  <div class="modal-dialog">
    <div class="modal-content">
      <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
      </a>
      <div class="scale-media" id="trailer-video-container">
      </div>
    </div>
  </div>
</div>
<div class="container">
  <div class="container_wrap">
    <div class="header_top">
        <div class="col-sm-3 logo"><a href="index.html"><img src="images/logo.png" alt=""/></a></div>
      <div class="clearfix"> </div>
        </div>
        <div class="slider">
     <div class="callbacks_container">
        <ul class="rslides" id="slider">
          {movie_featured}
        </ul>
      </div>
      </div>
      <div class="content">
        <div class="box_1">
         <h1 class="m_2">Recent Movies</h1>
         
    <div class="clearfix"> </div>
    </div>
    <div class="box_2">
      
      {movie_tiles}

      <div class="clearfix"> </div>
    </div>

      </div>
   </div>
 </div>
</body>
</html>
'''

# A single movie for featured slider
movie_featured_content = '''
<li><img src="{slider_image_url}" class="img-responsive" alt=""/>
      <div class="button">
      <a href="#" class="hvr-shutter-out-horizontal movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Watch Now</a>
    </div>
</li>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-4">
  <div class="col_2">
    <div class="m_7 movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><img src="{poster_image_url}" class="img-responsive cover" alt=""/></div>
    <div class="caption1">
          <p class="m_3">{movie_title}</p>
    </div>
        <ul class="list_4">
          <li><p><b>Storyline</b> : {movie_storyline}</p></li>
        <li><b>Rating</b> : &nbsp;&nbsp;<p><img src="images/rating{movie_rating}.png" alt=""></p></li>
        <li><b>Release</b> : &nbsp;<span class="m_4">{movie_release_date}</span> </li>
        <div class="clearfix"> </div>
      </ul>
    </div>
</div>
'''

def create_movie_featured_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        if movie.featured_movie == True:
          # Extract the youtube ID from the url
          youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
          youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
          trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

          # Append the tile for the movie with its content filled in
          content += movie_featured_content.format(
              slider_image_url=movie.slider_image_url,
              trailer_youtube_id=trailer_youtube_id
          )
    return content

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    total = 0
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        #check if new row
        if total == 0:
            row = '''<div class="row">'''
        elif total % 3 == 0:
            row = '''</div><div class="row">'''
        else:
            row = ''

        if len(movies) - 1 == total:
            row_end = '''</div>'''
        else:
            row_end = ''

        total = total + 1

        # Append the tile for the movie with its content filled in
        content += row + movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_release_date=movie.release_date,
            movie_rating=movie.rating,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        ) + row_end
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(
                      movie_tiles=create_movie_tiles_content(movies),
                      movie_featured=create_movie_featured_content(movies)
                    )

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible