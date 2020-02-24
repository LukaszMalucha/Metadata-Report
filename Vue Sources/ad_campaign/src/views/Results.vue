<template>
  <div class="row plain-element">
    <div v-if="thompson_list" id="page-index">
      <div class="row plain-element" id="Environment">
        <div class="row campaign-header">
          <div class="row" id="headerEnvironment">
            <div class="col-xs-12 col-sm-12 col-md-3 col-lg-2 text-left plain-element">
              <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/environment.jpg" class="img responsive campaign-restbank" alt="Campaign Results">
            </div>
            <div class="col-xs-12 col-sm-12 col-md-9 col-lg-10 plain-element">
              <div class="row summary">
                <div class="box">
                  <h5>Peek into Crystal Ball - proposed advert designs with conversion rates</h5>
                </div>
                <p>So what are the Ad tastes of an statistical RestBank Customer? According to previous page survey we can
                clearly see now which Ad will be able to convince <span class="purple-font">21%</span> to buy a Home Insurance.
                But in the real world we won't have a crystal ball - so it's just an assumption for the simulation purposes.
                That's why <span class="purple-font">AI Algorithm</span> won't have that knowledge.
                It'll have to figure it out through observation of customer's consecutive choices. </p>
              </div>
            </div>
          </div>
          <div class="row" id="headerResults">
            <div class="col-xs-12 col-sm-12 col-md-3 col-lg-2 text-left plain-element">
              <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/results.jpg" class="img responsive campaign-restbank" alt="Campaign Results">
            </div>
            <div class="col-xs-12 col-sm-12 col-md-9 col-lg-10 plain-element">
              <div class="row summary">
                <div class="box">
                  <h5>Thompson Sampling Algorithm vs. Random Choice</h5>
                </div>
                <p>As we see on graphs below, our AI algorithm was able to figure it out much faster and with greater
                      precision that Ad Project <span class="purple-font">"{{thompson_list[0][0]}}"</span> will have the greatest conversion rate. Algorithm
                      decided to display
                      it <span class="purple-font">{{thompson_list[0][3]}}</span> times to customers (compared with <span class="purple-font">{{random_list[0][3] }}</span> of Random
                      Sampling), achieving overwhelming
                      confidence in superiority of Project <span class="purple-font">"{{thompson_list[0][0]}}"</span>. Just with the small sample of 10.000 bank
                      customers we're
                      able to save <span class="purple-font">{{relative_return}}%</span> costs compared to Random Sampling benchmark method. Enough
                      to impress
                      Management?</p>
              </div>
            </div>
          </div>
        </div>
      <div class="dashboard-cards">
        <div class="row row-campaign">
          <div class="col-md-3 col-left">
            <div class="section-left" id="sectionLeftEnvironment">
              <div class="section-heading text-left">
                10.000 Rounds
              </div>
              <p>With every round <span class="purple-font">Thompson Sampling</span> algorithm will narrow the choice of displayed Ads. In simplified example,
              if among first 100 customers none of them clicked on project <span class="purple-font">"Family + Car"</span>, then
              that proposal will be greatly omitted during the rounds 101-200 in a favor of more popular chioices.
              </p>
              <div class="section-heading text-left">
                The Benchmark
              </div>
               <p>Random Sampling - that's what we play against. On each of <span class="purple-font">10.000</span> rounds we'll display random Project to our customer.
               Bottom line is why do we bother our Management with this whole "AI" if we can't do significantly better than Random...
                </p>
              <div class="section-heading text-left">
                What A.I. doesn't know?
              </div>
               <p>We'll compare absolute and relative returns between Random Sampling and <span class="purple-font">Thompson Sampling</span> methods.
               RESTBank's profit on each insurance is <span class="purple-font">10.000 USD</span> and that's how much is worthy one
                </p>
            </div>
            <div class="section-left" id="sectionLeftResults">
              <div class="section-heading text-left">
                The Winning Advert
              </div>
              <div class="single-advert-left">
                <img :src='"https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/" + percentage_scores[0][0] + ".png"'
                     class="img responsive img-advert-medium" alt="Ad Campaign"/>
              </div>
              <div class="single-advert-content content-side text-left">
              <p><span class="purple-font">Conversion Rate: 21%</span><br>
                  {{thompson_list[0][0]}}</p>
              </div>
              <div class="section-heading text-left">
                The Time
              </div>
              <p>Thanks to Probability Matching Strategy AI was analyzing feedback received from the Customers in
                          a real-time. It didn't had to wait until the very last round to draw conclusion.
              </p>
              <div class="section-heading text-left">
                The Profit
              </div>
               <p>Just with the small sample of 10.000 bank customers we're able to create
                          <span class="purple-font">{{absolute_return}}</span> USD absolute
                    return which was <span class="purple-font">{{relative_return}}%</span> bigger than return achieved with Random Sampling.
                </p>
               <div class="row plain-element">
                 <button  onclick="window.location.href='/'" type="submit" class="btn btn-form"><span><i class="far fa-arrow-alt-circle-right fa-rotate-180"></i></span> Back to Main Page </button>
              </div>

            </div>
          </div>
          <div class="col-md-9 col-right">
            <div class="section-right" id="sectionRightEnvironment">
              <div class="section-heading text-left">
                Conversion Rates according to customer preferences
              </div>
              <div class="row row-medium-adverts">
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-left">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/female_trust_cash.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['female_trust_cash']}}%</span><br>
                        Girl + Trust + Cash Bonus</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-center-left">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/female_trust_car.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['female_trust_car']}}%</span><br>
                        Girl + Trust + Car Insurance</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-center-right">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/female_familyhome_cash.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['female_familyhome_cash']}}%</span><br>
                        Girl + Family Home + Cash Bonus</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-right">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/female_familyhome_car.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['female_familyhome_car']}}%</span><br>
                        Girl + Family Home + Car Insurance</p>
                    </div>
                 </div>
              </div>
              <div class="row  row-medium-adverts">
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-left">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/family_trust_cash.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['family_trust_cash']}}%</span><br>
                        Family + Trust + Cash Bonus</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-center-left">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/family_trust_car.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['family_trust_car']}}%</span><br>
                        Family + Trust + Car Insurance</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-center-right">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/family_familyhome_cash.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['family_familyhome_cash']}}%</span><br>
                        Family + Family Home + Cash Bonus</p>
                    </div>
                 </div>
                 <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 col-advert-right">
                    <div class="single-advert-left">
                      <img src="https://leanbank.s3-eu-west-1.amazonaws.com/static/img/campaign/family_familyhome_car.png"
                           class="img responsive img-advert-medium" alt="Ad Campaign"/>
                    </div>
                    <div class="single-advert-content content-side text-left">
                    <p><span>Conversion Rate: {{ scores['family_familyhome_car']}}%</span><br>
                         Family + Family Home + Car Insurance</p>
                    </div>
                 </div>
              </div>
              <br>
              <div class="row plain-element">
                  <div class="col-md-4 col-lg-4">
                       <button @click="showResults" type="submit" class="btn btn-form"><span>Apply Thompson Sampling Algorithm <i class="far fa-arrow-alt-circle-right"></i></span></button>
                  </div>
              </div>
              <div class="row row-medium-adverts">
                <span class="inline-error">{{ error }}</span>
              </div>
            </div>
            <div class="section-right" id="sectionRightResults">
              <div class="section-heading text-left">
                AI. Algorithm vs. Benchmark Comparison
              </div>
              <div class="row plain-element">
                <div class="col-md-12 col-lg-12 text-center plain-element col-chart">
                    <thompson-chart  :chart-data="thompsonData" :styles="chartStyles"></thompson-chart>
                </div>
              </div>
              <hr>
              <div class="row plain-element">
                <div class="col-md-12 col-lg-12 text-center plain-element col-chart">
                    <random-chart  :chart-data="randomData" :styles="chartStyles"></random-chart>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  <div v-else id="page-index">
    <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Ad Campaign with AI</h4>
    </div>
    <div class="col-md-4 no-padding"></div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-campaign">
    <div class="row text-center">
          <h5>You have to define environment first:</h5>
    </div>
    <div class="row text-center">
          <button onclick="window.location.href='/ad-campaign'"  type="submit" class="btn btn-confirm btn-login">
          Ad Campaign
          </button>
    </div>
    </div>
  </div>
  </div>
