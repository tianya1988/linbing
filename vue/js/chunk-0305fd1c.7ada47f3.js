(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0305fd1c"],{"0bbb":function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("Card",[a("Table",{attrs:{border:"",editable:"",searchable:"","search-place":"top",data:e.tableData,columns:e.columns}}),a("Page",{staticClass:"page",attrs:{current:this.page.pageNum,"page-size":this.page.pageSize,total:this.page.count,"page-size-opts":[5,10],"show-sizer":"","show-elevator":"","show-total":""},on:{"on-change":e.handlePage,"on-page-size-change":e.handlePageSize}})],1)],1)},s=[],i=a("60e8"),_=i["a"],c=(a("dce2"),a("2877")),o=Object(c["a"])(_,r,s,!1,null,null,null);t["default"]=o.exports},"60e8":function(module,__webpack_exports__,__webpack_require__){"use strict";var _libs_crypto__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__("e0ac"),_libs_http__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__("b1d0"),_libs_util__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__("c276");__webpack_exports__["a"]={inject:["reload"],name:"tables_page",data:function(){var e=this;return{token:Object(_libs_util__WEBPACK_IMPORTED_MODULE_2__["i"])(),page:{pageNum:1,pageSize:5,count:0},columns:[{title:"目标",key:"target",sortable:!0,resizable:!0,width:150},{title:"描述",key:"description",sortable:!0,resizable:!0,width:260},{title:"创建时间",key:"create_time",resizable:!0,width:260},{title:"漏洞数量",key:"vulner_number",resizable:!0,width:150},{title:"扫描状态",key:"scan_status",resizable:!0,width:150},{title:"操作",key:"action",resizable:!0,width:250,align:"center",render:function(t,a){return t("div",[t("Button",{props:{type:"primary",size:"small"},style:{marginRight:"20px"},on:{click:function(){e.show(a)}}},"漏洞详情"),t("Button",{props:{type:"primary",size:"small"},style:{marginRight:"20px"},on:{click:function(){e.restore(a)}}},"恢复"),t("Button",{props:{type:"error",size:"small"},on:{click:function(){e.delete(a)}}},"彻底删除")])}}],tableData:[]}},methods:{getTableData:function getTableData(){var _this2=this,data={pagenum:this.page.pageNum,pagesize:this.page.pageSize,flag:"1",token:this.token.trim()};data=JSON.stringify(data);var params={data:_libs_crypto__WEBPACK_IMPORTED_MODULE_0__["a"].Encrypt(data)};_libs_http__WEBPACK_IMPORTED_MODULE_1__["a"].post("/api/targetlist",params).then(function(res){switch(res.data=eval("("+res.data+")"),res.data.code){case"Z1000":""!==res.data.data.result&&(_this2.tableData=res.data.data.result),_this2.page.count=res.data.data.total;break;case"Z1001":_this2.$Notice.error({title:"获取数据失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1002":_this2.$Notice.error({title:"获取数据失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1004":_this2.$Notice.error({title:"获取数据失败",desc:"认证失败,请稍后再次尝试"});break;case"Z1009":_this2.$Notice.info({title:"数据为空",desc:"数据为空,请新建笔记"});break;default:break}})},show:function(e){this.$router.push({name:"漏洞详情",query:{params:e["row"]["target"]}})},restore:function restore(params){var _this3=this,flag={type:"target",data:"0"},data={target:params.row.target,flag:flag,token:this.token.trim()};data=JSON.stringify(data);var req_params={data:_libs_crypto__WEBPACK_IMPORTED_MODULE_0__["a"].Encrypt(data)};_libs_http__WEBPACK_IMPORTED_MODULE_1__["a"].post("/api/setflag",req_params).then(function(res){switch(res.data=eval("("+res.data+")"),res.data.code){case"Z1000":_this3.reload();break;case"Z1001":_this3.$Notice.error({title:"请求失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1002":_this3.$Notice.error({title:"请求失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1004":_this3.$Notice.error({title:"请求失败",desc:"认证失败,请稍后再次尝试"});break;default:break}})},delete:function _delete(params){var _this4=this,flag={type:"target"},data={flag:flag,target:params.row.target,token:this.token.trim()};data=JSON.stringify(data);var req_params={data:_libs_crypto__WEBPACK_IMPORTED_MODULE_0__["a"].Encrypt(data)};_libs_http__WEBPACK_IMPORTED_MODULE_1__["a"].post("/api/delete",req_params).then(function(res){switch(res.data=eval("("+res.data+")"),res.data.code){case"Z1000":_this4.reload();break;case"Z1001":_this4.$Notice.error({title:"请求失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1002":_this4.$Notice.error({title:"请求失败",desc:"系统发生异常,请稍后再次尝试"});break;case"Z1004":_this4.$Notice.error({title:"请求失败",desc:"认证失败,请稍后再次尝试"});break;default:break}})},handlePage:function(e){this.page.pageNum=e,this.getTableData()},handlePageSize:function(e){this.page.pageSize=e,this.getTableData()}},mounted:function(){this.getTableData()}}},"9b59":function(e,t,a){},dce2:function(e,t,a){"use strict";var r=a("9b59"),s=a.n(r);s.a}}]);