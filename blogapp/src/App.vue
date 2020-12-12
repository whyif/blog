
<template>
<v-app>
  <meta charset="utf-8">

    <v-navigation-drawer app clipped>
     <v-toolbar flat>
        <v-list>
          <v-list-tile>
            <v-list-tile-title class="title">
              Application
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-toolbar>
      <v-divider></v-divider>
       <v-list dense class="pt-0">
        <v-list-tile v-for="item in items" :key="item.key"  >
          
          <v-btn  block style="padding:30px" :color='btncolor' >
            <v-list-tile-action>
              <v-icon left >{{item.icon}}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title style="font-size:25px;">{{ item.items }}</v-list-tile-title>
            </v-list-tile-content>
          </v-btn>
        </v-list-tile>
        
      </v-list>


    </v-navigation-drawer>


  <v-app-bar app color="light-blue" dark style="font-size:50px;" clipped-left  src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
    lee's blog
  </v-app-bar><!-- 根据应用程序组件调整内容大小 -->
  
  <v-main><!-- 为应用程序提供正确的插槽 -->
    <v-container fluid  >

  <v-carousel v-model="model" cycle continuous>
    <v-carousel-item v-for="(color, i) in colors" :key="color" >
      <v-sheet :color="color" height="100%" tile>
        <v-row class="fill-height" align="center" justify="center">
          <div class="display-3">
            Slide {{ i + 1 }}
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>

      <v-row  dense>
        <v-col  v-for="item in blogs" :key="item.key">
          <v-card elevation='3' outline width="390" height="490">
            <v-img v-bind:src='item.imgsrc' height="320"></v-img>
            <!-- should use flask to build another backend -->
            <!-- <v-img  src='/home/lee/PycharmProjects/leeblog/blogapp/public/img/cat.jpeg'></v-img> -->
            <v-card-title>{{item.blogtitle}}</v-card-title>
            <v-card-text>
              {{item.blogtext}}
            </v-card-text>
            <v-btn color="info" right absolute>view more</v-btn>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>

  <v-footer app>
    <!-- -->
  </v-footer>
</v-app>

</template>


<script>
import {
  mdiAccount,
  mdiCommentQuestionOutline,
  mdiBug,
  mdiFeather,mdiGithub,
  } from '@mdi/js'

export default {
  name: 'App',
  data: () => ({
    model: 0,
      colors: [
        'primary',
        'secondary',
        'yellow darken-2',
        'orange',
      ],
    btncolor:'',
    items:[
      {
        icon:mdiAccount,
        items:'User'
      },
      {
        icon:mdiCommentQuestionOutline,
        items:"Questions"
      },
 
      {
        icon:mdiFeather,
        items:"share ideas"
      },
      {
        icon:mdiBug,
        items:"Report Bugs"
      },
      {
        icon:mdiGithub,
        items:"github"
      }

    ],
    blogs:[
      {
        blogtitle:'READ ME',
        blogtext:'please read me before using!',
        imgsrc:'https://cdn.vuetifyjs.com/images/cards/cooking.png',
        src:''
      },
      {
        blogtitle:'title1',
        blogtext:'text1dljslkdjkasdlkajsdkasdjakldadslkjs',
        imgsrc:'https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg',
        src:''
      },
      {
        blogtitle:'title2',
        blogtext:'text2',
        imgsrc:'https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg',
        src:''
      },
    ]
  }),
};
</script>