</div>
</template>


<script>
import RandomChart from "@/common/RandomChart.js";
import ThompsonChart from "@/common/ThompsonChart.js";
import RowHeaderComponent from "@/components/RowHeader.vue";


export default {
  name: "Results",
  props: {
    results: {
      type: Object,
      required: false
    }
  },
  components: {
      RandomChart,
      ThompsonChart,
      RowHeaderComponent,
  },
  data() {
    return {
      error: null,
      percentage_scores: null,
      scores: {},
      ai_results: {},
      absolute_return: null,
      relative_return: null,
      thompson_list: null,
      random_list: null,
      top_ts_count: null,
      top_rs_count: null,
      scores_list: null,
      randomData: {},
      thompsonData: {},

    }
  },
  methods: {
    showResults() {
      document.getElementById("headerResults").style.display = "block";
      document.getElementById("sectionLeftResults").style.display = "block";
      document.getElementById("sectionRightResults").style.display = "block";
      document.getElementById("headerEnvironment").style.display = "none";
      document.getElementById("sectionLeftEnvironment").style.display = "none";
      document.getElementById("sectionRightEnvironment").style.display = "none";
      this.fillRandomChart();
      this.fillThompsonChart();
    },
    fillRandomChart() {
      var dataLabels = []
      var dataValues = []
      for (var i = 0; i < this.random_list.length; i++) {
          dataLabels.push(this.random_list[i] ? this.random_list[i][0] : '');
          dataValues.push(this.random_list[i] ? this.random_list[i][3] : '');
      }
      this.randomData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#356899", "#5789b6", "#7bb0d5", "#89bddc", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3"],
            data: dataValues
          }
        ]
      }
    },
    fillThompsonChart() {
      var dataLabels = []
      var dataValues = []
      for (var i = 0; i < this.thompson_list.length; i++) {
          dataLabels.push(this.thompson_list[i] ? this.thompson_list[i][0] : 'zxc');
          dataValues.push(this.thompson_list[i] ? this.thompson_list[i][3] : '');
      }
      this.thompsonData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#356899", "#5789b6", "#7bb0d5", "#89bddc", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3"],
            data: dataValues
          }
        ]
      }
    },

  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  mounted() {
  if (this.results) {
      document.getElementById("headerResults").style.display = "none";
      document.getElementById("sectionLeftResults").style.display = "none";
      document.getElementById("sectionRightResults").style.display = "none";
      }
  },

  created() {
    document.title = "Building Environment";
    if (this.results) {
         window.console.log(this.results);
        this.scores = this.results.scores;
        this.percentage_scores = this.results.percentage_scores;
        this.ai_results = this.results.ai_results;
        this.absolute_return = this.results.ai_results.absolute_return;
        this.relative_return = this.results.ai_results.relative_return;
        this.thompson_list = this.results.ai_results.thompson_list;
        this.random_list = this.results.ai_results.random_list;
        this.top_ts_count = this.results.ai_results.top_ts_count;
        this.top_rs_count = this.results.ai_results.top_rs_count;
        this.scores_list = this.results.ai_results.scores_list;
    }


  }

}
</script>