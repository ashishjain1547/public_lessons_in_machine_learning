import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;
import weka.classifiers.functions.LinearRegression;

public class Regression{
	public static void main(String args[]) throws Exception{
		//Load Data set
		DataSource source = new DataSource("/home/ashish/Desktop/ws/weka/e4_linear_regression_using_java_code/house.arff");
		Instances dataset = source.getDataSet();
		//set class index to the last attribute
		dataset.setClassIndex(dataset.numAttributes()-1);
		
		//Build model
		LinearRegression model = new LinearRegression();
		model.buildClassifier(dataset);
		//output model
		System.out.println("LR FORMULA : "+model);	
		
		// Now Predicting the cost 
		Instance myHouse = dataset.lastInstance();
		double price = model.classifyInstance(myHouse);
		System.out.println("-------------------------");	
		System.out.println("PRECTING THE PRICE : "+price);	
	}
}