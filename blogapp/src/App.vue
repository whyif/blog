
<template>

<v-app>
  <v-main>
    <!-- <v-navigation-drawer clipped floating >
     
      <v-avatar color='primary' size='56' dark>lee</v-avatar> 
      navigation-drawer:
    </v-navigation-drawer> -->
    <v-navigation-drawer permanent >
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
          
          <v-btn  block style="padding:30px" :color='btncolor' v-on:click='changecolor'>
            <v-list-tile-action>
              <v-icon left>{{item.icon}}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title style="font-size:25px;">{{ item.items }}</v-list-tile-title>
            </v-list-tile-content>
          </v-btn>
        </v-list-tile>
        
      </v-list>
    </v-navigation-drawer>

    <v-container fluid>
    </v-container>
aaaaaaa

  </v-main>

  <v-app-bar app  color="light-blue" dark style="font-size:50px;" fixed>
    lee's blog
  </v-app-bar>


  <v-footer app>
    hei i'm footer
  </v-footer>  

</v-app>
</template>


<script>
import {
  mdiAccount,
  mdiCommentQuestionOutline,
  mdiBug,
  mdiFeather
  } from '@mdi/js'

export default {
  name: 'App',
  data: () => ({
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
        icon:mdiBug,
        items:"Report Bugs"
      },
      {
        icon:mdiFeather,
        items:"share ideas"
      }

    ],
  methods: {
    changecolor:function(){
      this.btncolor="primary"
    }
  },
  }),
};
</script>
